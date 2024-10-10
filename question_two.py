# Using a function, create the program that calculates the volume of the cylinder.
height = int(input("Enter height: "))
radius =  int(input("Enter radius: "))
volume_of_cylinder = 22/7*radius**2*height
print(f'The volume of cylinder with hieght: {height} and radius: {radius} is: {volume_of_cylinder}')


#2nd approach
import math
height = int(input("Enter height: "))
radius =  int(input("Enter radius: "))
pie_value = math.pi
volume = pie_value * radius**2*height
print(f" The volume of cylinder is: {volume}")