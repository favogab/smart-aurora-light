# SmartHoi 

**Smart Home Control & Automation — Built with Python**

SmartHoi is a Python-based IoT project focused on developing a secure, modular smart-home control and automation system.

The project begins with a simulated smart ambient light inspired by modern mood-lighting devices. The goal is to gradually evolve it into a connected system that supports device control, customizable lighting, automation, real-time monitoring, and eventually physical hardware.

## Project Goals

- Build reusable Python models for smart-home devices.
- Implement ON/OFF control, brightness, RGB colors, and lighting effects.
- Introduce MQTT for communication between devices and the backend.
- Develop a FastAPI backend and web dashboard.
- Add automation rules, scheduling, and device monitoring.
- Prioritize secure communication, authentication, and reliable device behavior.
- Explore integration with physical IoT hardware.

## Tech Stack

**Current:** Python, pytest, Git

**Planned:** MQTT, Mosquitto, FastAPI, SQLite, WebSockets, HTML, CSS, JavaScript, and ESP32.

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

Run the test suite:

```bash
python -m pytest -v
```

## Development Status

SmartHoi is in early development. The current implementation simulates a smart light locally; no physical hardware is connected yet.

The project is being developed incrementally, with an emphasis on understanding software engineering, IoT architecture, security, and real-world device integration.