from case import Case
from piece import Piece
from itertools import product

class PlateauDejeu:

    def __init__(self):
        self.cases = []
        self.piecesB = {}
        self.piecesN = {}
        self.value = 0

    def __repr__(self):
        st = ""
        for x in range(0,8):
            st += 'x '+str(7-x)+" "
            for y in range(0,8):
                i = 7-x
                j = y
                if self.cases[i][j].contenu is  None:
                    st += " ___"
                else:
                    st += " " + self.cases[i][j].contenu.nom
            st += "\n"
        st += " y:   0   1   2   3   4   5   6   7   "
        st += "\n  Valeur actuelle : "+str(self.value)
        if self.value > 0:
            st += "  Avantage aux blancs"
        elif self.value < 0:
            st += "Avantage aux noirs"
        return st

    def initpieces(self,piecepos):
        for (p,i,j) in piecepos:
            if p[1]=="n":
                self.piecesN[p]=Piece(p, 1, [i,j],self)
                self.cases[i][j].contenu = self.piecesN[p]
                self.value -= self.piecesN[p].value
            else:
                self.piecesB[p]=Piece(p, 0, [i,j],self)
                self.cases[i][j].contenu = self.piecesB[p]
                self.value += self.piecesB[p].value



    def creationCases(self):
        for i in range(0,8):
            self.cases.append([])
            for j in range(0,8):
                self.cases[i].append(Case(i,j))
        print("cases crees :{0}x{1}".format(len(self.cases),len(self.cases[0])))


    def move(self, oldI, oldJ, newI,newJ):
        pieceMangee = None
        if self.cases[oldI][oldJ].contenu is None:
            raise Exception('La case de départ est vide !')
        print("moving {} from ({}, {}) to ({}, {})".format(self.cases[oldI][oldJ].contenu.nom,oldI, oldJ, newI, newJ))
        if self.cases[newI][newJ].contenu is None:
            self.cases[newI][newJ].contenu = self.cases[oldI][oldJ].contenu
        else:
            pieceMangee = self.cases[newI][newJ].contenu
            self.cases[newI][newJ].contenu = self.cases[oldI][oldJ].contenu
            print(pieceMangee)
            if 1 == pieceMangee.couleur:
                print("piece mangée :" )
                print( self.piecesN.pop(pieceMangee.nom))
                self.value += pieceMangee.value
            else:
                print("piece mangée :" + self.piecesB.pop(pieceMangee.nom))
                self.value -= pieceMangee.value
        self.cases[oldI][oldJ].contenu = None
        self.cases[newI][newJ].contenu.position = [newI,newJ]
        return pieceMangee


    def GetPositionValue(self):
        value = 0
        for piece in self.piecesB:
            value += piece.value
        for piece in self.piecesN:
            value -= piece.value
        self.value = value
        return value


    def getBestMove(self, profondeur, couleur):
        if profondeur == 1:
            self.getBestMoveRankOne(couleur)
        else:
            l = self.getAllMoves()


    def getBestMoveRankOne(self, couleur):
        if couleur == 1:
            curBestValue = self.value
            curBestMove = None
            for piece in  self.piecesN:
                moves = piece.movePossibles()
                for move in moves:
                    l = 0
                    oldX = piece.position[0]
                    oldY = piece.position[1]
                    newX = move[0]
                    newY = move[1]
                    pieceMangee = move(oldX,oldY,newX,newY)
                    if pieceMangee is not None :
                        self.value -= pieceMangee.value
                    if curBestValue > self.value:
                        curBestValue = self.value
                        curBestMove = (oldX,oldY,newX,newY)
                    if pieceMangee is not None:
                        self.piecesB.append(pieceMangee)
                        self.value += pieceMangee.value
            return curBestMove
        else:
            curBestValue = self.value
            curBestMove = None
            for piece in self.piecesB:
                moves = piece.movePossibles()
                for move in moves:
                    l = 0
                    oldX = piece.position[0]
                    oldY = piece.position[1]
                    newX = move[0]
                    newY = move[1]
                    pieceMangee = move(oldX, oldY, newX, newY)
                    if pieceMangee is not None:
                        self.value += pieceMangee.value
                    if curBestValue < self.value:
                        curBestValue = self.value
                        curBestMove = (oldX, oldY, newX, newY)
                    if pieceMangee is not None:
                        self.piecesN.append(pieceMangee)
                        self.value -= pieceMangee.value
            return curBestMove




