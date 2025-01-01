# flake8: noqa: E501
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests
import subprocess
import sys


class UGVController:
    """
    This code is all about talking to a robot car (called a UGV, or Unmanned Ground Vehicle).

    It supports basic wheel movement, independent wheel control (if the robot supports it), ROS-based velocity control,
    motor PID configuration, and now movement commands for turning, moving backward, and forward.
    """

    def __init__(self, ssid="UGV", password="12345678", ip="192.168.4.1", interface_name=None):
        """
        Initialize the UGV controller.

        Args:
            ssid (str): The Wi-Fi SSID (default: 'UGV').
            password (str): The Wi-Fi password (default: '12345678').
            ip (str): The rover's IP address (default: '192.168.4.1').
            interface_name (str): Optional wireless interface name (e.g., 'wlan0').
        """
        self.ssid = ssid
        self.password = password
        self.ip = ip
        self.interface_name = interface_name or "wlp9s0"

    def connect_to_wifi(self):
        """
        Connect to the Wi-Fi network using nmcli.

        Raises:
            SystemExit: If the Wi-Fi connection fails or nmcli is not installed.
        """
        print(f"Connecting to Wi-Fi network '{self.ssid}' using interface '{self.interface_name}'...")
        try:
            command = [
                "nmcli", "connection", "add", "type", "wifi", "ifname", self.interface_name,
                "con-name", "UGVConnection", "ssid", self.ssid,
                "wifi-sec.key-mgmt", "wpa-psk", "wifi-sec.psk", self.password
            ]
            subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

            activate_command = ["nmcli", "connection", "up", "UGVConnection"]
            result = subprocess.run(activate_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            if result.returncode == 0:
                print(f"Successfully connected to Wi-Fi network '{self.ssid}'.")
            else:
                print(f"Failed to activate Wi-Fi connection: {result.stderr.strip()}")
                sys.exit(1)

        except subprocess.CalledProcessError as e:
            print(f"Error creating or activating Wi-Fi connection: {e.stderr.strip()}")
            sys.exit(1)
        except FileNotFoundError:
            print("Error: nmcli is not installed. Please install NetworkManager CLI tools.")
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)

    def move_forward_6wheels(self, left_front=0.5, left_middle=0.5, left_rear=0.5, 
                         right_front=0.5, right_middle=0.5, right_rear=0.5):
        """
        ** Not sure if supported by vendor, need to be tested **

        Move all six wheels forward with individually specified speeds using T: 13.

        Args:
            left_front (float): Speed for the front left wheel (-1.0 to 1.0).
            left_middle (float): Speed for the middle left wheel (-1.0 to 1.0).
            left_rear (float): Speed for the rear left wheel (-1.0 to 1.0).
            right_front (float): Speed for the front right wheel (-1.0 to 1.0).
            right_middle (float): Speed for the middle right wheel (-1.0 to 1.0).
            right_rear (float): Speed for the rear right wheel (-1.0 to 1.0).

        Returns:
            str: Response from the rover.

        "T": 2: Configure the motor's PID parameters (Looks like it's not supported by the hardware)
    """
        json_data = {
            "T": 2,
            "LF": left_front,
            "LM": left_middle,
            "LR": left_rear,
            "RF": right_front,
            "RM": right_middle,
            "RR": right_rear
        }
        return self.send_json_command(json_data)

    def send_json_command(self, json_data):
        """
        Send a JSON command to the rover.

        Args:
            json_data (dict): The JSON command to send.

        Returns:
            str: The response text from the rover.

        Raises:
            RequestException: If there is a communication error with the rover.
        """
        try:
            url = f"http://{self.ip}/js?json={json_data}"
            response = requests.get(url)
            print(f"Response: {response.text}")
            return response.text
        except requests.RequestException as e:
            print(f"Error communicating with the rover: {e}")
            return None

    def move(self, left_speed, right_speed):
        """
        Control left and right wheels together.

        Args:
            left_speed (float): Speed for the left wheels (-1.0 to 1.0).
            right_speed (float): Speed for the right wheels (-1.0 to 1.0).

        Returns:
            str: Response from the rover.

        "T": 1: Control left and right wheels. (at the same time)
        """
        json_data = {"T": 1, "L": left_speed, "R": right_speed}
        return self.send_json_command(json_data)

    def move_individual_wheels(self, left_front, left_rear, right_front, right_rear):
        """
        Control each wheel independently.

        Args:
            left_front (float): Speed for the front left wheel (-1.0 to 1.0).
            left_rear (float): Speed for the rear left wheel (-1.0 to 1.0).
            right_front (float): Speed for the front right wheel (-1.0 to 1.0).
            right_rear (float): Speed for the rear right wheel (-1.0 to 1.0).

        Returns:
            str: Response from the rover.

        "T": 2: Configure the motor's PID parameters (Looks like it's not supported by the hardware)
        """
        json_data = {
            "T": 2, "LF": left_front, "LR": left_rear, "RF": right_front, "RR": right_rear
        }
        return self.send_json_command(json_data)

    def move_right(self, speed=0.5):
        """
        Turn the robot to the right by slowing down the right wheels.

        Args:
            speed (float): The speed for the left wheels (-1.0 to 1.0).
                           Default is 0.5 for smooth turning.

        Returns:
            str: Response from the rover.
        """
        print("Turning right...")
        return self.move(left_speed=speed, right_speed=speed * 0.5)

    def move_left(self, speed=0.5):
        """
        Turn the robot to the left by slowing down the left wheels.

        Args:
            speed (float): The speed for the right wheels (-1.0 to 1.0).
                           Default is 0.5 for smooth turning.

        Returns:
            str: Response from the rover.
        """
        print("Turning left...")
        return self.move(left_speed=speed * 0.5, right_speed=speed)

    def move_backwards(self, speed=0.5):
        """
        Move the robot backwards by setting negative speeds for both wheels.

        Args:
            speed (float): The speed for both wheels (0.0 to 1.0).
                           Default is 0.5 for smooth reverse movement.

        Returns:
            str: Response from the rover.
        """
        print("Moving backwards...")
        return self.move(left_speed=-speed, right_speed=-speed)

    def cmd_ros_control(self, linear_velocity, angular_velocity):
        """
        Control the robot using ROS-style velocity commands.

        Args:
            linear_velocity (float): The moving linear velocity in m/s (meters per second).
            angular_velocity (float): The steering angular velocity in rad/s (radians per second).


            Keep in mind: 
               - Linear velocity: How fast the robot should move forward or backward.
                  - Positive Values: Move forward.
                  - Negative Values: Move backward.

                  Example(s):
                    - linear_velocity = 0.5: The robot moves forward at 0.5 m/s.
                    - linear_velocity = -0.3: The robot moves backward at 0.3 m/s.

               - Angular velocity: How fast the robot should turn (rotate) left or right.
                  - angular_velocity is mesasured by radians per second (rad/s). (A full circle is 2π radians or about 6.28 radians.)
                  - Positive Values: Turn right (clockwise).
                  - Negative Values: Turn left (counter-clockwise).

                  Example(s):
                    - angular_velocity = 0.2: The robot slowly turns to the right.
                    - angular_velocity = -0.5: The robot turns to the left more sharply.

        Returns:
            str: Response from the rover.

        "T": 13: ROS-style control for linear and angular velocities.
        """
        json_data = {"T": 13, "X": linear_velocity, "Z": angular_velocity}
        return self.send_json_command(json_data)

    def set_motor_pid(self, p_coefficient, i_coefficient, d_coefficient, windup_limit=255):
        """
        Configure the motor PID values.

        What is PID Control?
        PID control is like having a robot "driver" that continuously checks if the motor is doing
        what it’s supposed to and makes corrections to keep it on track.

        For example:

        You want the motor to spin at 50 RPM, but due to friction or other factors, it’s spinning at 45 RPM.
        A PID controller adjusts the motor's power to get it back to 50 RPM.


        Args:
            p_coefficient (int): Proportional coefficient.
            i_coefficient (int): Integral coefficient.
            d_coefficient (int): Differential coefficient.
            windup_limit (int): Windup limit for the PID controller (default: 255).

        p_coefficient (Proportional coefficient):
            This controls how strongly the system reacts to the current error.
                If the motor is 10 RPM too slow, the proportional term says, "Let me add more power to fix it right now."
                The larger the p_coefficient, the stronger the reaction. But if it’s too large, the system might 
                overreact and cause instability (e.g., oscillating speeds).

        i_coefficient (Integral coefficient):
            This looks at the history of the error over time and tries to fix any lingering issues.
            For example, if the motor has been consistently 2 RPM too slow, the integral term will keep track of this
            "cumulative error" and gradually adjust the power to eliminate it.
            The larger the i_coefficient, the more strongly the controller tries to correct long-term errors.
            However, if it’s too large, it may cause the system to overcompensate, leading to instability.

        d_coefficient (Derivative coefficient):
            This predicts how the error is changing and adjusts to prevent overshooting or instability.
            For example, if the motor is speeding up too fast and might overshoot the target RPM, the derivative
            term will slow it down slightly. The larger the d_coefficient, the more cautious the controller is
            about rapid changes. If it’s too large, the system may become too sluggish and fail to respond quickly to changes.

        windup_limit (Windup limit for the PID controller):
            The windup limit prevents the integral term from accumulating too much error over time.
            Why is this important? If the motor is stuck and can’t move for some reason, the integral term might keep "remembering"
            the large error and increase the power endlessly. This is called integral windup, and it can make the system unstable.
            The windup_limit sets a cap on how much correction the integral term can apply, ensuring the system stays stable.

            Default Value:
                The default value is 255, meaning the maximum allowed correction is limited to 255.

        Returns:
            str: Response from the rover.

        "T": 2: Configure the motor's PID parameters.
        """
        json_data = {
            "T": 2, "P": p_coefficient, "I": i_coefficient,
            "D": d_coefficient, "L": windup_limit
        }
        return self.send_json_command(json_data)
