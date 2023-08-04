class Animal:
    def __init__(self, looks_like_an_animal):
        self.LooksLikeAnAnimal = looks_like_an_animal


class Duck(Animal):
    def quack(self):
        return "El pato hace Quack!"

    def swim(self):
        return "El pato está nadando"

    def quack_and_swim(self):
        return f"{self.quack()} {self.swim()}"


class ToyDuck(Animal):
    def __init__(self, looks_like_an_animal, have_batteries):
        super().__init__(looks_like_an_animal)
        self.HaveBatteries = have_batteries

    def quack(self):
        return "El pato hace Quack!"


def make_ducks_with_principle_applied():
    real_duck = Duck(looks_like_an_animal=True)

    print("El pato real parece animal? :", real_duck.LooksLikeAnAnimal)
    print("El pato real está nadando? :", real_duck.swim())
    print("El pato real hace Quack? :", real_duck.quack())

    real_duck_can_quack_and_swim = real_duck.quack_and_swim()
    print("El pato real hace Quack y nada? :", real_duck_can_quack_and_swim)

    toy_duck = ToyDuck(looks_like_an_animal=True, have_batteries=True)

    print("El pato de juguete parece animal? :", toy_duck.LooksLikeAnAnimal)
    print("El pato de juguete hace Quack? :", toy_duck.quack())
    print("El pato de juguete tiene baterías? :", toy_duck.HaveBatteries)


if __name__ == "__main__":
    make_ducks_with_principle_applied()
