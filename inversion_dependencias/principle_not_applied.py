class SwimmingAnimal:
    def swim(self):
        return "El animal está nadando"


class RealDuck:
    def __init__(self):
        self.move_through_the_water = SwimmingAnimal()


def bad_wire():
    duck = RealDuck()
    print(duck.move_through_the_water.swim())


if __name__ == "__main__":
    bad_wire()
