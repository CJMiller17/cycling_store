import os
import django
from django.conf import settings

# Use this by running:
# python standalone_script.py
os.environ["DJANGO_SETTINGS_MODULE"] = "cycling_store.settings"
django.setup()

print('SCRIPT START ************* SUCCESS ************')
# Now you have django, so you can import models and do stuff as normal
### NOTE
# DO NOT CHANGE CODE ABOVE THIS LINE
# WORK BELOW
from inventory_system.models import *



# CREATE
'''
customer_A = Customer(name = "Jack Frost")
customer_A.save()

customer_B = Customer.objects.create(name= "Father Winter")
'''

# READ
'''
customer = Customer.objects.all()
for christmas in customer:
    print(christmas)

customer = Customer.objects.get(name = "Jack Frost")
print(customer)

customer = Customer.objects.filter(name__in = ["Jack Frost"])
for christmas in customer:
    print(christmas)
'''
    
# UPDATE
'''
customer = Customer.objects.get(name = "Father Winter")
customer.name = "Grandpa Winter"
customer.save()

print(customer.name)
'''

# DELETE
'''
customer = Customer.objects.all()
Customer.objects.get(name = "Jack Frost").delete()
for christmas in customer:
    print(christmas)
'''

print(f"Ugh... What do you want? \n \n [1] Customers \n [2] Orders \n [3] Inventory \n")

def handle_customers():
        # CREATE CUSTOMER

        def create_customer():
            print("Enter First Name")
            new_first_name = input("")
            print("Enter Last Name")
            new_last_name = input("")
            new_customer = Customer(last_name = new_last_name, first_name = new_first_name)
            new_customer.save()


        # UPDATE CUSTOMER

        def update_customer():
            print("Which Customer would you like to Update?")
            print("Last Name: ")
            current_last_name = input("")
            print("First Name: ")
            current_first_name = input("")
            print("What is the New Last Name?")
            updated_last_name = input("")
            print("What is the New First Name?")
            updated_first_name = input("")

            updated_customer = Customer.objects.filter(last_name = current_last_name, first_name = current_first_name).first()
            if update_customer:
                updated_customer.last_name = updated_last_name
                updated_customer.first_name = updated_first_name
                updated_customer.save()
                print("Customer Updated Successfully")
            else:
                print("Customer Could Not Be Found")
            

        # DELETE CUSTOMER

        def delete_customer():
            print("Which Customer would you like to DELETE?")
            print("Last Name: ")
            delete_last_name = input("")
            print("First Name: ")
            delete_first_name = input("")
            
            # Try and handle multiple through if else statements
            Customer.objects.filter(last_name = delete_last_name , first_name = delete_first_name).first().delete()


        # LOOK UP ALL CUSTOMERS

        def lookup_customers():
            all_customers = Customer.objects.all()
            print(f"Customer List: \n" )
            for person in all_customers:
                print(f"{person.last_name}, {person.first_name}")



def handle_inventory():
        # ADD TO INVENTORY

        def create_transport():
            print("Enter New Item Name")
            new_item_name = input("")
            print("Enter New Item Qty")
            new_item_qty = input("")
            new_item = Transport(item = new_item_name, in_stock = new_item_qty)
            new_item.save()


        # DISPLAY ALL INVENTORY

        def lookup_transport():
                    all_items = Transport.objects.all()
                    print(f"Transport List: \n" )
                    for item in all_items:
                        print(item)


        # EDIT CURRENT INVENTORY (NEW COLUMNS)

        def update_transport():
                    print("Which Item would you like to Update?")
                    print("Item Name: ")
                    current_item_name = input("")
                    print("New Quantity: ")
                    new_item_qty = int(input(""))

                    updated_item = Transport.objects.filter(item = current_item_name).first()
                    if updated_item:
                        updated_item.in_stock = new_item_qty
                        updated_item.save()
                        print("Item Updated Successfully")
                    else:
                        print("Item Could Not Be Found")


        # DELETE TRANSPORT TYPE

        def delete_transport():
                    print("Which Item would you like to DELETE?")
                    print("Item Name: ")
                    delete_item_name = input("")
                    
                    # Try and handle multiple through if else statements
                    Transport.objects.filter(item = delete_item_name).first().delete()


# def handle_orders():
# PLACE ORDER

def create_order():
            print("Enter First Name")
            new_first_name = input("")
            print("Enter Last Name")
            new_last_name = input("")
            new_customer = Order(last_name = new_last_name, first_name = new_first_name)
            new_customer.save()

# EDIT ORDER


# DELETE ORDER


# LOOK UP ALL ORDERS
