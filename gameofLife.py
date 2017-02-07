# DM Yo python

from tkinter import *
import time

nbLine = int (input("Saisir le nombre de ligne"))
nbCol = nbLine
fenetre = Tk()

#constructeur grille vide
def initialiser(nbCol, nbLine) :
  x = []
  for i in range(nbCol):
    y = []
    for j in range(nbLine):
      y.append(0)
    x.append(y)
  return(x)

#return nbVoisins vivant d'une cellule  
def nbVoisin(g,x,y):
  nbvoisin=0
  for i in range(x-1,x+2):
    for j in range(y-1,y+2):
      if i in range(nbLine) and j in range (nbCol)  :
        nbvoisin+=g[i][j]
  
  nbvoisin -= g[x][y]
  return(nbvoisin)
  
#creation de la grille fille  
def grilleSuivante(table) :
  comp = 1
  g = initialiser(nbLine,nbCol)
  for i in range(nbLine):
    for j in range(nbCol):
      if (nbVoisin(table, i, j) == 3) or ((table[i][j] == 1) and (nbVoisin(table,i,j) == 2)) :
        g[i][j] = 1
      else :
        g[i][j] = 0
  return(g)

#trace une grille sur canv de nbL/nbCol 
def drawGrille(canv):
  c = 500/nbCol
  a = c
  b = c
  for i in range(nbLine):
    ligne = canv.create_line(a,0,a,500)
    a += c
  for j in range(nbCol):
    colonne = canv.create_line(0,b,500,b)
    b += c
    
#trace un cercle sur canv de centre x,y et de rayon rad
def drawCircle(canv,x,y,rad): #OK
  canv.create_oval(x-rad,y-rad,x+rad,y+rad,width=0,fill='green')

#appelle drawCricle en boucle pour tracer les cercles en fonction de la grille
def creerLesCercles(canv, table): #OK
  for i in range (nbLine):
    for j in range(nbCol):
      if table[i][j] == 1:
        circle = drawCircle(canv, ((500/nbCol)*i)+(500/nbCol)/2, ((500/nbCol)*j)+(500/nbCol)/2, (500/nbCol)/2-1)
  
#bouton remise a zero
def effacer():
  global a
  canvas.delete("all")
  grille = drawGrille(canvas)
  a = initialiser(nbCol,nbLine)
  
 #bafficher etape suivante
def suivante(grille):  
  effacer()
  grilleSuiv = grilleSuivante(grille)
  circle = creerLesCercles(canvas, grilleSuiv)
  grille = grilleSuiv
  return grille

 #bouton appelant suivante
def boutonsuivant():
    global a
    a = suivante(a)
  
 #fonction pour l'event clic gauche 
def click(event):
  x, y = event.x, event.y
  if(x <= 500 and y <= 500): #si le click est dans canvas
    a[x//(500//nbCol)][y//(500//nbCol)] = 1
  circle = creerLesCercles(canvas, a)
  
 #appelle dessinBoucle
def automat():
  global arret
  dessinBoucle()
 
#change la valeur de la global "arret"  ainsi stop l'automatique
def stop():
  global arret
  arret = True

 #appelle boutonSuivant en boucle 
def dessinBoucle():
  global arret
  global a
  if arret == True or a == grilleSuivante(a):
    arret = False
    return 0   
  boutonsuivant()
  fenetre.after(1000, dessinBoucle)
  

canvas = Canvas(fenetre, width=500, height=500, background ='white')
grille = drawGrille(canvas)
canvas.bind('<Button-1>', click)

a = initialiser(nbCol,nbLine)
circle = creerLesCercles(canvas, a)
canvas.pack()

auto = Button(fenetre, text="Automatique", command=automat)
auto.pack()

arret = Button(fenetre, text="Stop", command=stop)
arret.pack()
  
etapeSuivante = Button (fenetre, text="Etape Suivante", command= boutonsuivant)
etapeSuivante.pack()

remiseAZero= Button (fenetre, text="Remise a zero", command=effacer)
remiseAZero.pack()

quitter = Button (fenetre, text="Quitter", command=fenetre.quit)
quitter.pack()

fenetre.mainloop()
fenetre.destroy()
