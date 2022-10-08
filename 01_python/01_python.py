import math

# Variables

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 10
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

print(my_string_variable, my_int_variable, my_bool_variable)

## Day 2: 30 Days of python progamming

first_name = "Cesar"
last_name = "Estrada"
full_name = "Julio Cesar Peña Estrada"
country = "Chile"
city = "Concon"
age = 28
year = 2022
is_married = 2019
is_true = True
is_light_on = False
variable_one, variable_two = 1, 2

print(len(first_name))
print(len(first_name) == len(last_name))

num_one, num_two = 5, 4

total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two


radius = 30
radius = float(input("Enter a radius: "))
area_of_circle = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

print(area_of_circle)

first_name = input("First name: ")
last_name = input("Last name: ")
age = input("Age: ")
country = input("Country: ")
