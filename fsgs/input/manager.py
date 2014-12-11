from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals


from .device import Device
from .enumeratehelper import EnumerateHelper


class DeviceManager(object):

    __instance = None

    @classmethod
    def instance(cls):
        if cls.__instance is None:
            helper = EnumerateHelper()
            cls.__instance = cls(helper)
        return cls.__instance

    def __init__(self, helper):
        self.helper = helper
        self.devices = []

    def get_devices(self):
        print("DeviceManager.get_devices")
        if self.helper is not None:
            self.helper.init()
            return self.helper.devices
        print("DeviceManager.get_devices ->", self.devices)
        return self.devices

    def add_joystick_device(self, event):
        device = Device()
        device.axes = event["axes"]
        device.balls = event["balls"]
        device.hats = event["hats"]
        device.buttons = event["buttons"]
        device.name = event["name"]
        device.id = event["id"]
        device.type = Device.TYPE_JOYSTICK
        self.devices.append(device)

    def add_keyboard_device(self, event):
        device = Device()
        device.name = event["name"]
        device.id = event["id"]
        device.type = Device.TYPE_KEYBOARD
        self.devices.append(device)

    def add_mouse_device(self, event):
        device = Device()
        device.name = event["name"]
        device.id = event["id"]
        device.type = Device.TYPE_MOUSE
        self.devices.append(device)
