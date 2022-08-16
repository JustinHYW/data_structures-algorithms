cars = ["ford", "volvo", "bmw"]

for  i in cars:
    print(i)
    
    
shop_name = "fan's coffee"
coffee_sizes = ["small", "medium", "large"]
coffee_roasts = ["hot chocolate", "light", "medium", "dark", "espresso"]


def order_coffee(size, roast):
    
    return "here's your {} coffee roasted {} ".format(size, roast)

def add_milk(fat_content):
    
    return "I've added the {}% milk".format(fat_content)