#########################################
# groupe MPCI 2
# GRP 2
# PAVIOT Mathis
# AKINCI Selin
# LUDIONGO Jordan
# ZTOTI Chahineze
# ORLHAC Maxime
# EL ALLALI Hicham
# https://github.com/uvsq22008474/projet_incendie/invitations
#########################################
import tkinter as tk
#############
# # GLOBALE
LARGE = 1000
HAUTEUR = 700

#############
# # FONCTION


def quadrillage():
    pass
    x0, x1 = 0, LARGE
    y = 0
    while y <= HAUTEUR:
        canvas.create_line(x0, y, x1, y, fill="black")
        y += 25
    y0, y1 = 0, LARGE
    x = 0
    while x <= LARGE:
        canvas.create_line(x, y0, x, y1, fill="black")
        x += 25

#################
# PROG_PRINCIPALE


root = tk.Tk()
canvas = tk.Canvas(bg="white", width=1000, height=700)
button_new_land = tk.Button(text="NEW LAND", width=15, height=2, bg="grey70")
button_save = tk.Button(text="SAVE", width=15, height=2, bg="grey70")
button_my_land = tk.Button(text="MY LAND", width=15, height=2, bg="grey70")
button_next_step = tk.Button(text="NEXT>>", width=15, height=2, bg="grey70")
button_start = tk.Button(text="START", width=15, height=2, bg="grey70")
button_stop = tk.Button(text="STOP", width=15, height=2, bg="grey70")
label = tk.Label(text="appuie sur '>' pour aller plus vite")


################
# # PLACEMENT
button_new_land.grid(row=0, column=6)
button_save.grid(row=2, column=6)
button_my_land.grid(row=1, column=6)
button_next_step.grid(row=5, column=2)
button_start.grid(row=5, column=1)
button_stop.grid(row=5, column=0)
label.grid(row=5,column=3)
canvas.grid(row=0, rowspan=4, column=0, columnspan=5)
quadrillage()
################
# BOUCLE
root.mainloop()
