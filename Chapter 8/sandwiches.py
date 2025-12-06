def sandwich_items(*sandwich):
    print("Items in your sandwich:")
    for item in sandwich:
        print(f"- {item}")
    
sandwich_items('salami', 'pepperoni', 'cheese')
sandwich_items('salami', 'cheese')
sandwich_items('salami')

def user_profile(first, last, **user_info):
    profile = {
        'first': first,
        'last': last
    }
    for k, v in user_info.items():
        profile[k] = v

    return profile

information = user_profile('yixiao', 'hu', school = 'burgmann', age = '16')
print(information)
information = user_profile('yixiao', 'hu')
print(information)

def make_car(manufactuer, model, **car_info):
    vehicle = {
        'manufactuer': manufactuer,
        'model': model,
    }
    for k, v in car_info.items():
        vehicle[k] = v
    
    return vehicle

car = make_car('subaru', 'outback', color = 'blue', tow_package = 'True')
print(car)