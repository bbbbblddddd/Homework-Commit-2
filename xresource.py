
def add_or_remove_cash(pet_shop,cash):
    pet_shop['admin']['total_cash'] += cash
    
























def get_pets_sold(pet_shop):
    return pet_shop['admin']['pets_sold']

def increase_pets_sold(pet_shop,num):
    pet_shop['admin']['pets_sold'] += num

def get_stock_count(pet_shop):
    return len(pet_shop['pets'])
