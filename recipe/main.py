from recipe import Recipe

def create_recipe(name, coffee=0, cholate=0, sugar=0, milk=0, price=0.0):
    recipe1 = Recipe(name)
    recipe1.coffee = coffee
    recipe1.sugar = sugar
    recipe3.chocolate = cholate
    recipe1.milk = milk
    recipe1.price = price
    return recipe1
    
if __name__ == '__main__':
    recipe1 = create_recipe("Coffee with sugar", 
                            coffee=4, cholate=0, 
                            sugar=2, milk=0, price=30.0)
    print(recipe1)
    recipe2 = create_recipe("Latte", 
                            coffee=3, cholate=0, 
                            sugar=2, milk=1, price=40.0)
    print(recipe2)
    recipe3 = create_recipe("Hot Chocolate", 
                            coffee=0, cholate=3, 
                            sugar=2, milk=4, price=30.0)
    print(recipe3)
    
    