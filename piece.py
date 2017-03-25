class Piece:

    def __init__(self,nom, couleur, position, pdj):
        self.nom = nom
        self.couleur = couleur
        self.position = position
        self.pdj = pdj
        value = -1
        if self.nom[0] == 'p':
            value = 1
        elif self.nom[0] == 'c':
            value = 3
        elif self.nom[0] == 't':
            value = 4
        elif self.nom[0] == 'f':
            value = 3
        elif self.nom[0] == 'r':
            value = 100
        elif self.nom[0] == 'd':
           value = 10
        else:
            raise Exception('mauvais nom de pièces : n\' est pas p c f r d t')
        self.value = value

    def move(self, newcase):
        position =  newcase

    def __repr__(self):
        return self.nom

    def isWhite(self):
        return self.couleur == 0

    def isBlack(self):
        return self.couleur == 1

    def movePossibles(self):
        l = []
        if self.pdj.cases[self.position[0]][self.position[1]] is None:
            raise Exception('case de départ vide')
        else:
            #couleur blanche
                if self.nom[0] == 'p':
                    if self.couleur == 0:
                        l = self.possibleMoveWhitePawn()
                    else:
                        l = self.possibleMoveBlackPawn()
                elif self.nom[0] == 'c':
                    l = self.possibleMoveHorse()
                elif self.nom[0] == 't':
                    l = self.possibleMoveRook()
                elif self.nom[0] == 'f':
                    l = self.possibleMoveBishop()
                elif self.nom[0] == 'r':
                    l = self.possibleMoveKing()
                elif self.nom[0] == 'd':
                    l = self.possibleMoveQueen()
                else:
                    raise Exception('mauvais nom de pièces : n\' est pas p c f r d t')
        return l


    def possibleMoveWhitePawn(self):
        x = self.position[0]
        y = self.position[1]
        cases = self.pdj.cases
        l = []
        if cases[x+1][y].isFree():
            l.append(cases[x+1][y])
            if cases[x+2][y].isFree() and y == 1:
                l.append(cases[x+2][y])
        if y != 0:
            if cases[x+1][y-1].hasBlackPiece():
                l.append(cases[x+1][y-1])
        if y != 7:
            if cases[x+1][y + 1].hasBlackPiece():
                l.append(cases[x + 1][y + 1])
        return l

    def possibleMoveBlackPawn(self):
        x = self.position[0]
        y = self.position[1]
        cases = self.pdj.cases
        l = []
        if cases[x-1][y].isFree():
            l.append(cases[x-1][y])
            if cases[x-2][y].isFree() and x == 6:
                l.append(cases[x-2][y])
        if y != 0:
            if cases[x - 1][y - 1].hasWhitePiece():
                l.append(cases[x - 1][y - 1])
        if y != 7:
            if cases[x - 1][y + 1].hasWhitePiece():
                l.append(cases[x - 1][y + 1])
        return l

    def testCaseAndAdd(self, i, j, l):
        if self.couleur == 0:
            if self.pdj.cases[i][j].isFree() or self.pdj.cases[i][j].hasBlackPiece():
                l.append(self.pdj.cases[i][j])
        else:
            if self.pdj.cases[i][j].isFree() or self.pdj.cases[i][j].hasWhitePiece():
                l.append(self.pdj.cases[i][j])

    def possibleMoveKing(self):
        x = self.position[0]
        y = self.position[1]
        l = []
        if x != 7:
            self.testCaseAndAdd(x+1,y,l)
            if y != 7:
                self.testCaseAndAdd(x + 1, y + 1, l)
                self.testCaseAndAdd(x, y + 1, l)
            if y != 0:
                self.testCaseAndAdd(x + 1, y -1, l)
                self.testCaseAndAdd(x, y - 1, l)
        if x != 0:
            self.testCaseAndAdd(x - 1, y, l)
            if y != 7:
                self.testCaseAndAdd(x - 1, y + 1, l)
            if y != 0:
                self.testCaseAndAdd(x - 1, y - 1, l)
        return l

    def testCaseAndAddWithBool(self, i, j, l):
        b = False
        if self.couleur == 0:
            if self.pdj.cases[i][j].isFree():
                l.append(self.pdj.cases[i][j])
                b=True
            if self.pdj.cases[i][j].hasBlackPiece():
                l.append(self.pdj.cases[i][j])

        else:
            if self.pdj.cases[i][j].isFree():
                l.append(self.pdj.cases[i][j])
                b = True
            if self.pdj.cases[i][j].hasWhitePiece():
                l.append(self.pdj.cases[i][j])

        return b

    def possibleMoveRook(self):
        x = self.position[0]
        y = self.position[1]
        l = []
        i = x-1
        j = y
        b = True
        while i >= 0 and b:
            b = self.testCaseAndAddWithBool(i,j,l)
            i-=1
        i = x+1
        b = True
        while i <= 7 and b:
            b = self.testCaseAndAddWithBool(i,j,l)
            i+=1
        i = x
        j= y+1
        b = True
        while j <= 7 and b:
            b = self.testCaseAndAddWithBool(i,j,l)
            j+=1
        j=y-1
        b = True
        while j >= 0 and b:
            b = self.testCaseAndAddWithBool(i,j,l)
            j-=1
        return l


    def possibleMoveBishop(self):
        x = self.position[0]
        y = self.position[1]
        l = []
        i = x+1
        j = y+1
        b = True
        while i <= 7 and j <= 7 and b:
            b = self.testCaseAndAddWithBool(i,j,l)
            i+=1
            j+=1
        i = x - 1
        j = y + 1
        b = True
        while i >= 0 and j <= 7 and b:
            b = self.testCaseAndAddWithBool(i, j, l)
            i -= 1
            j += 1
        i = x + 1
        j = y - 1
        b = True
        while i <= 7 and j >= 0 and b:
            b = self.testCaseAndAddWithBool(i, j, l)
            i += 1
            j -= 1
        i = x - 1
        j = y - 1
        b = True
        while i >= 0 and j >= 0 and b:
            b = self.testCaseAndAddWithBool(i, j, l)
            i -= 1
            j -= 1
        return l

    def possibleMoveQueen(self):
        l = self.possibleMoveBishop()
        l2 = self.possibleMoveRook()
        return l+l2

    def possibleMoveHorse(self):
        x = self.position[0]
        y = self.position[1]
        l = []
        i = x + 2
        j = y + 1
        if i <= 7 and j <= 7:
            self.testCaseAndAdd(i,j,l)
        i = x + 2
        j = y - 1
        if i <= 7 and j >= 0:
            self.testCaseAndAdd(i, j, l)
        i = x - 2
        j = y + 1
        if i >= 0 and j <= 7:
            self.testCaseAndAdd(i, j, l)
        i = x - 2
        j = y - 1
        if i >= 0 and j >= 0:
            self.testCaseAndAdd(i, j, l)
        i = x + 1
        j = y + 2
        if i <= 7 and j <= 7:
            self.testCaseAndAdd(i, j, l)
        i = x + 1
        j = y - 2
        if i <= 7 and j >= 0:
            self.testCaseAndAdd(i, j, l)
        i = x - 1
        j = y + 2
        if i >= 0 and j <= 7:
            self.testCaseAndAdd(i, j, l)
        i = x - 1
        j = y - 2
        if i >= 0 and j >= 0:
            self.testCaseAndAdd(i, j, l)
        return l























