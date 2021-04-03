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
    

# task 8 return the number of a specific breed

def get_pets_by_breed(pet_shop, breed):
    
    if breed in pet_shop == breed:
        return len(petshop["pets"][0]["breed"] and petshop["pets"][1]["breed"])


   
    
#     breed_list = []
    
#     for breeds in pet_shop:
#         if breeds == breed:
#             breed_list.append(breed)
        
#         return "found"

# print(get_pets_by_breed(pet_shop, "British Shorthair"))






    

