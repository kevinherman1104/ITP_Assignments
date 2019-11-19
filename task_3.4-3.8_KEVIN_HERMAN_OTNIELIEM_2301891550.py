guests = ["lala","jason","katlin"]
print(guests[0] + "\nplease come to dinner")
print(guests[1] + "\nplease come to dinner")
print(guests[2] + "\nplease come to dinner")
print("\n")


print (guests[1] + " could not come")
print("\n")

guests[1] = "kevin"
print(guests[0] + "\nplease come to dinner")
print(guests[1] + "\nplease come to dinner")
print(guests[2] + "\nplease come to dinner")
print("\n")

print("We got a bigger table")
guests.insert(0,"lebron")
guests.insert(2,"kyrie")
guests.append("love")
print(guests[0] + "\nplease come to dinner")
print(guests[1] + "\nplease come to dinner")
print(guests[2] + "\nplease come to dinner")
print(guests[3] + "\nplease come to dinner")
print(guests[4] + "\nplease come to dinner")
print(guests[5] + "\nplease come to dinner")
print("\n")

print("Sorry guys but the table is only for 2")
print("\n")

popped_guests= guests.pop(1)
popped_guests_1= guests.pop(2)
popped_guests_2= guests.pop(1)
popped_guests_3= guests.pop(2)
print(popped_guests + "\nsorry maybe next time")
print(popped_guests_1 + "\nsorry maybe next time")
print(popped_guests_2 + "\nsorry maybe next time")
print(popped_guests_3 + "\nsorry maybe next time")
print("\n")

print(guests[0] + "\nyou are still invited")
print(guests[1] + "\nyou are still invited")
print("\n")

del guests[0]
del guests[0]
print(guests)

print("\n")

places = ["London","Italy","France","Japan","Australia"]
print(places)
print("\n")

sorted_places = sorted(places)
print(sorted_places)
print("\n")

print(places)
print("\n")

sorted_places_2 = sorted(places, reverse = True)
print(sorted_places_2)
print("\n")

print(places)
print("\n")

places.reverse()
print(places)
print("\n")

places.reverse()
print(places)
print("\n")

places.sort()
print (places)
print("\n")

places.sort(reverse = True)
print(places)














