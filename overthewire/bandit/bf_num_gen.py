from itertools import product


lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lst = ["".join(item) for item in product(lst, repeat=4)]
with open("PINs.txt", 'a') as f:
    for i in lst:
        f.write('UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ ' + i + '\n')
