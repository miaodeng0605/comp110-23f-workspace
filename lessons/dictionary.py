"""Practice with Dictionaries."""

#Constructing a dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("Make my dictionary.")
print(ice_cream)

#Adding an key, value pair to a dictionary
ice_cream["mint"] = 3
print("After adding a key.")
print(ice_cream)

#Removing a key, value pair from dictionary
ice_cream.pop("mint")
print("After removing a key")
print(ice_cream)

#Accessing a value
print(f"There are {ice_cream['chocolate']} orders of chocolate")

#Adjusting a value
ice_cream["vanilla"] += 2
print("After modification.")
print(ice_cream)

#Getting the length 
print(f"The nmber of key value pairs: {len(ice_cream)}")

#Checking if a value is in a dictionary
print("Is chocolate in ice_cream?")
print("chocolate" in  ice_cream)
print("Is mint in ice_cream?")
print("mint" in ice_cream)

#Using it in a conditional
if "mint" in ice_cream:
    print(f"There are {ice_cream['mint']} orders of mint")
else:
    print("no orders of mint")

#Loop through and print out every flavor and its number of orders
for key in ice_cream:
    #print "<flavor> has <num_orders> orders"
    print(f"{key} has {ice_cream[key]} orders.")