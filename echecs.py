from pdj import PlateauDejeu


print("hello")

positionInitialeB = [("tb1",0,0),("cb1",0,1),("fb1",0,2),("db1",0,3),("rb1",0,4),("fb2",0,5),("cb2",0,6),("tb2",0,7),("pb1",1,0),("pb2",1,1),("pb3",1,2),("pb4",1,3),("pb5",1,4),("pb6",1,5),("pb7",1,6),("pb8",1,7)]
positionInitialeN = [("tn1",7,0),("cn1",7,1),("fn1",7,2),("dn1",7,3),("rn1",7,4),("fn2",7,5),("cn2",7,6),("tn2",7,7),("pn1",6,0),("pn2",6,1),("pn3",6,2),("pn4",6,3),("pn5",6,4),("pn6",6,5),("pn7",6,6),("pn8",6,7)]

pdj = PlateauDejeu()
pdj.creationCases()
pdj.initpieces(positionInitialeB)
pdj.initpieces(positionInitialeN)

print(pdj)

print("========================")
pdj.move(0,1,3,3)
print(pdj)
pdj.move(3,3,7,3)
print(pdj)
print(pdj.piecesN)
print("test mouvement pion")
print(pdj.cases[4][1].contenu)
print(pdj.cases[1][4].contenu)
b = pdj.cases[1][2].hasWhitePiece()

print(pdj.cases[1][2])
print(pdj.cases[2][1])
l = pdj.cases[1][1].contenu.movePossibles()
print("l contient :" + str(l))


pdj.move(1,6,5,6)
l1 = pdj.cases[5][6].contenu.movePossibles()
print("l1 contient :" + str(l1))
l2 = pdj.cases[6][5].contenu.movePossibles()
print("l2 contient :" + str(l2))
l3 = pdj.cases[6][7].contenu.movePossibles()
print("l3 contient :" + str(l3))

l3 = pdj.cases[6][7].contenu.movePossibles()
print("l3 contient :" + str(l3))

def testMovePossibles(i,j):
    l3 = pdj.cases[i][j].contenu.movePossibles()
    print(str(pdj.cases[i][j].contenu.nom)+" en "+str(i)+", "+str(j)+" peut bouger en :" + str(l3))

testMovePossibles(5, 6)
testMovePossibles(6,5)
testMovePossibles(6,6)
testMovePossibles(0,4)
pdj.move(7,4, 2,0)
testMovePossibles(2,0)

print("HALO")


testMovePossibles(7,0)
pdj.move(7,7,5,3)
testMovePossibles(5,3)


testMovePossibles(7,2)
pdj.move(0,2,3,1)
testMovePossibles(3,1)

pdj.move(0,3,3,3)
testMovePossibles(3,3)

testMovePossibles(0,6)
pdj.move(7,1,5,2)
testMovePossibles(5,2)

print(pdj)
print("test meilleur move rang 1")








