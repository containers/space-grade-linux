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
Module containing NASA-specific operations for the RocketLaunch simulation.
"""

def curiosity_mission_operations(rocket):
    """
    Special operations for NASA's Curiosity rover mission.

    Parameters:
    - rocket (RocketLaunch): Instance of the RocketLaunch class.
    """
    rocket.display_message("Curiosity rover entering Martian atmosphere...", "🪐")
    rocket.display_message("Deploying parachute for descent...", "🪂")
    rocket.display_message("Initiating sky-crane maneuver...", "🛸")
    rocket.display_message("Curiosity rover has landed safely on Mars!", "🪨")
    rocket.display_message("Starting surface operations and data collection.", "🛰️")
