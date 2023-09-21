import random
import string

N = int(input("Enter number of username to create -> "))


def unique_username():
    while True:
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        yield username


# username =unique_username()
# print(next(username))
# print(next(username))
# print(next(username))
for k in range(N):
    username = unique_username()
    print(next(username))
