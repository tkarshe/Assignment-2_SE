
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, amount_needed in ingredients.items():
            if ingredient in self.machine_resources:
                if self.machine_resources[ingredient] < amount_needed:
                    print(f"Sorry, there's not enough {ingredient}.")
                    return False
            else:
                print(f"Sorry, {ingredient} is not available.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        if self.check_resources(order_ingredients):
            for ingredient, amount in order_ingredients.items():
                self.machine_resources[ingredient] -= amount
            print(f"{sandwich_size.capitalize()} sandwich made successfully.")
        else:
            print("Could not make the sandwich due to insufficient resources.")