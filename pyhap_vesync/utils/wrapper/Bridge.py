from pyhap.accessory import Bridge as HAPBridge
from .API import API


class Bridge(HAPBridge):
    def __init__(self, username, password, display_name, driver, *args, **kwargs):
        super().__init__(driver=driver, display_name=display_name)
        self.api = API(username, password)
        [self.add_accessory(outlet) for outlet in self.api.outlets]
