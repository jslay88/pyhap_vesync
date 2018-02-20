from pyhap_vesync.utils.vesync import API as VAPI
from pyhap_vesync.utils.wrapper import Outlet


class API(VAPI):
    outlets = []

    def get_devices(self):
        super().get_devices()
        self.outlets = [Outlet(self, outlet) for outlet in self._devices]
