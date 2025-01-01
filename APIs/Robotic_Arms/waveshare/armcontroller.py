# Licensed under the Apache License, Version 2.0 (the \"License\");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an \"AS IS\" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests
import math

class RoArmM2S:
    def __init__(self, ip_address):
        self.base_url = f"http://{ip_address}/js?json="

    def send_command(self, command_json):
        url = self.base_url + command_json
        response = requests.get(url)
        return response.text

    # WiFi Settings
    def cmd_wifi_on_boot(self):
        return self.send_command('{"T":401,"cmd":3}')

    def cmd_set_ap(self, ssid, password):
        return self.send_command(f'{{"T":402,"ssid":"{ssid}","password":"{password}"}}')

    def cmd_set_sta(self, ssid, password):
        return self.send_command(f'{{"T":403,"ssid":"{ssid}","password":"{password}"}}')

    def cmd_wifi_apsta(self, ap_ssid, ap_password, sta_ssid, sta_password):
        return self.send_command(f'{{"T":404,"ap_ssid":"{ap_ssid}","ap_password":"{ap_password}","sta_ssid":"{sta_ssid}","sta_password":"{sta_password}"}}')

    def cmd_wifi_info(self):
        return self.send_command('{"T":405}')

    def cmd_wifi_config_create_by_status(self):
        return self.send_command('{"T":406}')

    def cmd_wifi_config_create_by_input(self, mode, ap_ssid, ap_password, sta_ssid, sta_password):
        return self.send_command(f'{{"T":407,"mode":{mode},"ap_ssid":"{ap_ssid}","ap_password":"{ap_password}","sta_ssid":"{sta_ssid}","sta_password":"{sta_password}"}}')

    # ESP-NOW Settings
    def cmd_broadcast_follower(self, mode, mac):
        return self.send_command(f'{{"T":300,"mode":{mode},"mac":"{mac}"}}')

    def cmd_esp_now_config(self, mode, dev, cmd, megs):
        return self.send_command(f'{{"T":301,"mode":{mode},"dev":{dev},"cmd":{cmd},"megs":{megs}}}')

    def cmd_get_mac_address(self):
        return self.send_command('{"T":302}')

    def cmd_esp_now_add_follower(self, mac):
        return self.send_command(f'{{"T":303,"mac":"{mac}"}}')

    def cmd_esp_now_remove_follower(self, mac):
        return self.send_command(f'{{"T":304,"mac":"{mac}"}}')

    def cmd_esp_now_many_ctrl(self, dev, b, s, e, h, cmd, megs):
        return self.send_command(f'{{"T":305,"dev":{dev},"b":{b},"s":{s},"e":{e},"h":{h},"cmd":{cmd},"megs":"{megs}"}}')

    def cmd_esp_now_single(self, mac, dev, b, s, e, h, cmd, megs):
        return self.send_command(f'{{"T":306,"mac":"{mac}","dev":{dev},"b":{b},"s":{s},"e":{e},"h":{h},"cmd":{cmd},"megs":"{megs}"}}')

    # Torque Control
    def cmd_torque_ctrl(self, cmd):
        return self.send_command(f'{{"T":210,"cmd":{cmd}}}')

    # Dynamic Adaptation
    def cmd_set_new_x(self, mode, b, s, e, h):
        return self.send_command(f'{{"T":112,"mode":{mode},"b":{b},"s":{s},"e":{e},"h":{h}}}')

    # Moving Control
    def cmd_move_init(self):
        return self.send_command('{"T":100}')

    def cmd_single_joint_ctrl(self, joint, rad, spd, acc):
        return self.send_command(f'{{"T":101,"joint":{joint},"rad":{rad},"spd":{spd},"acc":{acc}}}')

    def cmd_joints_rad_ctrl(self, base, shoulder, elbow, hand, spd, acc):
        return self.send_command(f'{{"T":102,"base":{base},"shoulder":{shoulder},"elbow":{elbow},"hand":{hand},"spd":{spd},"acc":{acc}}}')

    def cmd_xyzt_goal_ctrl(self, x, y, z, t, spd):
        return self.send_command(f'{{"T":104,"x":{x},"y":{y},"z":{z},"t":{t},"spd":{spd}}}')

    def cmd_xyzt_direct_ctrl(self, x, y, z, t):
        return self.send_command(f'{{"T":1041,"x":{x},"y":{y},"z":{z},"t":{t}}}')

    def cmd_servo_rad_feedback(self):
        return self.send_command('{"T":105}')

    def cmd_eoat_hand_ctrl(self, cmd, spd, acc):
        return self.send_command(f'{{"T":106,"cmd":{cmd},"spd":{spd},"acc":{acc}}}')

    def cmd_single_joint_angle(self, joint, angle, spd, acc):
        return self.send_command(f'{{"T":121,"joint":{joint},"angle":{angle},"spd":{spd},"acc":{acc}}}')

    def cmd_joints_angle_ctrl(self, b, s, e, h, spd, acc):
        return self.send_command(f'{{"T":122,"b":{b},"s":{s},"e":{e},"h":{h},"spd":{spd},"acc":{acc}}}')

    def cmd_constant_ctrl(self, m, axis, cmd, spd):
        return self.send_command(f'{{"T":123,"m":{m},"axis":{axis},"cmd":{cmd},"spd":{spd}}}')

    def cmd_delay_millis(self, cmd):
        return self.send_command(f'{{"T":111,"cmd":{cmd}}}')

    # EOAT Control
    def cmd_eoat_type(self, mode):
        return self.send_command(f'{{"T":1,"mode":{mode}}}')

    def cmd_config_eoat(self, pos, ea, eb):
        return self.send_command(f'{{"T":2,"pos":{pos},"ea":{ea},"eb":{eb}}}')

    def cmd_eoat_grab_torque(self, tor):
        return self.send_command(f'{{"T":107,"tor":{tor}}}')

    # Joints PID Control
    def cmd_set_joint_pid(self, joint, p, i):
        return self.send_command(f'{{"T":108,"joint":{joint},"p":{p},"i":{i}}}')

    def cmd_reset_pid(self):
        return self.send_command('{"T":109}')

    # Mission & Steps Edit
    def cmd_create_mission(self, name, intro):
        return self.send_command(f'{{"T":220,"name":"{name}","intro":"{intro}"}}')

    def cmd_mission_content(self, name):
        return self.send_command(f'{{"T":221,"name":"{name}"}}')

    def cmd_append_step_json(self, name, step):
        return self.send_command(f'{{"T":222,"name":"{name}","step":"{step}"}}')

    def cmd_replace_step_json(self, name, step_num, step):
        return self.send_command(f'{{"T":228,"name":"{name}","stepNum":{step_num},"step":"{step}"}}')

    # File System Control
    def cmd_scan_files(self):
        return self.send_command('{"T":200}')

    def cmd_create_file(self, name, content):
        return self.send_command(f'{{"T":201,"name":"{name}","content":"{content}"}}')

    def cmd_read_file(self, name):
        return self.send_command(f'{{"T":202,"name":"{name}"}}')

    def cmd_delete_file(self, name):
        return self.send_command(f'{{"T":203,"name":"{name}"}}')

    def cmd_append_line(self, name, content):
        return self.send_command(f'{{"T":204,"name":"{name}","content":"{content}"}}')

    # Switch Control
    def cmd_switch_ctrl(self, pwm_a, pwm_b):
        return self.send_command(f'{{"T":113,"pwm_a":{pwm_a},"pwm_b":{pwm_b}}}')

    def cmd_light_ctrl(self, led):
        return self.send_command(f'{{"T":114,"led":{led}}}')

    def cmd_switch_off(self):
        return self.send_command('{"T":115}')

    # ESP32 Settings
    def cmd_reboot(self):
        return self.send_command('{"T":600}')

    def cmd_free_flash_space(self):
        return self.send_command('{"T":601}')

    def cmd_boot_mission_info(self):
        return self.send_command('{"T":602}')

    def cmd_reset_boot_mission(self):
        return self.send_command('{"T":603}')

    def cmd_nvs_clear(self):
        return self.send_command('{"T":604}')

    def cmd_info_print(self, cmd):
        return self.send_command(f'{{"T":605,"cmd":{cmd}}}')

    def do_some_crazy_move(self, radius=None, speed=0.5, acceleration=0.5):
        """
        Moves the arm in a crazy move if not used the correct args
    
        Args:
            radius (float, optional): The radius of the circle in meters or units. 
                                      Defaults to current position if not provided.
            speed (float, optional): The speed of the motion. Defaults to 0.5.
            acceleration (float, optional): The acceleration for the motion. Defaults to 0.5.
        """

        # Fetch current position if radius is not provided
        if radius is None:
            # Assuming self.cmd_servo_rad_feedback() fetches current position in [x, y, z, t]
            current_position = self.cmd_servo_rad_feedback()  
            if isinstance(current_position, str):  # If response is a string, parse it
                current_position = eval(current_position)  # Replace eval with a proper parser in production
            radius = current_position.get('radius', 1)  # Default to 1 if radius isn't provided

        # Break the circle into segments
        segments = 36  # Adjust for smoother or coarser movement
        angle_increment = 2 * math.pi / segments

        for i in range(segments + 1):  # +1 to complete the circle
            angle = i * angle_increment
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            z = 0  # Assuming z stays constant
            t = angle  # Assuming t aligns with the angle of rotation
            self.cmd_xyzt_goal_ctrl(x, y, z, t, speed)

    def open_jaw(self, open_cmd=1.0, speed=0.5, acceleration=0.5):
        """
        Opens the jaw.

        Args:
            open_cmd (float, optional): Command value to open the jaw. Defaults to 1.0.
            speed (float, optional): Speed of the jaw movement. Defaults to 0.5.
            acceleration (float, optional): Acceleration of the jaw movement. Defaults to 0.5.
        """
        self.cmd_eoat_hand_ctrl(open_cmd, speed, acceleration)
        print(f"Jaw opened with command: {open_cmd}")

    def close_jaw(self, close_cmd=0.0, speed=0.5, acceleration=0.5):
        """
        Closes the jaw.

        Args:
            close_cmd (float, optional): Command value to close the jaw. Defaults to 0.0.
            speed (float, optional): Speed of the jaw movement. Defaults to 0.5.
            acceleration (float, optional): Acceleration of the jaw movement. Defaults to 0.5.
        """
        self.cmd_eoat_hand_ctrl(close_cmd, speed, acceleration)
        print(f"Jaw closed with command: {close_cmd}")
