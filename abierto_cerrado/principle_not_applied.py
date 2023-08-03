
class HamburgerCocaCola:
    def __init__(self, hamburger_type):
        self.hamburger_type = hamburger_type

    def get_description(self):
        return f"{self.hamburger_type} en combo con CocaCola y Papas a la Francesa"

class HamburgerQuatro:
    def __init__(self, hamburger_type):
        self.hamburger_type = hamburger_type

    def get_description(self):
        return f"{self.hamburger_type} en combo con Quatro y Anillos de cebolla"

class HamburgerLemonate:
    def __init__(self, hamburger_type):
        self.hamburger_type = hamburger_type

    def get_description(self):
        return f"{self.hamburger_type} en combo con Limonada"

def make_menu_without_principle_applied():
    hamburger_combo_coca_cola = HamburgerCocaCola(
        hamburger_type="Hamburguesa Clásica"
    )

    hamburger_combo_quatro = HamburgerQuatro(
        hamburger_type="Hamburguesa Clásica"
    )

    hamburger_combo_limonada = HamburgerLemonate(
        hamburger_type="Hamburguesa Clásica"
    )

    print("Menú")
    print("1. HamburgerComboCocaCola:")
    print("Consta de:", hamburger_combo_coca_cola.hamburger_type)

    print("2. HamburgerComboQuatro:")
    print("Consta de:", hamburger_combo_quatro.hamburger_type)

    print("3. HamburgerComboLimonada:")
    print("Consta de:", hamburger_combo_limonada.hamburger_type)


if __name__ == "__main__":
    make_menu_without_principle_applied()
