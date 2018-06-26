from pyhap_vesync.utils.vesync import API as VAPI
from pyhap_vesync.utils.wrapper import Outlet


class API(VAPI):
    outlets = []

    def __init__(self, driver, username, password):
        super().__init__(username, password)
        self.driver = driver

    def get_devices(self):
        super().get_devices()
        if not self.outlets:
            self.outlets = [Outlet(self, outlet) for outlet in self._devices]
        else:
            for outlet in self._devices:
                existing = [x for x in self.outlets if x._outlet._id == outlet['id']]
                if existing:
                    if existing[0].on_char.get_value() == 1 and outlet['relay'] == Outlet.OFF:
                        existing[0].on_char.set_value(0)
                    elif existing[0].on_char.get_value() == 0 and outlet['relay'] == Outlet.ON:
                        existing[0].on_char.set_value(1)
                else:
                    new_outlet = Outlet(self.driver, self, outlet)
                    self.outlets.append(new_outlet)
