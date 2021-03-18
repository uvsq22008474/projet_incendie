####################

# PROJET INCENDIE

# MPCI TD 07

# Matthis PAVIOT


####################

# Import des librairies

import tkinter as tk
import random as rd


####################

# CONSTANTES

HEIGHT = 600
WIDTH = 600
COTE = 20
COUL_GRILLE = "grey"
COUL_EAU = "cornflower blue"
COUL_FORET = "lawn green"
COUL_PRAIRIE = "khaki"
COUL_FEU = "tomato"
COUL_CENDRET = "gray34"
COUL_CENDREN = "gray10"
DUREE_FEU = 4
DUREE_CENDRES = 2

####################

# Fonctions du Programme

def create_lists():
    """ genere des tableaux de la taille du canvas """
    l = list(range(WIDTH // COTE))
    for i in l:
        l[i] = list(range(WIDTH // COTE))
        for j in range(WIDTH // COTE):
            l[i][j] = 0
    return l

def grille():
    """ Dessine le grillage GRIS """
    x, y = 0, 0

    while y <= HEIGHT:
        canvas.create_line((0, y), (WIDTH, y), fill = COUL_GRILLE)
        y += COTE

    while x <= WIDTH:
        canvas.create_line((x, 0), (x,HEIGHT), fill = COUL_GRILLE)
        x += COTE

def generate_water(x, y):
    """ transforme la case en eau si elle n'est pas deja attribuee """
    i, j = x, y 
    
    if etat_case[i][j] == 0:
        a = i * COTE
        b = j * COTE
        carre = canvas.create_rectangle((a, b), (a + COTE, b + COTE), fill = COUL_EAU, outline = COUL_EAU)
        etat_case[i][j] = 2
        nature[i][j] = carre

def generate_forest(x, y):
    """ transforme la case en foret si elle n'est pas deja attribuee """
    i, j = x, y
    
    if etat_case[i][j] == 0:
        a = i * COTE
        b = j * COTE
        carre = canvas.create_rectangle((a, b), (a + COTE, b + COTE), fill = COUL_FORET, outline = COUL_FORET)
        nature[i][j] = carre
        etat_case[i][j] = 1 

def generate_land(x, y):
    """ transforme la case en prairie si elle n'est pas deja attribuee """
    i, j = x, y
    
    if etat_case[i][j] == 0:
        a = i * COTE
        b = j * COTE
        carre = canvas.create_rectangle((a, b), (a + COTE, b + COTE), fill = COUL_PRAIRIE, outline = COUL_PRAIRIE)
        etat_case[i][j] = 3
        nature[i][j] = carre

def generate_fire(x, y):
    """ transforme la case en feu uniquement si elle est en foret ou prairie """
    i, j = coord_case(x, y)
    
    if etat_case[i][j] == 3 or etat_case[i][j] == 1:
        a = i * COTE
        b = j * COTE
        canvas.delete(nature[i][j])
        carre = canvas.create_rectangle((a, b), (a + COTE, b + COTE), fill = COUL_FEU, outline = COUL_FEU)
        etat_case[i][j] = 4
        nature[i][j] = carre

def generate_warm_ashes(x, y):
    """ transforme la case en cendres tiedes uniquement si la case etait faite de feu a l'etat precedent """
    i, j = x, y
    
    if etat_case[i][j] == 4:
        a = i * COTE
        b = j * COTE
        canvas.delete(nature[i][j])
        carre = canvas.create_rectangle((a, b), (a + COTE, b + COTE), fill = COUL_CENDRET, outline = COUL_CENDRET)
        etat_case[i][j] = 5
        nature[i][j] = carre

def generate_ashes(x, y):
    """ transforme la case en cendres tiedes uniquement si la case etait faite de cendres tiedes a l'etat precedent """
    i, j = x, y
    
    if etat_case[i][j] == 5:
        a = i * COTE
        b = j * COTE
        canvas.delete(nature[i][j])
        carre = canvas.create_rectangle((a, b), (a + COTE, b + COTE), fill = COUL_CENDREN, outline = COUL_CENDREN)
        etat_case[i][j] = 6
        nature[i][j] = carre

def coord_case(x, y):
    """ donne les coord de la case du tableau selectionnee """
    #print("case de coord (", x//COTE, ",", y//COTE, ")")
    return x // COTE, y // COTE

def get_fire_click(event):
    """ met la case en feu au click """
    #print("getfireworks")
    generate_fire(event.x, event.y)

def detect_forest(x, y):
    """ compte le nombre d'arbres autour de la case """
    i, j = x, y
    n = 0

    if i >= 1:

        if j >= 1:

            if etat_case[i-1][j-1] == 1:
                n += 1

        if etat_case[i-1][j] == 1:
            n += 1
        
        if j <= len(etat_case) - 2:

            if etat_case[i-1][j+1] == 1:
                n += 1
            
    if j <= len(etat_case) - 2:
        if etat_case[i][j+1] == 1:
            n += 1

    if j >= 1:

        if etat_case[i][j-1] == 1:
            n += 1

        if i <= len(etat_case) - 2:

            if etat_case[i+1][j-1] == 1:
                n += 1
            
    if i <= len(etat_case) - 2:
        if etat_case[i+1][j] == 1:
            n += 1

    if i <= len(etat_case) - 2 and j <= len(etat_case) - 2:
        if etat_case[i+1][j+1] == 1:
            n += 1

    return n

def generate_forest_map():
    """ genere des lisieres de foret"""
    i, j = 0, 0

    #for i in range(HEIGHT // COTE):
        #for j in range(HEIGHT // COTE):
            #nb_arbres = detect_forest(i, j)
            #arbres[i][j] = nb_arbres
    
    for j in range(len(etangs)):
        for i in range(len(etangs)):

            nb_arbres = detect_forest(i, j)
            arbres[i][j] = nb_arbres

            if arbres[i][j] == 0:
                chance = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 1/20 chance
                choix = rd.choice(chance)
                #print(choix)
            if choix == 1:
                generate_forest(i, j)

            if arbres[i][j] == 1:
                chance = [1, 0, 0, 0, 0] # 1/5 chance
                choix = rd.choice(chance)

                if choix == 1:
                    generate_forest(i, j)

            if arbres[i][j] >= 3:
                chance = [1, 0, 0] # 1/3 chance
                choix = rd.choice(chance)

                if choix == 1:
                    generate_forest(i, j)

def detect_eau(x, y):
    """ compte le nombre de plans d'eau autour de la case """
    i, j = x, y
    n = 0

    if i >= 1:

        if j >= 1:

            if etat_case[i-1][j-1] == 2:
                n += 1

        if etat_case[i-1][j] == 2:
            n += 1
        
        if j <= len(etat_case) - 2:

            if etat_case[i-1][j+1] == 2:
                n += 1
            
    if j <= len(etat_case) - 2:
        if etat_case[i][j+1] == 2:
            n += 1

    if j >= 1:

        if etat_case[i][j-1] == 2:
            n += 1

        if i <= len(etat_case) - 2:

            if etat_case[i+1][j-1] == 2:
                n += 1
            
    if i <= len(etat_case) - 2:
        if etat_case[i+1][j] == 2:
            n += 1

    if i <= len(etat_case) - 2 and j <= len(etat_case) - 2:
        if etat_case[i+1][j+1] == 2:
            n += 1

    return n

def generate_water_map():
    """ genere des etangs """
    i, j = 0, 0

    #for i in range(HEIGHT // COTE):
        #for j in range(HEIGHT // COTE):
            #nb_arbres = detect_forest(i, j)
            #arbres[i][j] = nb_arbres
    
    for j in range(len(etangs)):
        for i in range(len(etangs)):

            nb_etangs = detect_eau(i, j)
            etangs[i][j] = nb_etangs
            arbres[i][j] = detect_forest(i, j)

            if arbres[i][j] == 0:

                if etangs[i][j] == 0:
                    chance = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 1/25 chance
                    choix = rd.choice(chance)
                    #print(choix)
                if choix == 1:
                    generate_water(i, j)

                if etangs[i][j] == 1:
                    chance = [1, 0, 0, 0, 0] # 1/5 chance
                    choix = rd.choice(chance)

                    if choix == 1:
                        generate_water(i, j)

                if etangs[i][j] >= 3:
                    chance = [1, 0, 0] # 1/3 chance
                    choix = rd.choice(chance)

                    if choix == 1:
                        generate_water(i, j)

def generate_land_map():
    """ rempli les cases qui ne sont pas eau ou foret """
    i, j = 0, 0

    for i in range(len(etangs)):
        for j in range(len(etangs)):

            if etat_case[i][j] == 0:
                generate_land(i,j)

def detect_feu(x, y):
    """ compte le nombre de cases en feu autour """
    i, j = x, y
    n = 0

    if i >= 1:

        if etat_case[i-1][j] == 4:
            n += 1
        
            
    if j <= len(etat_case) - 2:

        if etat_case[i][j+1] == 4:
            n += 1

    if j >= 1:

        if etat_case[i][j-1] == 4:
            n += 1
            
    if i <= len(etat_case) - 2:

        if etat_case[i+1][j] == 4:
            n += 1

    return n

def Propagation_feu():
    """ propage le feu dans les cases alentours selon les regles """
    i, j = 0, 0

    for i in range(len(etangs)):
        for j in range(len(etangs)):

            feu[i][j] = detect_feu(i, j)
            #if feu[i][j] != 0:
                #print("(",i,",",j,")", feu[i][j])
    
    for i in range(len(etangs)):
        for j in range(len(etangs)):

            if etat_case[i][j] == 3:

                if feu[i][j] >= 1:
                    x, y = i * COTE, j * COTE
                    generate_fire(x, y)

            if etat_case[i][j] == 1:

                if feu[i][j] == 1:
                    chance = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 1/10 chance
                    choix = rd.choice(chance)

                    if choix == 1:
                        x, y = i * COTE, j * COTE
                        generate_fire(x, y)

                if feu[i][j] == 2:
                    chance = [1, 0, 0, 0, 0] # 1/5 chance
                    choix = rd.choice(chance)

                    if choix == 1:
                        x, y = i * COTE, j * COTE
                        generate_fire(x, y)
                if feu[i][j] == 3:
                    chance = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0] # 3/10 chance
                    choix = rd.choice(chance)

                    if choix == 1:
                        x, y = i * COTE, j * COTE
                        generate_fire(x, y)
                
                if feu[i][j] == 4:
                    chance = [1, 1, 0, 0, 0] # 2/5 chance
                    choix = rd.choice(chance)

                    if choix == 1:
                        x, y = i * COTE, j * COTE
                        generate_fire(x, y)

def next_step():
    """ declenche le t+1 """
    Propagation_feu()
    temps_feu()
    temps_cendres()

    if pause == 0: # Lancement du compte a rebour (boucle)

        if choix_vitesse == 1:
            canvas.after(250, next_step)

        if choix_vitesse == 0:
            canvas.after(500, next_step)

        if choix_vitesse == 2:
            canvas.after(125, next_step)


def temps_feu():
    """ compte a rebour feu de la case """

    for i in range(len(etangs)):
        for j in range(len(etangs)):

            if etat_case[i][j] == 4:
                
                if t_feu[i][j] < DUREE_FEU:

                    t_feu[i][j] += 1

                else:
                    
                    t_feu[i][j] = 0
                    generate_warm_ashes(i, j)

def temps_cendres():
    """ compte a rebour cendres de la case """
    
    for i in range(len(etangs)):
        for j in range(len(etangs)):

            if etat_case[i][j] == 5:
                
                if t_cendres[i][j] < DUREE_CENDRES:

                    t_cendres[i][j] += 1

                else:
                    
                    t_cendres[i][j] = 0
                    generate_ashes(i, j)

def generate_full_map():
    """ Genere integralement la map """
    generate_forest_map() # genere les forets
    generate_water_map() # genere les etangs
    generate_land_map() # genere les champs

def PAUSE():
    global pause
    global playy 

    playy = 0
    pause = 1

def PLAY():
    global pause
    global playy

    if playy == 0: # On ne peut mettre play QUE s'il n'est pas deja sur play
        pause = 0
        playy = 1
        next_step()  

def diminuer_vitesse():
    global choix_vitesse
    global vitesses
    i = choix_vitesse

    if vitesses[i] > 0:
        choix_vitesse = vitesses[i-1]

def augmenter_vitesse():
    global choix_vitesse
    global vitesses
    i = choix_vitesse

    if vitesses[i] < 2:
        choix_vitesse = vitesses[i+1]

def restart():
    """ reinitialise toute la map """
    
    PAUSE()

    for i in range(len(etat_case)):
        for j in range(len(etat_case)):

            canvas.delete(nature[i][j])
            etat_case[i][j] = 0
            choix_vitesse = 1


####################

# Variables Globales

nature = create_lists() # tableau qui contient les carres (eau, foret etc..)
etat_case = create_lists() # tableau qui contient l'etat de la case (0 vide, 1 foret, 2 eau, 3 prairie, 4 feu, 5 cendret, 6 cendresn)
case_autour = create_lists() # tableau qui contient le nb de voisins en feu autour de la case
arbres = create_lists() # tableau qui contient le nb d'arbres voisins pour chaque case
etangs = create_lists() # tableau qui contient le nb d'etangs voisins pour chaque case
feu = create_lists() # tableau qui contient le nb de feux voisins pour chaque case
t_feu = create_lists() # tableau qui contient le temps en feu pour chaque case
t_cendres = create_lists() # tableau qui contient le temps en cendres pour chaque case
vitesses = [0, 1, 2] # trois vitesses d'animation possible

pause = 1
playy = 0
choix_vitesse = 1

####################

# Programme Principal

racine = tk.Tk() # Creation de la fenetre
racine.title("INCENDIE") # Titre de la fenetre

canvas = tk.Canvas(racine, bg = "white", height = HEIGHT, width = WIDTH) # Creation du Canvas
canvas.grid()

grille() # Creation de la grille

canvas.bind("<1>", get_fire_click)

etape_suivante = tk.Button(racine, text = "ETAPE SUIVANTE", command = next_step, font = ("helvetica", "10")) #bouton prochaine etape
etape_suivante.grid(row = 0, column = 1 ) #positionnement bouton " etape suivante "

generer_map = tk.Button(racine, text = "GENERER MAP", command = generate_full_map, font = ("helvetica", "10")) #bouton genere map
generer_map.grid(row = 0, column = 2 ) #positionnement bouton " generer map "

pause = tk.Button(racine, text = "PAUSE", command = PAUSE, font = ("helvetica", "10")) # Creer Bouton Pause
pause.grid(row = 0, column = 3)

play = tk.Button(racine, text = "PLAY", command = PLAY, font = ("helvetica", "10")) # Creer Bouton play
play.grid(row = 0, column = 4)

moins_vite = tk.Button(racine, text = "- vite", command = diminuer_vitesse, font = ("helvetica", "10"))
moins_vite.grid(row = 0, column = 5)

plus_vite = tk.Button(racine, text = "+ vite", command = augmenter_vitesse, font = ("helvetica", "10"))
plus_vite.grid(row = 0, column = 6)

recommencer = tk.Button(racine, text = "recommencer", command = restart, font = ("helvetica", "10"))
recommencer.grid(row = 0, column = 7)

racine.mainloop()