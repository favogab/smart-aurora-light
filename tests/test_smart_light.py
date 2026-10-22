# 
from smarthoi.smart_light import SmartLight

# 
def test_light_starts_off():
    light = SmartLight("light-1", "Living Room")
    assert light.get_status() == "OFF"

# 
def test_light_turns_on():
    light = SmartLight("light-1", "Living Room")
    light.turn_on()
    assert light.get_status() == "ON"

# 
def test_light_turns_off():
    light = SmartLight("light-1", "Living Room")
    light.turn_on()
    light.turn_off()
    assert light.get_status() == "OFF"


def test_repeated_on_command():
    light = SmartLight("light-1", "Living Room")
    light.turn_on()
    light.turn_on()
    assert light.get_status() == "ON"


def test_repeated_off_command():
    light = SmartLight("light-1", "Living Room")
    light.turn_off()
    light.turn_off()
    assert light.get_status() == "OFF"
