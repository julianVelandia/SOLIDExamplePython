class Swim:
    def swim(self) -> str:
        pass


class SwimmingAnimal(Swim):
    def swim(self) -> str:
        return "El animal está nadando"


class RealDuck:
    def __init__(self, move_through_the_water: Swim):
        self.move_through_the_water = move_through_the_water


def wire():
    swimming_animal = SwimmingAnimal()
    duck = RealDuck(swimming_animal)

    print(duck.move_through_the_water.swim())


if __name__ == "__main__":
    wire()
