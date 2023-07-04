
item_list = ["laptop" , "headset" ,"second monitor" , "mousepad","USB drive", "external drive"]

limit = 5000
price_sheet = {"laptop":1500,             
               "headset": 100,
               "second monitor":200,
               "mousepad":50, 
               "USB drive":70,
               "external drive":250 }

cart =[]     #Initialize the cart list

def add_to_cart(item,quantity):
    cart.append((item,quantity))


for i in range(len(item_list)):
    item = item_list[i]
    quantity = int(input("Enter the quantity for {}: ".format(item)))
    add_to_cart(item, quantity)


def create_invoice():
    
    for item,quantity in cart:
        total_amount_inc_tax=0
        price = price_sheet[item]
        tax = 0.18 * price
        total = (price + tax) * quantity
        total_amount_inc_tax+= total
        print("Item:",item,"\t","quantity:",quantity,"\t","tax:",tax,"\t","total:",total,"\n")
    print("After the taxes are applied the total amount is:","\t",total_amount_inc_tax,"\n")
    return total_amount_inc_tax


def checkout():
    global limit
    total_amount = create_invoice()
    if limit == 0:
        print("You do not have ant budget!")
    elif total_amount > limit:
        print("The amount you have to pay is above the spending limit. Drop some items.")
    else :
        limit -= total_amount
        print(f"You have paid is {total_amount},you have {limit} dolars left.","\n")


checkout()

