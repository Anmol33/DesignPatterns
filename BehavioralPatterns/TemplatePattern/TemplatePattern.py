class PizzaMaker:
    def make(self):
        self.prepare_dough()
        self.select_toppings()
        self.add_topping()
        self.bake()

    def prepare_dough(self):
        print("Preparing flour dough")

    def select_toppings(self):
        print("carrots and onion")

    def add_topping(self):
        print("sprinkle toppings")

    def bake(self):
        print("bake in simple oven")


class ChickenPizzaMaker(PizzaMaker):
    def select_toppings(self):
        print("chicken and onion")


class PanPizzaMaker(PizzaMaker):
    def bake(self):
        print("bake in pan pizza oven")

