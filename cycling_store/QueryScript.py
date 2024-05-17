import os
import django
from django.conf import settings

# Use this by running: python standalone_script.py
os.environ["DJANGO_SETTINGS_MODULE"] = "cycling_store.settings"
django.setup()

print('SCRIPT START ************* SUCCESS ************') # Now you have django, so you can import models and do stuff as normal

### NOTE
# DO NOT CHANGE CODE ABOVE THIS LINE: # WORK BELOW
from inventory_system.models import *

# GLOBAL VARIABLES THAT GIVE ACCESS TO KEY PARTS OF DATA

all_customers = Customer.objects.all()
all_items = Inventory.objects.all()
all_orders = Order.objects.all()



print("MAIN MENU: \n ")

# CREATE CUSTOMER

def create_customer():
    print("Enter First Name")
    new_first_name = input("").strip().casefold().strip().casefold()
    print("Enter Last Name")
    new_last_name = input("").strip().casefold()
    new_customer = Customer(last_name = new_last_name, first_name = new_first_name)
    new_customer.save()
    print("New Customer Created Successfully!")

# LOOK UP ALL CUSTOMERS

def lookup_customers():
    print(f"Here are all the customers. \n Customer List: \n" )
    for person in all_customers:
        print(f"{person.last_name}, {person.first_name}")

# UPDATE CUSTOMER

def update_customer():
    print("Which Customer Would You Like to Update? \n Last Name: ")
    current_last_name = input("").strip().casefold()
    print("First Name: ")
    current_first_name = input("").strip().casefold()
    print("What is the New Last Name?")
    updated_last_name = input("").strip().casefold()
    print("What is the New First Name?")
    updated_first_name = input("").strip().casefold()

    updated_customer = Customer.objects.filter(last_name = current_last_name, first_name = current_first_name).first()
    if updated_customer:
        updated_customer.last_name = updated_last_name
        updated_customer.first_name = updated_first_name
        updated_customer.save()
        print("Customer Updated Successfully")
    else:
        print("Customer Could Not Be Found")
    

# DELETE CUSTOMER

def delete_customer():
    print("Which Customer Would You Like to DELETE? \n Last Name: ")
    delete_last_name = input("").strip().casefold()
    print("First Name: ")
    delete_first_name = input("").strip().casefold()

    Customer.objects.filter(last_name = delete_last_name , first_name = delete_first_name).first().delete()
    print("DELETED Customer Successfully!")


 # ADD TO INVENTORY

def create_inventory():
    print("Enter New Item Name")
    new_item_name = input("").strip().casefold()
    print("Enter New Item Qty")
    new_item_qty = input("").strip().casefold()
    new_item = Inventory(item = new_item_name, in_stock = new_item_qty)
    new_item.save()
    print("New Item Added To Inventory Successfully!")


# DISPLAY ALL INVENTORY

def lookup_inventory():
            # all_items = Inventory.objects.all()
            print(f"Here is the Entire Inventory. \n Inventory List: \n" )
            for item in all_items:
                print(item)


# EDIT CURRENT INVENTORY (NEW COLUMNS)

def update_inventory():
            print("Which Item would you like to Update? \n Item Name: ")
            current_item_name = input("").strip().casefold()
            print("New Quantity: ")
            new_item_qty = int(input("").strip().casefold())

            updated_item = Inventory.objects.filter(item = current_item_name).first()
            if updated_item:
                updated_item.in_stock = new_item_qty
                updated_item.save()
                print("Item Updated Successfully")
            else:
                print("Item Could Not Be Found")


# DELETE INVENTORY TYPE

def delete_inventory():
            print("Which Item would you like to DELETE? Item Name: ")
            delete_item_name = input("").strip().casefold()
            
            Inventory.objects.filter(item = delete_item_name).first().delete()
            print("Item Has Been Deleted From the Inventory Successfully!")


# PLACE ORDER

def create_order():
            print("Enter Information to Place Order: \n Which Customer is Ordering? \n Last Name: ")
            customer_last_name = input("").strip().casefold()
            print("First Name:")
            customer_first_name = input("").strip().casefold()

            try:
                existing_customer = Customer.objects.get(last_name = customer_last_name, first_name = customer_first_name)
            except Customer.DoesNotExist:
                  print("Could Not Find Customer.")
                  return

            print("What Item Are They Ordering?")
            customer_item = input("").casefold().strip()

            try:
                existing_item = Inventory.objects.get(item = customer_item)
            except Inventory.DoesNotExist:
                print("Could Not Find That Item.")
                return

            print("How Many?")
            customer_qty = int(input("").strip().casefold())

            if existing_item.in_stock >= customer_qty:
                  existing_item.in_stock -= customer_qty
                  existing_item.save()
            else:
                print("There Aren't Enough For This Order")
                return

            print("Are They Paying Now?")
            customer_paid = input("").strip().casefold()

            if customer_paid.casefold() == "yes":
                customer_paid = True
            else:
                customer_paid = False  

            # CONNECTING THE EXISTING ITEM WITH THE ITEM ENTERED BY THE INPUT
            new_order = Order(customer = existing_customer, item = existing_item, qty = customer_qty, paid = customer_paid)
            new_order.save()


# LOOK UP ALL ORDERS

def lookup_orders():
            # all_orders = Order.objects.all()
            print(f"Order List: \n" )
            for order in all_orders:
                print(order)

# EDIT ORDER

def update_order():
        print("Which Way Would You Like to Look Up the Order By? \n [1] Last Name, First Name \n [2] Order Number \n [3] Item Name \n [4] Order Date")
        lookup_method = int(input("").strip().casefold())
        
        if lookup_method == 1:
            print("What is the Last Name? :")
            lookup_last_name = input("").strip().casefold()
            print("What is the First Name? :")
            lookup_first_name = input("").strip().casefold()
            
            try:
                existing_customer = Customer.objects.get(last_name = lookup_last_name, first_name = lookup_first_name)
                orders = Order.objects.filter(customer = existing_customer)
                for order in orders:
                     print(order) # I may have to create a string that contains order.id, .customer, .qty, .item, .paid
                print("Enter the Order Id You Want to Update: ")
                order_id = int(input("").strip().casefold())
                order = orders.get(id = order_id)
            
            except Customer.DoesNotExist:
                print("Customer Could Not Be Found")
                return

            except Order.DoesNotExist:
                print("Order Could Not Be Found")
                return
             

        elif lookup_method == 2:
            print("Enter the Order Number: ")
            order_id = int(input("").strip().casefold())
            try:
                order = Order.objects.get(id = order_id)
            except Order.DoesNotExist:
                 print("Order Could Not Be Found")
                 return

        elif lookup_method == 3:
            print("Enter the Item Name: ")
            item_name = input("").strip().casefold()

            try:
                query_item = Inventory.objects.get(item = item_name)
                orders = Order.objects.filter(item = query_item)
                for order in orders:
                    print(order)
                print("Enter the Order Id You Want to Update: ")
                order_id = int(input("").strip().casefold())
                order = orders.get(id = order_id)
            
            except Inventory.DoesNotExist:
                print("Customer Could Not Be Found")
                return

            except Order.DoesNotExist:
                print("Order Could Not Be Found")
                return

        elif lookup_method == 4:
            print("Enter Order Date in YYYY-MM-DD Format: ")
            order_date = input("").strip().casefold()
            try:
                orders = Order.objects.filter(date = order_date)
                for order in orders:
                    print(order)
                print("Enter the Order Id You Want to Update: ")
                order_id = int(input("").strip().casefold())
                order = orders.get(id = order_id)

            except Order.DoesNotExist:
                print("Order Could Not Be Found")
                return

        else:
            print("Invalid input. Try again.")
            return   

        if order:
            print("Which Aspect of the Order Would You Like to Update? \n [1] Items \n [2] Quantity \n [3] Paid Status")
            specific_aspect = int(input("").strip().casefold())
        
        if specific_aspect == 1:
            print("Which Item Would You Like to Add? :")
            additional_item = input("").strip().casefold()

            try:
                additional_item = Inventory.objects.get(item = additional_item)
                if additional_item.in_stock >= order.qty:
                     order.item = additional_item
                     order.save()
                     print("Item Added Successfully")
                else:
                     print("Not Enough In Stock")
            except Inventory.DoesNotExist:
                 print("Item Not Found")

        elif specific_aspect == 2:
            print("Enter the New Quantity: ")
            new_qty = int(input("").strip().casefold())
            if order.item.in_stock + order.qty >= new_qty:
                 order.item.in_stock += order.qty - new_qty
                 order.qty = new_qty
                 order.item.save()
                 order.save()
                 print("Quantity Updated to Order Successfully")
            else:
                 print("Not Enough Stock For the Updated Quantity")

        elif specific_aspect == 3:
            print("Has the Order Been Paid For?")
            paid_status = input("").strip().casefold() == "yes" # CREATES BOOLEAN VALUE
            order.paid = paid_status
            order.save()
            print("Order Status Has Been Updated Successfully")
             
        else:
            print("Invalid Input.")


# DELETE ORDER

def delete_order():
            print("Which Order Number would you like to DELETE?")
            delete_purchase_order = input("").strip().casefold()
            
            # Try and handle multiple through if else statements
            Order.objects.filter(id = delete_purchase_order).first().delete()


# update_order() # Needs to handle adding items


# delete_inventory()
# delete_order()

# lookup_customers()
# lookup_inventory()
# lookup_orders()