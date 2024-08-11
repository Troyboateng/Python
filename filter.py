#filer() = creates a collection of elements from an iterable for which a function returns)

# filter (function, iterable)

friends = [("Rachel", 20),
       ("George", 25),
       ("Prince", 17),
       ("Kim", 12),
       ("Evelyn", 18)]
age = lambda data:data[1] >=18
drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)

print("=========================")
age=lambda data:data[1]<=18
none_Drinking=list(filter(age, friends))

for k in none_Drinking:
    print(k)