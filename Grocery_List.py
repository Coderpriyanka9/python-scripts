Grocery_List = []
while True:
    item = input("Enter item to add (or type 'done' to finish): ")
    if item.lower() == 'done':
        break
    Grocery_List.append(item)
print(Grocery_List)
