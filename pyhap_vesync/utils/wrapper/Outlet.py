import threading
import pyhap.loader as loader
from pyhap.accessory import Accessory
from pyhap.const import CATEGORY_OUTLET
from pyhap_vesync.utils.vesync import Outlet as VOutlet


class Outlet(Accessory):
    category = CATEGORY_OUTLET
    ON = 'open'
    OFF = 'break'

    def __init__(self, driver, api, outlet_data, *args, **kwargs):
        self._outlet = VOutlet(api, outlet_data)
        self._api = api
        super().__init__(driver=driver, display_name=outlet_data['deviceName'], *args, **kwargs)

    def hk_callback(self, new_value):
        threading.Thread(target=self._outlet.switch_outlet, args=[new_value]).start()

    def get_status(self):
        self._api.get_devices()
        return self.on_char.value

    def _set_services(self):
        super()._set_services()

        outlet_service = loader.get_serv_loader().get('Outlet')
        self.add_service(outlet_service)
        self.on_char = outlet_service.get_characteristic('On')
        self.on_char.setter_callback = self.hk_callback
        self.on_char.getter_callback = self.get_status
