class Animal:
    def __init__(self, x, y, z):
        self.live = True
        self._cords = {"X": x, "Y": y, "Z": z}

    def attack(self):
        print("Be careful, I'm attacking you 0_0")

    def move(self, dx, dy, dz):
        self._cords["X"] += dx
        self._cords["Y"] += dy
        self._cords["Z"] += dz

    def get_cords(self):
        print(f"X: {self._cords['X']} Y: {self._cords['Y']} Z: {self._cords['Z']}")

class Bird(Animal):
    def speak(self):
        print("Tweet-tweet")

class AquaticAnimal(Animal):
    def dive_in(self, dz):
        dz = abs(dz)
        self._cords["Z"] -= dz*2

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    def __init__(self, x, y=20, z=30):
        super().__init__(x, y, z)
        self.beak = True
        self.sound = "Click-click-click"

    def lay_eggs(self):
        num_eggs = 3
        print(f"Here are(is) {num_eggs} eggs for you")

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
