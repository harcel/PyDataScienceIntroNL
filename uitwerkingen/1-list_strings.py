lijstje = [2, 1.4, 'aap']
print(lijstje)
lijstje += [4]
print(lijstje)
lijstje[1] = ['nog', 'drie', 'woordjes']
print(lijstje)
print(lijstje[1][1])
lijstje[1] = ['nog', 'drie', 'woordjes'] * 2
print(lijstje)
# print(lijstje+3) # Deze is commentaar want hij levert een error op, en dan gebeurt de volgende regel niet meer
# print(lijstje+'olifant') # Werkt niet
lijstje += 'olifant' # lijstje = lijstje + 'olifant' werkt ook niet!
print(lijstje)

lossewoorden = zin.split()
print(lossewoorden)
print(', '.join(lossewoorden))
print("Het kan in een keer met replace: ", zin.replace(' ', ', '))