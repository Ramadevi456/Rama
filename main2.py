import timeit

# code snippet to be executed only once
mysetup = "from math import sqrt"
mycode = '''
def example():
    mylist = []
    for x in range(100):
        mylist.append(sqrt(x))
'''
# timeit statement
print (timeit.timeit(setup = mysetup,
                     stmt = mycode,
                     number = 100000))
