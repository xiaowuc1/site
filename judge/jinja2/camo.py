from judge.utils.camo import client as camo_client

from . import registry

@registry.function
def camo(url):
    return camo_client.image_url(url)