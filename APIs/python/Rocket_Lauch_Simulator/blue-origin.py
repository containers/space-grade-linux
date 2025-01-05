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
Module containing Blue Origin-specific operations for the RocketLaunch simulation.
"""

def blue_origin_payload_deployment(rocket):
    """
    Special operations for Blue Origin rocket payload deployment.

    Parameters:
    - rocket (RocketLaunch): Instance of the RocketLaunch class.
    """
    rocket.display_message("Blue Origin rocket achieving stable suborbital trajectory...", "🚀")
    rocket.display_message("Preparing payload for deployment...", "📦")
    rocket.display_message("Deploying payload with precision...", "🎯")
    rocket.display_message("Payload successfully deployed in suborbital space!", "🌌")
    rocket.display_message("Post-deployment system checks in progress...", "🔍")


def blue_origin_return_and_landing(rocket):
    """
    Special operations for Blue Origin rocket's return and safe landing.

    Parameters:
    - rocket (RocketLaunch): Instance of the RocketLaunch class.
    """
    rocket.display_message("Blue Origin rocket beginning return sequence...", "🔄")
    rocket.display_message("Initiating controlled descent with precision thrusters...", "🛬")
    rocket.display_message("Deploying landing gear and stabilizers...", "🛠️")
    rocket.display_message("Performing soft landing at designated site...", "🏞️")
    rocket.display_message("Rocket has landed safely. Ready for reuse.", "♻️")
    rocket.display_message("Blue Origin mission completed successfully!", "🎉")
