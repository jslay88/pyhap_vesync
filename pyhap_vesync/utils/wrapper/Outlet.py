import threading
import pyhap.loader as loader
from pyhap.accessory import Accessory, Category
from pyhap_vesync.utils.vesync import Outlet as VOutlet


class Outlet(Accessory):
    category = Category.OUTLET

    def __init__(self, api, outlet_data, *args, **kwargs):
        self._outlet = VOutlet(api, outlet_data)
        super().__init__(outlet_data['deviceName'], *args, **kwargs)

    def hk_callback(self, new_value):
        threading.Thread(target=self._outlet.switch_outlet, args=[new_value]).start()

    def _set_services(self):
        super()._set_services()

        outlet_service = loader.get_serv_loader().get('Outlet')
        self.add_service(outlet_service)
        self.on_char = outlet_service.get_characteristic('On')
        self.on_char.setter_callback = self.hk_callback
