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
Module containing Boeing-specific operations for the RocketLaunch simulation.
"""

def boeing_precision_payload_deployment(rocket):
    """
    Special operations for Boeing rocket launch with a focus on payload deployment.

    Parameters:
    - rocket (RocketLaunch): Instance of the RocketLaunch class.
    """
    rocket.display_message("Boeing rocket performing smooth stage transition...", "🔄")
    rocket.display_message("Ensuring precise orbital alignment...", "🛰️")
    rocket.display_message("Deploying payload with Boeing precision...", "🎯")
    rocket.display_message("Payload successfully deployed to orbit!", "🌌")
    rocket.display_message("Performing post-deployment checks and operations...", "✅")


def boeing_return_and_landing(rocket):
    """
    Special operations for returning the rocket and landing safely.

    Parameters:
    - rocket (RocketLaunch): Instance of the RocketLaunch class.
    """
    rocket.display_message("Preparing for return journey to Earth...", "🌍")
    rocket.display_message("Initiating controlled descent...", "🛬")
    rocket.display_message("Adjusting aerodynamics for smooth reentry...", "☁️")
    rocket.display_message("Deploying landing gear and final adjustments...", "🛠️")
    rocket.display_message("Touchdown! Boeing rocket has landed safely.", "🏁")
    rocket.display_message("Mission complete with Boeing reliability.", "🎉")
