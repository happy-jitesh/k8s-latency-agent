from kubernetes import client, config

def init():

    try:
        config.load_incluster_config()
    except:
        config.load_kube_config()

    return client.AppsV1Api()