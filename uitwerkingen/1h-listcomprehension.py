lijstje = [x+2 for x in range(5)]
lijstje2 = [3*x for x in "Python is Gaaf!"]
print(lijstje2)
lijstje3 = [x if x.isupper() else 2*x if x.islower() else 3*x for x in "Python is Gaaf!"]
print(lijstje3)
lijstje4 = [(i+1)*x for i, x in enumerate("Python is Gaaf!")]
print(lijstje4)
