# Pricing  -----------------------------------------------------------

pricing = {
    'Samsung': 50000,
    'Mi': 30000,
    'Oppo': 40000
}


def user_input(value):
    input_value = int(input(f"Enter number of {value} phones: "))
    return input_value


samsung_qty = user_input("Samsung")
mi_qty = user_input("Mi")
oppo_qty = user_input("Oppo")
total = samsung_qty * pricing['Samsung'] + mi_qty * pricing['Mi'] + oppo_qty * pricing['Oppo']

if samsung_qty and mi_qty and oppo_qty == 0:
    exit(0)
else:
    print(f"\nYour sum total is : {total}\n")

# Delivery  -----------------------------------------------------------

delivery_type = {
    'Home': 250,
    'Pick-up': 0
}
delivery_price = 0

print(f"Enter your choice of delivery: \n1. Home\n2. Self Pick-Up")
delivery = int(input("Choice: \n"))

if delivery == 1:
    delivery_price += delivery_type['Home']

# Packaging  -----------------------------------------------------------

package_type = {
    'Plastic': 500,
    'Bag': 1000,
    'Gift-Box': 5000
}
package_price = 0

print(f"Enter your choice of package: \n1. Home\n2. Bag\n3. Gift-Box")
package = int(input("Choice: "))

if package == 1:
    package_price += package_type['Plastic']
elif package == 2:
    package_price += package_type['Bag']
elif package == 3:
    package_price += package_type['Gift-Box']
else:
    print("Invalid Choice. Enter numbers between 1 and 3")

# Totaling  -----------------------------------------------------------

grand_total = total + delivery_price + package_price
print(f"\nYour grand total is {grand_total}\n"
      f"Mobiles -> {total}\n"
      f"Delivery -> {delivery_price}\n"
      f"Packaging -> {package_price}")
