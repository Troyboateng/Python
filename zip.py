#Zip(*itereables) function - aggregate elements from two or more iterables
#(list, tuples, sets etc).
# creates a zip object with paired elements store in tuples for each element

usernames=["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_date = ["1/1/2024", "2/2/2024", "12/30/2023"]

#users = zip(usernames, passwords)
#users = list(zip(usernames, passwords)) #Can be made into a list/Dict or left alone
#users = dict(zip(usernames, passwords)) #dictionary
users = zip(usernames, passwords, login_date)

print(type(users))
for i in users:
    print(i)

