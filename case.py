class Case:
	
	def __init__(self,i,j):
		self.position = (i,j)
		self.contenu = None 
		
	def __repr__(self):
		return str(self.position[0])+','+str(self.position[1])+':'+str(self.contenu)

	def isFree(self):
		return (self.contenu is None)

	def hasBlackPiece(self):
		if self.contenu is not None:
			return self.contenu.isBlack()
		else:
			return False

	def hasWhitePiece(self):
		if self.contenu is not None:
			return self.contenu.isWhite()
		else:
			return False