# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# def get_total_cash(pet_shop):
#     total_cash = 0
#     for pet in pet_shop["pets"]:
#         total_cash = total_cash + pet["price"]
#     return total_cash

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
   pet_shop["admin"]["total_cash"] = pet_shop["admin"]["total_cash"] + cash   

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, add_pet):
   pet_shop["admin"]["pets_sold"] = pet_shop["admin"]["pets_sold"] + add_pet   

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, description):
    animals = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == description:
             animals.append(pet) 
    return animals
        
def get_pets_by_breed(pet_shop, description):
    animals = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == description:
             animals.append(pet) 
    return animals
        
def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet
        
def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet
        
def remove_pet_by_name(pet_shop, name):
    pet_shop["pets"].remove(find_pet_by_name(pet_shop,name))
            
def add_pet_to_stock(pet_shop, pet):
    pet_shop["pets"].append(pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)



# optional functions 

def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:     # or can use 
        return True
    else:
        return False
    

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet != None and customer_can_afford_pet(customer, pet):
        remove_pet_by_name(pet_shop, pet["name"])
        add_pet_to_customer(customer, pet)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])
        increase_pets_sold(pet_shop, 1)