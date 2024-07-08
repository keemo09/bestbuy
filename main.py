import products
import store
import sys


# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)


def print_product_list(store_instance):
    '''
    Print all the active products.
    '''
    product_list = store_instance.get_all_products()
    print("------")
    counter = 1
    for product in product_list:
        product_data = product.show()
        print(f"{counter}. {product_data}")
        counter += 1
    print("------")
            

def show_total_ammount(store_instance):
    '''
    Print the total number of quantity of the products in store.
    '''
    total_quantity = store_instance.get_total_quantity()
    print(total_quantity)


def make_order(store_instance):
    '''
    Ask the user for product and quantity.
    Print the total price of order and refresh the quantity of the store.
    '''
    print_product_list(store_instance)  # Print the active products.
    shopping = True    
    shopping_cart = []
    while shopping == True: 
        product_choice = input("Which product # do you want?")
        quantity_choice =  input("What amount do you want?")

        # Checks if user input is not empty.
        if product_choice != "" or quantity_choice != "":
            product = store_instance.get_all_products()[int(product_choice)-1]  
            quantity = int(quantity_choice)
            shopping_cart.append((product, quantity))
        else:
            shopping = False
    if shopping_cart != 0:
        total_price = store_instance.order(shopping_cart)
        print(f"Order made! Total payment: ${total_price}")


def quit():
    '''
    Exit the programm.
    '''
    sys.exit()


def call_function(choice, store_instance):
    '''
    Call the function from the dispatcher with the store_instance variable.
    '''
    if choice in dispatcher:
        dispatcher[choice](store_instance)
    else:
        raise ValueError("No mathcing func")



dispatcher = {1: lambda store_instance: print_product_list(store_instance),
              2: lambda store_instance: show_total_ammount(store_instance),
              3: lambda store_instance: make_order(store_instance), 
              4: lambda store_instance: sys.exit() }


def start(store_instance):
    '''
    Starts the Programm and handel the behavior of it.
    '''
    while True:
        try:
            print()
            print("   Store Menu")
            print("   ----------")
            print("1. List all products in store")
            print("2. Show total amount in store")
            print("3. Make an order")
            print("4. Quit")
            user_choice = int(input("Please choose a number: "))
            call_function(user_choice, store_instance)
        except ValueError:
            pass


def main():
    start(best_buy)


if __name__ == "__main__":
    main()