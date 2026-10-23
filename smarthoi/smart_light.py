
class SmartLight:
    def __init__(self, device_id, name):
        self.device_id = device_id
        self.name = name
        self.is_on = False
        self.brightness = 100
        self.color = (255, 255, 255)

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def get_status(self):
        return "ON" if self.is_on else "OFF"

    def set_brightness(self, value):
        if type(value) is not int:
            raise TypeError("Brightness must be an integer")

        if not 0 <= value <= 100:
            raise ValueError(
                "Brightness must be between 0 and 100"
            )

        self.brightness = value

    def set_color(self, red, green, blue):
        channels = (red, green, blue)

        for channel in channels:
            if type(channel) is not int:
                raise TypeError(
                    "RGB channels must be integers"
                )

            if not 0 <= channel <= 255:
                raise ValueError(
                    "RGB channels must be between 0 and 255"
                )

        self.color = channels
