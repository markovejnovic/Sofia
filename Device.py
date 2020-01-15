import enum
import abc

class DeviceType(enum.Enum):
    Binary = 1
    Generic = -1

class Device:
    """General type device"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.type = DeviceType.Generic

    def serialize(self):
        return {'id': self.id, 'name': self.name, 'type': self.type.name}

    def serialize_long(self):
        return {'id': self.id, 'name': self.name, 'type': self.type.name}

class BinaryDevice(Device):
    """Devices with a binary state, like lights"""
    def __init__(self, id, name):
        Device.__init__(self, id, name)
        self.type = DeviceType.Binary

    @abc.abstractmethod
    def on(self):
        pass

    @abc.abstractmethod
    def off(self):
        pass

    @abc.abstractmethod
    def toggle(self):
        pass

    def parse_cmd(self, arg):
        if arg == 'on':
            self.on()
        elif arg == 'off':
            self.off()
        elif arg == 'toggle':
            self.toggle()
        else:
            return 405

        return 200
