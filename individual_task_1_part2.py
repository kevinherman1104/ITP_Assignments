def toRadian(degrees):
    return (degrees * (3.14/180))
degrees = 150 
radian = toRadian(degrees)
print("degrees = "+ str(degrees))
print("radian = " + str(radian))



print("\n")

def countAverage(student1,student2,student3):
    return((student1 + student2 + student3)/3)
print("Students scores =")

student1 = 80.0
print(student1)

student2 = 90.0
print(student2)

student3 = 66.5
print(student3)

average = countAverage(student1,student2,student3)
print("average = ",average)


print("\n")
w

Class_1 = 32
Class_2 = 45
Class_3 = 51

print("Number of students in each group:")
print("Class 1 = ", Class_1 // 5)
print("Class 2 = ", Class_2 // 7)
print("Class 3 = ", Class_3 // 6)

print("Number of students left :")
print("Class 1 = ", Class_1 % 5)
print("Class 2 = ", Class_2 % 7)
print("Class 3 = ", Class_3 % 6)

print("\n")

pi = 3.14
pie_diameter = 55.4
pie_radius = pie_diameter / 2
circumference = 2 * pi * pie_radius
circumference_msg = "Jimmy’s pie has a circumference: "
print(circumference_msg, circumference)

print("\n")

v = 343

print("The speed (m/s):",v)

f = 256

print("The frequency (Hz):",f)

wavelength = v/f

print("The wavelength (m):",wavelength)








