my_list = [100, 200, 150, 50, 80, 60]

print(my_list.count(100))
print(len(my_list))

print(my_list.index(100))

my_list.insert(0,80)
print(my_list)

my_list.append(500)
print(my_list)

my_list.remove(100)
print(my_list)

popped_item = my_list.pop(0)
print(my_list)
print(popped_item)

my_list.sort(reverse=False)
print(my_list)

my_list.reverse()
print(my_list)

my_list.clear()
print(my_list)

user_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(user_list[1:6:3])
print(user_list[:-2])

first_element = user_list[2]
print(first_element)

last_element = user_list[-1]
print(last_element)

product_name = []
product_quantity = []
product_price = []

product_name.append("iPhone")
product_quantity.append(1)
product_price.append(5000)

product_name.append("Laptop")
product_quantity.append(2)
product_price.append(2000)

print(product_name)
print(product_quantity)
print(product_price)

total_price = product_price[0] + product_price[1]
print("Total Price: ", total_price)

print(sum(product_price))

product_1_details = [product_name[0],product_quantity[0],product_price[0]]
print(product_1_details)



