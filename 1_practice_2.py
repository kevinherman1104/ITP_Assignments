data = "3,5,7,23"
data = data.replace(","," ")
new_list = data.split()
print("list:" + str(new_list))
print("tuples:" + str(tuple(new_list)))