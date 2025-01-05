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
Module containing SpaceX-specific operations for the RocketLaunch simulation.
"""

def spacex_booster_recovery(rocket):
    """
    Special operations for SpaceX booster recovery.

    Parameters:
    - rocket (RocketLaunch): Instance of the RocketLaunch class.
    """
    rocket.display_message("SpaceX booster initiating controlled descent...", "🛬")
    rocket.display_message("Adjusting fins for precise landing maneuver...", "🦾")
    rocket.display_message("Firing landing burn...", "🔥")
    rocket.display_message("Touchdown! Booster successfully recovered.", "🪂")
