"""
Module utilizing Lockheed Martin-specific operations for the RocketLaunch simulation.
"""

from rocket_launcher import RocketLaunch
from rocket_launcher import lockheed_martin

def main():
    """
    Simulate a Lockheed Martin rocket launch with payload deployment and return operations.
    """
    rocket = RocketLaunch("Lockheed Martin Atlas V", "Satellite Payload", "lockheed_martin")

    print("\nStarting Lockheed Martin Rocket Launch Simulation...")
    rocket.simulate_launch()

    print("\nExecuting Lockheed Martin Precision Payload Deployment...")
    lockheed_martin.lockheed_martin_payload_deployment(rocket)

    print("\nExecuting Lockheed Martin Return and Landing...")
    lockheed_martin.lockheed_martin_return_and_landing(rocket)

if __name__ == "__main__":
    main()
