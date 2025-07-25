class Character:
    def __init__(self, name, power_level):
        self.name = name
        self._power_level = power_level  

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Power Level: {self._power_level}")

class Superhero(Character):
    def __init__(self, name, power_level, superpower):
        super().__init__(name, power_level)  
        self.superpower = superpower

    def use_power(self):
        print(f"{self.name} uses {self.superpower}!")

    def power_up(self, amount):
        self._power_level += amount
        print(f"{self.name} powered up to {self._power_level}!")


hero = Superhero("Photon Girl", 80, "Light Beam")
hero.display_info()
hero.use_power()
hero.power_up(20)
