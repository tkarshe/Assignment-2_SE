import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(data.resources)
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###
    print("Welcome to the Ham Sandwich Maker Machine!")

    sandwich_choice = "ham_sandwich"  
    if sandwich_maker_instance.check_resources(data.recipes[sandwich_choice]):
        print("Resources are sufficient. Proceeding to payment.")
        pay = 5.0  # Assuming the customer pays $5.0
        cost = 3.5  # Assuming cost of the sandwich is $3.5
        if cashier_instance.transaction_result(cost, pay):
            sandwich_maker_instance.make_sandwich(data.recipes[sandwich_choice])
            print("Sandwich made successfully!")
        else:
            print("Payment insufficient.")
    else:
        print("Insufficient resources to make the sandwich.")

if __name__=="__main__":
    main()
