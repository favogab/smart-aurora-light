# 
from smart_aurora_light.smart_light import SmartLight
import pytest

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


def test_default_brightness():
    light = SmartLight("light-1", "Living Room")
    assert light.brightness == 100


def test_set_brightness():
    light = SmartLight("light-1", "Living Room")
    light.set_brightness(50)
    assert light.brightness == 50


def test_invalid_brightness():
    light = SmartLight("light-1", "Living Room")

    with pytest.raises(ValueError):
        light.set_brightness(150)

    assert light.brightness == 100


@pytest.mark.parametrize("brightness", [0, 100])
def test_brightness_boundaries(brightness):
    light = SmartLight("light-1", "Living Room")

    light.set_brightness(brightness)

    assert light.brightness == brightness


def test_negative_brightness():
    light = SmartLight("light-1", "Living Room")

    with pytest.raises(ValueError):
        light.set_brightness(-10)

    assert light.brightness == 100


def test_wrong_brightness_type():
    light = SmartLight("light-1", "Living Room")

    with pytest.raises(TypeError):
        light.set_brightness(True)

    assert light.brightness == 100


def test_set_color():
    light = SmartLight("light-1", "Living Room")
    light.set_color(128, 0, 255)
    assert light.color == (128, 0, 255)


def test_invalid_color():
    light = SmartLight("light-1", "Living Room")

    with pytest.raises(ValueError):
        light.set_color(255, 100, 999)

    assert light.color == (255, 255, 255)
