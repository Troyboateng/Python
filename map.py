# Map = applies a function to each item in an iterable(list, tuple, etc)

#map(function, iterable)

store = [("shirt", 20.00),
       ("pants", 25.00),
       ("jacket", 50.00),
       ("socks", 10.00)]

#Coverting column 2 which is in $ to Euro using rate of 0.82
to_euros = lambda data:(data[0], data[1]*0.82)

to_dollars = lambda data:(data[0], data[1]/0.82)
store_dollars = list(map(to_dollars, store))
store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)
for k in store_euros, store_dollars:
    print(k)