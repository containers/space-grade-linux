# Autonomous Drone Control with Joystick Integration (Initial Support for Tello)

This project provides a Python-based framework for controlling drones, initially supporting DJI Tello drones using the `djitellopy` library. The script supports joystick integration for manual control and autonomous movements as a fallback. The framework is designed to be extensible for other drones by modifying the drone-specific logic.

## Features

- **Wi-Fi Management:** Scans for available Wi-Fi networks and manages connections dynamically.
- **Joystick Control:** Supports joystick-based manual control using `pygame`.
- **Autonomous Control:** Performs predefined movements if no joystick is detected.
- **Modular Design:** Can be extended to support additional drones.
- **Safety Features:** Ensures safe landing and error handling during operations.
- **Logging:** Provides detailed logging for debugging and operational insights.

## Requirements

- Python 3.7 or later
- A compatible drone (initially tested with DJI Tello)
- PlayStation 5 controller (or any joystick supported by `pygame`)
- USB-C cable for joystick connection
- Dependencies:
  - `djitellopy` for Tello drone control: `pip install djitellopy`
  - `pygame` for joystick input: `pip install pygame`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dougsland/autonomous_drones
   cd autonomous_drones
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the `nmcli` tool is installed and accessible for managing Wi-Fi connections.

## Usage

1. **Power on the Drone:**
   - For DJI Tello, power on the drone and wait for the Wi-Fi SSID to become available.

2. **Run the Script:**
   ```bash
   python main.py
   ```

3. **Joystick Connection:**
   - Connect a joystick (e.g., PlayStation 5 controller) via USB-C for manual control.

4. **Autonomous Mode:**
   - If no joystick is detected, the script executes autonomous movements.

## Tested Configuration

- [**Drone:** DJI Tello](https://www.amazon.com/DJI-Tello-Boost-Combo-Drone/dp/B0BTJ773C1)
<p align="center">
  <img src="https://github.com/dougsland/autonomous_drones/blob/main/pics/01.jpg" alt="Autonomous Drone Image 1" width="50%">
</p>

- [**Controller:** PlayStation 5 controller connected via USB-C](https://www.amazon.com/PlayStation-DualSense-Wireless-Controller/dp/B0CPXXWZGW/ref=sr_1_4?crid=V5QLJV24Y2UH&dib=eyJ2IjoiMSJ9.a_ghpjg03vvpon7A_D6F3Aeppp1-Cj82LIi8p57n29xZQkjts76dRPiyJjwcXro9ZDG_tZvJJo_FVW072LiJz7rVxY_YwwuVTDd4VO6oeDwXCAOwge1KuECYPraOBkOvw5Fam3UR6e7684z-C20bfXAyQ-x_t9K_NEIbMKFY1LyXjQHddreenPitO03pK59ZzC2-hS74KL9J1CrX_DLTxOhjKhxeYAsLhqgj-oOYSxA.EeHMzUYEEWj_1VEEAT_jmIvcReExAsDtIVHX6eawPiU&dib_tag=se&keywords=playstation+5+controller&qid=1735403675&sprefix=playstation+5+controlle%2Caps%2C150&sr=8-4)
<p align="center">
  <img src="https://github.com/dougsland/autonomous_drones/blob/main/pics/02.jpg" alt="Autonomous Drone Image 1" width="50%">
</p>


- **Operating System:** Linux-based system with `nmcli` for Wi-Fi management

## Extending to Other Drones

To support other drones:
1. Replace the `Tello` class from `djitellopy` with the corresponding library or SDK for the target drone.
2. Update the methods related to drone-specific operations, such as `connect_drone`, `drone_logic`, and `process_joystick_input`.

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome to extend support for additional drones and improve the framework. Please open an issue or submit a pull request.

---
