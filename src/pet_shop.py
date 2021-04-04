# WRITE YOUR FUNCTIONS HERE

# function to get pet shop name. task 1

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

name = get_pet_shop_name

print(name)

# get total cash in pet_shop task 2 & 3

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


# add or remove cash tasks 3 & 4

def add_or_remove_cash(pet_shop, money):
    pet_shop["admin"]["total_cash"] += money

# task 5  return number of sold pets

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# task 6 increase the number of sold pets

def  increase_pets_sold(pet_shop, add_number ):
     pet_shop["admin"]["pets_sold"] = add_number


# count (LEN) the number of pets for a stock count
def get_stock_count(pet_shop):
    
    return len(pet_shop["pets"])
    

# task 8 return the number of a specific breed.
# task 9 return none if breed doesn't exits

def get_pets_by_breed(pet_shop, breed):

    dog_breed= []

    for dogs in pet_shop["pets"]:
        if dogs["breed"] == breed:
            dog_breed.append(breed)
    
    return dog_breed



 # task 10 return pet by name.

def find_pet_by_name(pet_shop, pet_name):
    
    for pet in pet_shop["pets"]:
         if pet["name"] == pet_name:
             return pet

# task 11 remove pet by name.

def remove_pet_by_name(pet_shop, pet_name): 
    
    for pet in pet_shop["pets"]:
         if pet["name"] == pet_name:
             pet_shop["pets"].remove(pet)

#task 12 add pet by name

def add_pet_to_stock(pet_shop, pet_to_add):
    
    pet_shop["pets"].append(pet_to_add)


#task 13 get customer cash


def get_customer_cash(customer_pets):

    return customer_pets["cash"]

# task 14 remove customer cash:

def remove_customer_cash(customers, cash_remove):

    customers["cash"] -= cash_remove

    return customers["cash"]

# task get count of pets for a customer

def get_customer_pet_count (customer_pets):

    return len(customer_pets["pets"])

#task 16 add a pet to a customer.

def add_pet_to_customer(customer_pets, add_pet):

    customer_pets["pets"].append(add_pet)


    



       
        
        








    

