class Outlet(object):
    def __init__(self, api, outlet_data):
        self._api = api
        self._id = outlet_data['id']

    def switch_outlet(self, state):
        self._api.switch_outlet(self._id, state)

    def get_state(self):
        self._api.get_devices()
