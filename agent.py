import time
from prometheus_client import query_prometheus
from llm_brain import llm_decide
from actions import scale
from config import *

def get_latency():

    query = 'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[1m]))'

    result = query_prometheus(query)

    if not result:
        return 0

    return float(result[0]["value"][1])


def controller():

    print("Latency AI Agent Started")

    while True:

        latency = get_latency()

        print(f"[METRIC] Latency: {latency}")

        decision = llm_decide(latency)

        print(f"[LLM] Decision: {decision}")

        if "SCALE_DEPLOYMENT" in decision:

            scale(DEPLOYMENT_NAME, NAMESPACE, SCALE_REPLICAS)

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    controller()