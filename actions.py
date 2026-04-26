from k8s_client import init
from config import MAX_REPLICAS

apps = init()

def scale(deployment, namespace, replicas):

    dep = apps.read_namespaced_deployment(deployment, namespace)

    if dep.spec.replicas >= MAX_REPLICAS:
        print("Max replicas reached")
        return

    dep.spec.replicas = replicas

    apps.patch_namespaced_deployment(deployment, namespace, dep)

    print(f"Scaled to {replicas}")