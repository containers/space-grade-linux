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
Module containing Lockheed Martin-specific operations for the RocketLaunch simulation.
"""

def lockheed_martin_payload_deployment(rocket):
    """
    Special operations for Lockheed Martin rocket payload deployment.

    Parameters:
    - rocket (RocketLaunch): Instance of the RocketLaunch class.
    """
    rocket.display_message("Lockheed Martin rocket achieving stable geostationary orbit...", "🛰️")
    rocket.display_message("Verifying orbital precision with advanced navigation systems...", "📡")
    rocket.display_message("Deploying high-value payload with Lockheed precision...", "🎯")
    rocket.display_message("Payload successfully deployed to geostationary orbit!", "🌌")
    rocket.display_message("Performing thorough post-deployment diagnostics...", "✅")


def lockheed_martin_return_and_landing(rocket):
    """
    Special operations for Lockheed Martin rocket's return and landing.

    Parameters:
    - rocket (RocketLaunch): Instance of the RocketLaunch class.
    """
    rocket.display_message("Initiating controlled descent to Earth...", "🛬")
    rocket.display_message("Adjusting thrusters for precision-guided reentry...", "🚀")
    rocket.display_message("Deploying thermal protection systems...", "🔥")
    rocket.display_message("Touchdown! Lockheed Martin rocket has landed safely.", "🏁")
    rocket.display_message("Mission completed with Lockheed Martin engineering excellence.", "🎉")
