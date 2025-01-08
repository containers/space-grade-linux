from datetime import date, timedelta
import math

class Moon:
    def __init__(self):
        # Reference date: New Moon on January 6, 2025
        self.reference_date = date(2025, 1, 6)
        self.lunar_cycle_length = 29.53  # Average length of a lunar cycle in days
        self.average_distance = 384400  # Average distance from Earth to Moon in km
        self.orbital_period = 27.32  # Orbital period in days

    def days_since_new_moon(self, target_date=None):
        """Calculate the number of days since the last new moon."""
        if target_date is None:
            target_date = date.today()
        delta_days = (target_date - self.reference_date).days
        return delta_days % self.lunar_cycle_length

    def phase_of_moon(self, target_date=None):
        """Determine the current phase of the moon."""
        days = self.days_since_new_moon(target_date)
        if days < 1.0:
            return "New Moon"
        elif days < 7.4:
            return "Waxing Crescent"
        elif days < 10.9:
            return "First Quarter"
        elif days < 14.8:
            return "Waxing Gibbous"
        elif days < 17.8:
            return "Full Moon"
        elif days < 22.1:
            return "Waning Gibbous"
        elif days < 25.7:
            return "Last Quarter"
        else:
            return "Waning Crescent"

    def next_full_moon(self):
        """Calculate the next full moon date."""
        today = date.today()
        days = self.days_since_new_moon(today)
        days_to_full_moon = (14.8 - days) % self.lunar_cycle_length
        return today + timedelta(days=days_to_full_moon)

    def distance_from_earth(self):
        """Calculate the approximate distance from Earth to the Moon in km."""
        days = self.days_since_new_moon()
        angle = (2 * math.pi * days) / self.orbital_period
        distance = self.average_distance * (1 + 0.0549 * math.cos(angle))  # Eccentricity adjustment
        return distance

    def visibility_percentage(self):
        """Calculate the percentage of the moon's surface illuminated."""
        days = self.days_since_new_moon()
        illumination = 50 * (1 + math.cos(2 * math.pi * days / self.lunar_cycle_length))
        return illumination

    def gravitational_force(self, mass):
        """Calculate the gravitational force between an object and the moon."""
        G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
        moon_mass = 7.342e22  # Mass of the moon in kg
        distance_meters = self.distance_from_earth() * 1000  # Convert km to meters
        force = G * (moon_mass * mass) / (distance_meters ** 2)
        return force

# Example usage
#moon = Moon()
#print(f"How many days have passed since most recent New Moon within the current lunar cycle. : {moon.days_since_new_moon():.2f}.")
#print(f"Current moon phase: {moon.phase_of_moon()}")
#print(f"Next full moon date: {moon.next_full_moon()}")
#print(f"Distance from Earth: {moon.distance_from_earth():,.2f} km")
#print(f"Visibility percentage: {moon.visibility_percentage():.2f}%")
#mass_of_object = 80  # Mass in kg
#print(f"Gravitational force on a {mass_of_object} kg object: {moon.gravitational_force(mass_of_object):.2e} N")
