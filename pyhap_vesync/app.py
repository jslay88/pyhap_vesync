import signal
import argparse

from pyhap.accessory_driver import AccessoryDriver
from pyhap_vesync.utils.wrapper import Bridge


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Vesync HomeKit Bridge.'
                                                 'Allows you to setup a Etekcity Vesync account '
                                                 'as a HomeKit Bridge for iOS devices.')
    parser.add_argument('-u', '--username', type=str, required=True, help='Vesync Username (usually an email address.')
    parser.add_argument('-p', '--password', type=str, required=True, help='Vesync Password')

    args = parser.parse_args()

    bridge = Bridge(args.username, args.password, 'Vesync Bridge')
    driver = AccessoryDriver(bridge, 51827)
    signal.signal(signal.SIGINT, driver.signal_handler)
    signal.signal(signal.SIGTERM, driver.signal_handler)
    driver.start()
