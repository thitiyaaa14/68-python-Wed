heroes = ['Ironman', 'Thor' , 'Hulk' , 'Superman' , 'Spiderman']
h2 = ['Dr.Strange', 'Cpt. America', 'Black Panter', 'Ant Man']

heroes.insert(0, h2[0])
print(heroes.index('Thor'))
heroes.insert(heroes.index('Thor'), h2[1])
print(heroes)
heroes.append('Superman')
heroes.append('Ant Man')
print(heroes)
heroes.sort()
print(heroes)
heroes.reverse()
print(heroes)
newheroe = heroes
newheroe[0] = 'Wonder Women'
print(heroes)
copyheroes = [] + heroes
print(copyheroes)
copyheroes[0] = 'Hanuman'
print(heroes)
print(copyheroes)