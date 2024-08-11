#lambda function = a function written in 1 line using lambda keyword
# accepts any number of arguments, but only has one expression.*its a shortcut


def double(x):
    return x*2
print(double(5))

#Can be rewritten as 

double = lambda x:x*2
multiply = lambda x, y:x*y
add = lambda x, y, z: x+y+z
full_name = lambda first_name, last_name: first_name+ " " + last_name
age_check = lambda age: True if age>=18 else False

print(multiply(8,2))
print(add(3,6, 5))
print(full_name("Dominic", "Asiedu"))
print(age_check(18))
