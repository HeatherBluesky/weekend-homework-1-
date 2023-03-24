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
        
    