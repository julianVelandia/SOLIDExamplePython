class Animal:
    def looks_like_an_animal(self):
        return True


class Duck(Animal):
    def quack(self):
        return "El pato hace Quack!"


class SwimmingAnimals(Animal):
    def swim(self):
        return "El pato está nadando"


class RealDuck:
    def looks_like_an_animal(self):
        return True

    def swim(self):
        return "El pato está nadando"

    def quack(self):
        return "El pato hace Quack!"

    def quack_and_swim(self):
        return self.quack() + self.swim()


class ToyDuck:
    def __init__(self, have_batteries):
        self.have_batteries = have_batteries

    def looks_like_an_animal(self):
        return True

    def quack(self):
        return "El pato de juguete hace Quack!"


def make_ducks_with_principle_applied():
    real_duck = RealDuck()

    print("El pato real parece animal? :", real_duck.looks_like_an_animal())
    print("El pato real está nadando? :", real_duck.swim())
    print("El pato real hace Quack? :", real_duck.quack())
    print("El pato real hace Quack y nada? :", real_duck.quack_and_swim())

    toy_duck = ToyDuck(True)

    print("El pato de juguete parece animal? :", toy_duck.looks_like_an_animal())
    print("El pato de juguete hace Quack? :", toy_duck.quack())
    print("El pato de juguete tiene baterias? :", toy_duck.have_batteries)


if __name__ == "__main__":
    make_ducks_with_principle_applied()
