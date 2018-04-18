users = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}


def accept_login(u, p):
    for i in users.keys():
        if u == i and p == users[i]:
            return print("Login successful! ")
    return print("Login failed... ")


user = input("Enter username: ")
password = input("Enter password: ")
accept_login(user, password)
# class User:
#     def accept_login(user, username, password):
