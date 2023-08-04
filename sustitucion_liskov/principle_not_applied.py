class Animal:
    def __init__(self):
        self.looks_like_an_animal = True

    def swim(self):
        return "El animal está nadando"


class Duck(Animal):
    def quack(self):
        return "El pato hace Quack!"

    def swim(self):
        return "El pato está nadando"

    def quack_and_swim(self):
        return f"{self.quack()} {self.swim()}"


class ToyDuck(Animal):
    def quack(self):
        return "El pato hace Quack!"

    def swim(self):
        raise Exception("Un pato de juguete no puede nadar")

    def quack_and_swim(self):
        return "Un pato de juguete no puede nadar, es un comportamiento inesperado"


def make_ducks_without_principle_applied():
    real_duck = Duck()

    print("El pato real parece animal?:", real_duck.looks_like_an_animal)
    print("El pato real está nadando?:", real_duck.swim())
    print("El pato real hace Quack?:", real_duck.quack())
    print("El pato real puede hacer Quack y nadar:", real_duck.quack_and_swim())

    toy_duck = ToyDuck()

    print("El pato de juguete parece animal?:", toy_duck.looks_like_an_animal)
    try:
        # El método nadar en toyDuck me retornaría una excepción en Python
        print("El pato de juguete hace Quack?:", toy_duck.quack())
        print("El pato de juguete puede hacer Quack y nadar:", toy_duck.quack_and_swim())
        print("El pato de juguete puede nadar:", toy_duck.swim())

    except Exception as e:
        print("El pato de juguete No puede nadar:", str(e))


if __name__ == "__main__":
    make_ducks_without_principle_applied()
