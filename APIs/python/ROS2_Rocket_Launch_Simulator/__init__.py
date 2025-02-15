#!/usr/bin/env python3
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

"""
Common module for RocketLaunch simulation.
Provides the base RocketLaunch class and common operations.
"""

import time
import rclpy
from rclpy.node import Node as BaseNode
from std_msgs.msg import String


class RocketLaunch(BaseNode):
    """
    Class representing a rocket launch simulation with common functionality.

    Attributes:
    - rocket_name (str): Name of the rocket.
    - payload (str): Description of the payload.
    - mission_type (str): Type of mission (e.g., 'curiosity', 'spacex', or 'standard').
    - current_stage (str): Current stage of the rocket launch.
    - stages (list): List of stages in the launch sequence.
    - stage_index (int): Index of the current stage in the stages list.
    - completed_stages (list): List of completed stages.

    Methods:
    - initialize_stages: Initialize launch stages based on the mission type.
    - delay: Introduce a delay for a given number of seconds.
    - display_message: Display a message with an accompanying emoji.
    - handler: Handle messages received on the 'rocket_launch' ROS2 topic.
    - advance_stage: Advance to the next stage in the launch sequence.
    - reset_launch: Reset the launch sequence.
    - simulate_launch: Simulate the entire launch sequence.
    """

    def __init__(self, rocket_name, payload, mission_type="standard"):
        """
        Initialize a RocketLaunch instance and a ROS2 Node.

        Parameters:
        - rocket_name (str): Name of the rocket.
        - payload (str): Description of the payload.
        - mission_type (str): Type of mission (e.g., 'curiosity', 'spacex', or 'standard').
        """
        super().__init__('rocket_launch_node')
        self.rocket_name = rocket_name
        self.payload = payload
        self.mission_type = mission_type.lower()
        self.current_stage = "Initialization"
        self.stages = self.initialize_stages()
        self.stage_index = 0
        self.completed_stages = []
        self.sub = self.create_subscription(
            String,
            'rocket_launch',
            self.handler,
            10
        )

    def initialize_stages(self):
        """
        Initialize the stages based on the mission type.

        Returns:
        list: List of stages for the launch.
        """
        base_stages = [
            "Pre-Launch Preparations",
            "Ignition and Liftoff",
            "Ascent Stage",
            "Stage Separation",
            "Fairing Separation",
            "Orbital Insertion or Payload Deployment",
            "Stage Reentry and Recovery",
            "Post-Launch Operations"
        ]
        if self.mission_type == "curiosity":
            base_stages.append("Curiosity Mission Operations")
        elif self.mission_type == "spacex":
            base_stages.append("SpaceX Booster Recovery")
        return base_stages

    def delay(self, seconds=2):
        """
        Introduce a delay for a given number of seconds.

        Parameters:
        - seconds (int): Number of seconds to delay.
        """
        time.sleep(seconds)

    def display_message(self, message, emoji):
        """
        Display a message with an accompanying emoji.

        Parameters:
        - message (str): Message to be displayed.
        - emoji (str): Emoji to accompany the message.
        """
        print(f"{emoji} {message}")
        self.delay()

    def handler(self, msg):
        """
        Handle messages received on the 'rocket_launch' topic.

        Parameters:
        - msg (String): Received message.
        """
        self.get_logger().info(f'Received rocket_launch data: {msg.data}')

    def advance_stage(self):
        """
        Advance to the next stage in the rocket launch sequence.
        Calls the method corresponding to the current stage.
        """
        if self.stage_index < len(self.stages):
            stage_method_name = (
                self.stages[self.stage_index]
                .lower()
                .replace(" ", "_")
                .replace("-", "_")
                .replace("/", "_")
            )
            stage_method = getattr(self, stage_method_name, None)
            if stage_method:
                self.current_stage = self.stages[self.stage_index]
                self.completed_stages.append(self.current_stage)
                print(f"\n--- Stage: {self.current_stage} ---")
                stage_method()
                self.stage_index += 1
            else:
                print(f"Error: No method found for stage '{self.stages[self.stage_index]}'")
        else:
            print("🚀 Rocket launch sequence is complete! 🎉")

    def reset_launch(self):
        """
        Reset the launch sequence, allowing it to be restarted.
        """
        self.current_stage = "Initialization"
        self.stage_index = 0
        self.completed_stages = []
        print(f"🔄 Launch sequence for {self.rocket_name} has been reset.")

    def simulate_launch(self):
        """
        Simulate the entire launch sequence.
        Advances through all stages and calls the respective methods for each stage.
        """
        print(f"🚀 Starting launch sequence for {self.rocket_name} with payload: {self.payload} 🚀")
        while self.stage_index < len(self.stages):
            self.advance_stage()
        print("🎉 Launch sequence completed successfully! 🎉")
