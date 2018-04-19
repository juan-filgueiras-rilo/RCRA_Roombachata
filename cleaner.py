import os
import math
import sys
#clase salida
class tile():
	def __init__(self,x,y,val):
		self.x=x
		self.y=y
		self.val=val
	def toClingo(self,salida):
		salida.storetail('tile('+str(self.x)+','+str(self.y)+','+str(self.val)+').\n')

class salida():
	def __init__(self,ficherosalida):
		self.fsalida=open(ficherosalida,'w')
		self.strstored=''
	def publica (self):
		print(self.strstored)
	def storetail(self,cosas):
		self.strstored=self.strstored+cosas
	def storehead(self,cosas):
		self.strstored=cosas+self.strstored
	def privado(self):
		self.fsalida.write(self.strstored)
	def close(self):
		self.fsalida.close()
#clase tabla
class tabla:
	def __init__(self,fichero):
		self.lmapa=[]
		f=open(fichero,'r')
		i=0
		j=0
		linea="Apruebanos"
		while (linea!=""):
			linea=f.readline()
			if (linea.lstrip(' ').lstrip("\n")==""): 
				linea=f.readline()
				continue
			else:
				self.maxx= len(linea)-2
				for i in range(0,len(linea)-1):
					self.lmapa.append((linea[i]))
	def toClingo(self,salidafinal,base):
		linea="apruebanos"
		f=open(base,'r')
		
		while(linea!="% Initial state\n"):
			linea=f.readline()
			salidafinal.storetail(linea)
		self.showMapa(salidafinal)
		while(linea!=""):
			linea=f.readline()
			salidafinal.storetail(linea)
		f.close()
	def showMapa(self,salida):
		i=0
		for i in range(0,len(self.lmapa)):
			if ((i % (self.maxx+1) == 0) and (i!=0)):
				salida.storetail("\n")
			#print(self.gettype(self.lmapa[i]))		
			salida.storetail("tile("+str(math.floor(i/(self.maxx+1))+1)+","+str(i%(self.maxx+1)+1)+","+self.gettype(self.lmapa[i])+").\n")
	def gettype (self,simbolo):
		if simbolo=="#": return "obs"
		if simbolo==".": return "free"
		if simbolo=="@": return "initial"
		if simbolo=="X": return "goal"

def main():
	t=tabla(sys.argv[1])
	sclgsol=salida("finalrules.txt")	
	
	t.toClingo(sclgsol,"cleaner.txt")
	sclgsol.privado()
	sclgsol.close()
	os.system('clingo 0 finalrules.txt')
	
if __name__ == "__main__":
    # execute only if run as a script
    main()