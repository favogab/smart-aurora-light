# Smart Aurora Light

**Python-Powered Ambient Lighting & IoT Automation**

Smart Aurora Light is a Python-based project I'm building to explore how smart lighting systems work, from simple device controls to connected home automation.

The idea started with my interest in ambient lighting and how different colors, brightness levels, and lighting effects can change the atmosphere of a room. I wanted to understand what goes into building that experience myself, not just from the visual side, but from the software that controls it.

I'm starting with a simulated smart light and gradually developing it into a more complete IoT system. The long-term goal is to support customizable lighting effects, remote control, automation, real-time device monitoring, and eventually physical hardware.

## What I'm Building

The project begins with a single smart ambient light.

At its simplest, the light should respond to commands to turn on or off, change brightness, and display different RGB colors.

As development progresses, I plan to introduce lighting modes inspired by the kinds of effects found in ambient light projectors, including gradual color transitions, breathing effects, and aurora-style lighting.

Beyond the lighting effects, I also want to explore the engineering involved in building a connected device system: how devices communicate, how commands are validated, how state is tracked, and how to keep the system secure and reliable.

## Current Features

The first version focuses on the Python device model and automated testing.

**Implemented:**

- ON/OFF control with device state tracking.
- Adjustable brightness from 0% to 100%.
- RGB color control using red, green, and blue values.
- Input validation for brightness and RGB channels.
- Error handling for invalid values and unsupported input types.
- Consistent behavior when ON/OFF commands are repeated.
- Preservation of existing settings when invalid commands are rejected.
- Automated tests using pytest.

The current implementation runs locally as a simulation. It does not yet communicate with a physical light or use a network connection.

## Planned Features

### Ambient Lighting Effects

- Static color mode.
- Sunset-inspired color transitions.
- Aurora-inspired lighting effects.
- Breathing and fading brightness effects.
- Customizable colors and brightness for different lighting modes.

### IoT Communication

- MQTT messaging between devices and the application.
- Device state reporting and synchronization.
- Remote commands for controlling connected lights.
- Reliable handling of device connectivity and communication failures.

### Backend and Web Dashboard

- FastAPI backend for device management and control.
- Web dashboard for controlling lights through a browser.
- Real-time updates using WebSockets.
- SQLite database for storing device information and settings.
- Lighting presets, scheduling, and automation rules.

### Security and Reliability

- Validation of incoming device commands.
- Authentication and authorization for remote access.
- Secure communication between application components.
- Safe handling of invalid commands and disconnected devices.
- Automated testing of device behavior and failure scenarios.

### Hardware Integration

- Explore ESP32-based lighting control.
- Connect the application to physical RGB lighting hardware.
- Test how software commands translate into real device behavior.
- Expand support for additional smart-home devices where practical.

These features are planned and will be implemented incrementally.

## Tech Stack

### Currently Used

| Technology | Purpose |
|---|---|
| Python | Device modeling and control logic |
| pytest | Automated testing |
| Git | Version control |
| GitHub | Source code hosting and development history |

### Planned

| Technology | Purpose |
|---|---|
| MQTT / Mosquitto | Communication between connected devices |
| FastAPI | Backend API |
| SQLite | Device settings and application data |
| WebSockets | Real-time updates |
| HTML, CSS, JavaScript | Web-based control dashboard |
| ESP32 | Potential physical lighting controller |

The technology choices may evolve as the project grows.

## Current Progress

- [x] Day 1 — SmartLight class and ON/OFF state management
- [x] Day 2 — Python package structure and automated tests
- [ ] Day 3 — Brightness and RGB color control
- [ ] Day 4 — Device state validation
- [ ] Day 5 — MQTT communication
- [ ] Day 6 — MQTT state reporting
- [ ] Day 7 — Integration and testing

## Running the Tests

Create and activate a Python virtual environment, then install the development dependencies:

```bash
python -m pip install -e ".[dev]"
```

### 4. Run the Tests

```bash
python -m pytest -v
```

All tests should pass when the environment is configured correctly.

## Inspiration

This project was inspired by ambient lighting products such as the Havie lamp.

What interested me was the experience of using color, brightness, and changing lighting effects to create different moods. That made me curious about how I could design and program a similar experience myself.

Rather than recreating an existing product, I'm using the idea as a starting point to learn more about Python application development, device control, IoT communication, and automation.

Smart Aurora Light is an independent project and is not affiliated with, endorsed by, or developed by Havie.

## Development Status

**Status: Early development — Python device simulation**

The core light model currently supports ON/OFF commands, brightness adjustment, RGB colors, and input validation. These features are covered by automated tests.

The project is being developed incrementally, with an emphasis on understanding software engineering, IoT architecture, security, and real-world device integration.