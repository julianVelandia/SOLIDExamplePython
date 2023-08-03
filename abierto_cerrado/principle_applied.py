class Combo:
    def get_description(self):
        pass


class Hamburger:
    def __init__(self, hamburger_type, combo):
        self.hamburger_type = hamburger_type
        self.combo = combo

    def get_description(self):
        return f"{self.hamburger_type} en combo con {self.combo.get_description()}"


class CocaColaAndFries(Combo):
    def get_description(self):
        return "CocaCola y Papas a la Francesa"


class QuatroAndOnionRings(Combo):
    def get_description(self):
        return "Quatro y Anillos de cebolla"


class Lemonade(Combo):
    def get_description(self):
        return "Limonada"


def make_menu_with_principle_applied():
    hamburger_combo_coca_cola = Hamburger(
        hamburger_type="Hamburguesa Clásica", combo=CocaColaAndFries()
    )

    hamburger_combo_quatro = Hamburger(
        hamburger_type="Hamburguesa Clásica", combo=QuatroAndOnionRings()
    )

    hamburger_combo_limonada = Hamburger(
        hamburger_type="Hamburguesa Clásica", combo=Lemonade()
    )

    print("Menú")
    print("1. HamburgerComboCocaCola:")
    print("Consta de:", hamburger_combo_coca_cola.hamburger_type, "en combo con",
          hamburger_combo_coca_cola.combo.get_description())

    print("2. HamburgerComboQuatro:")
    print("Consta de:", hamburger_combo_quatro.hamburger_type, "en combo con",
          hamburger_combo_quatro.combo.get_description())

    print("3. HamburgerComboLimonada:")
    print("Consta de:", hamburger_combo_limonada.hamburger_type, "en combo con",
          hamburger_combo_limonada.combo.get_description())


if __name__ == "__main__":
    make_menu_with_principle_applied()
