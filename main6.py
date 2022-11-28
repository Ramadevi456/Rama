import re
string=input("enter a string")
def find(string):
    special_char=re.compile('[!@#$%^&*()_+-=:"><;{}]')
    if special_char.search(string):

    else:
        print(string)
