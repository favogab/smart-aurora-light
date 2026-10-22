
class SmartLight:
    def __init__(self, device_id, name):
        self.device_id = device_id
        self.name = name
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def get_status(self):
        return "ON" if self.is_on else "OFF"
