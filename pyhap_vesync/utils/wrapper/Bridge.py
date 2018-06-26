from pyhap.accessory import Bridge as HAPBridge
from .API import API


class Bridge(HAPBridge):
    def __init__(self, username, password, display_name, *args, **kwargs):
        super().__init__(display_name=display_name, *args, **kwargs)
        self.api = API(username, password)
        [self.add_accessory(outlet) for outlet in self.api.outlets]
