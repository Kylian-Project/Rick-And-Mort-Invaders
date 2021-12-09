import pygame # importation de la librairie pygame
from pygame.locals import *
from moviepy.editor import *
import sys # pour fermer correctement l'application
import random

#--------------------- CLASS ------------------#

class Joueur(pygame.sprite.Sprite) : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        super().__init__()
        self.sens = ""
        self.image = pygame.image.load("img/pisto.png")
        self.imagerect = self.image.get_rect()
        self.imagerect.x, self.imagerect.y = 500, 360
        self.image2 = pygame.image.load("img/tete.png")
        self.imagerect2 = self.image2.get_rect()
        self.image3 = pygame.image.load("img/icon/step1.png")
        self.imagerect3 = self.image2.get_rect()
        self.imagerect3.x, self.imagerect3.y = 515, 20
        self.imagerect2.x, self.imagerect2.y = self.imagerect.x, 50
        self.depart = self.imagerect.x
        self.score = 0
        self.vie = 3
        self.level = 1
        self.groupe = pygame.sprite.Group()
        self.vitesse = 4
    def deplacer(self):
        if self.sens == "gauche" and self.imagerect.x > 235:
            self.imagerect.x -= self.vitesse
        elif self.sens == "droite" and self.imagerect.x <840:
            self.imagerect.x += self.vitesse
    def tirer(self):
        obus = Balle(self)
        self.groupe.add(obus)
    def marquer(self):
        self.score += 1
        if self.score%10 == 0:
            self.level += 1
    def hp(self):
        self.vie -=1
        if self.vie == 2:
            self.image3 = pygame.image.load("img/icon/step2.png")
        elif self.vie == 1:
            self.image3 = pygame.image.load("img/icon/step3.png")
    def toucher(self,ennemi):
        if -60<self.hauteur-ennemi.imagerect.y<60 and -60<self.depart-ennemi.imagerect.x<60:
            return True
        else:
            return False

class Balle(pygame.sprite.Sprite):
    def __init__(self,joueur):
        super().__init__()
        self.etat = ""
        self.etat2 = ""
        self.image = pygame.image.load("img/balle.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = joueur.imagerect.x+10
        self.rect.y = 360
        self.joueur = joueur
        self.vitesse = 2
    def bouger(self):
        self.rect.y -= self.vitesse
    def toucher(self,ennemi):
        if self.rect.colliderect(ennemi.imagerect):
            return True
        else:
            return False

class ennemi():
    Nbennemis = 2
    def __init__(self) :
        self.type = random.randint(1,5)
        self.image = pygame.image.load("img/invader1.png").convert_alpha()
        if self.type == 1:
            self.image = pygame.image.load("img/invader1.png").convert_alpha()
            self.imagerect = self.image.get_rect()
        elif self.type == 2:
            self.image = pygame.image.load("img/invader2.png").convert_alpha()
            self.imagerect = self.image.get_rect()
        elif self.type == 3:
            self.image = pygame.image.load("img/meteor.png").convert_alpha()
            self.imagerect = self.image.get_rect()
        elif self.type == 4:
            self.image = pygame.image.load("img/invader4.png").convert_alpha()
            self.imagerect = self.image.get_rect()
        else:
            self.image = pygame.image.load("img/invader3.png").convert_alpha()
            self.imagerect = self.image.get_rect()
        self.imagerect = self.image.get_rect()
        self.imagerect.x, self.imagerect.y = random.randint(250,810), random.randint(-2000,-100)
        self.vitesse = 2
    def avancer(self):
            self.imagerect.y += self.vitesse
    def disparaitre(self):
        self.imagerect.x = random.randint(250,810)
        self.imagerect.y = random.randint(-2000,-100)
    def replay(self):
        self.imagerect.x = 10000
        self.imagerect.y = -100000000

#--------------------- CLASS ------------------#

# lancement des modules inclus dans pygame
pygame.init() 

# création d'une fenêtre de 800 par 600
fenetre = pygame.display.set_mode((1100,600))
pygame.display.set_caption("Rick And Mort'invader") 

#--------------------- Load des Images ------------------#
# Colisions
rectangle = pygame.image.load("img/colide/colision.png").convert_alpha()
colid_invader1 = pygame.image.load("img/colide/colid_invader1.png").convert_alpha()
colide_pisto_rect = rectangle.get_rect()
colid_invader1_rect = colid_invader1.get_rect()

# Variable curseur
nbcurseur = 'img/icon/curseur1.png'

# Image menu / icons / Buttons (menu princiaple)
background_menu = pygame.image.load("img/menu.png").convert_alpha()
rect_backmenu = background_menu.get_rect()

play_button = pygame.image.load("img/icon/play_but.png").convert_alpha()
rect_play = play_button.get_rect()
rect_play.x, rect_play.y = 402, 356  # place l'image sur l'écran

leave_button = pygame.image.load("img/icon/leave_but.png").convert_alpha()
rect_leave = leave_button.get_rect()
rect_leave.x, rect_leave.y = 402, 469  # place l'image sur l'écran

info_button = pygame.image.load("img/icon/info.png").convert_alpha()
rect_info = info_button.get_rect()
rect_info.x, rect_info.y = 1026, 10  # place l'image sur l'écran

setting_button = pygame.image.load("img/icon/gear.png").convert_alpha()
rect_setting = setting_button.get_rect()
rect_setting.x, rect_setting.y = 10, 524  # place l'image sur l'écran

close_button = pygame.image.load("img/icon/close.png").convert_alpha()
rect_close = close_button.get_rect()
rect_close.x, rect_close.y = 720, 76  # place l'image sur l'écran

# Image menu / icons / Buttons (menu info)
img_back_info = pygame.image.load("img/menu_info.png").convert_alpha()
rect_back_info = img_back_info.get_rect()

resume_button = pygame.image.load("img/icon/reprendre.png").convert_alpha()
rect_resume = resume_button.get_rect()
rect_resume.x, rect_resume.y = 428, 215  # place l'image sur l'écran

rect_close2 = close_button.get_rect()
rect_close2.x, rect_close2.y = 670, 73  # place l'image sur l'écran

menu_button = pygame.image.load("img/icon/menu_button.png").convert_alpha()
rect_menu = menu_button.get_rect()
rect_menu.x, rect_menu.y = 428, 295  # place l'image sur l'écran

leave_button_pause = pygame.image.load("img/icon/quitter.png").convert_alpha()
rect_leave_button = leave_button_pause.get_rect()
rect_leave_button.x, rect_leave_button.y = 428, 375  # place l'image sur l'écran

setting_button2 = pygame.image.load("img/icon/gear2.png").convert_alpha()
rect_setting2 = setting_button2.get_rect()
rect_setting2.x, rect_setting2.y = 400, 434  # place l'image sur l'écran

# Image menu / icons / Buttons (menu pause)
img_back_pause = pygame.image.load("img/menu_pause.png").convert_alpha()
rect_back_pause = img_back_pause.get_rect()

on_button = pygame.image.load("img/icon/on.png").convert_alpha()
rect_on_son = on_button.get_rect()  # button on du son
rect_on_son.x, rect_on_son.y = 653, 263
rect_on_debug = on_button.get_rect()  # button on du mode debug
rect_on_debug.x, rect_on_debug.y = 653, 343

off_button = pygame.image.load("img/icon/off.png").convert_alpha()
rect_off_son = off_button.get_rect()  # button off du son
rect_off_son.x, rect_off_son.y = 653, 263
rect_off_debug = off_button.get_rect()  # button off du mode debug
rect_off_debug.x, rect_off_debug.y = 653, 343

# Image menu / icons / Buttons (menu options)
img_back_option = pygame.image.load("img/menu_option.png").convert_alpha()
rect_back_option = img_back_option.get_rect()

rect_leave_button2 = leave_button.get_rect()
rect_leave_button2.x, rect_leave_button2.y = 767, 284  # place l'image sur l'écran

replay_button = pygame.image.load("img/icon/rejouer.png").convert_alpha()
rect_replay = replay_button.get_rect()
rect_replay.x, rect_replay.y = 37, 284  # place l'image sur l'écran

menu_button2 = pygame.image.load("img/icon/menu_button2.png").convert_alpha()
rect_menu2 = menu_button2.get_rect()
rect_menu2.x, rect_menu2.y = 402, 500  # place l'image sur l'écran

img_back_fin = pygame.image.load("img/menu_fin.png").convert_alpha()
rect_back_fin = img_back_fin.get_rect()

# Son
tir_sound = pygame.mixer.Sound('son/tir.mp3')
expl_sound = pygame.mixer.Sound('son/expl.mp3')

fond = pygame.image.load('img/background3.png').convert_alpha()
fond2 = pygame.image.load('img/cockpit.png').convert_alpha()
fond3 = pygame.image.load('img/charge.png').convert_alpha()

fenetre.blit(fond3,(0,0))
pygame.display.update()

clip = VideoFileClip('img/intro.mpg')
#------------------ FIN Load des Images ------------------#
listeennemis = []

def reload():
    global player, listeennemis
    listeennemis = []
    # creation du joueur
    player = Joueur()
    player.vitesse = 4
    # creation de la balle
    # creation des ennemis
    vaisseau.Nbennemis = 2
    for ennemi in listeennemis:
        ennemi.disparaitre()

# Variable menu option
music_on = 1 #variable musique activer au début du jeu
debug_on = 0 #variable mode debug désactiver au debut du jeu

def actumechant():
    global vaisseau
    for indice in range(ennemi.Nbennemis):
        vaisseau = ennemi()
        listeennemis.append(vaisseau)
for indice in range(ennemi.Nbennemis):
        vaisseau = ennemi()
        listeennemis.append(vaisseau)

#-------------------------------------------------------------------------------------------------------------#

def option_menu():
    """
        Procédure du menu principale, appelé en premier lors du lancement du jeu
    """
    global rectangle, colid_invader1, nbcurseur, on_button, off_button, music_on, debug_on
    in_option = 1 #variable de la boucle en dessous
    while in_option:
        pointer() #appele la procédure du changement de pointeur de souris
        for event in pygame.event.get():  # On parcourt la liste de tous les événements reçus
            if event.type == QUIT:  # Si un de ces événements est de type QUIT
                in_option = 0  # On arrête la boucle
                menu = 0 #termine la boucle menu
            if event.type == KEYDOWN:  # si une touche pressé
                if event.key == K_ESCAPE:  # si touche echap pressé
                    in_option = 0  # On arrête la boucle
            if event.type == pygame.MOUSEBUTTONDOWN:  # si click souris pressé
                if rect_on_son.collidepoint(event.pos): #si button "son on" clické
                    music_on = not music_on #music_on reçois sont inverse quand clické
                    if music_on: #si musique activer
                        pygame.mixer.music.unpause()
                        on_button = pygame.image.load("img/icon/on.png").convert_alpha() #affiche image bonton "on"
                        print('musique :', music_on) #print dans la console (sert a rien)
                    else:
                        pygame.mixer.music.pause()
                        on_button = pygame.image.load("img/icon/off.png").convert_alpha() #afffiche image button "off"
                        print('musique :', music_on) #print dans la console (sert a rien)
                if rect_off_debug.collidepoint(event.pos): #si button "debug off" clické
                    debug_on = not debug_on #mode debug reçoit sont inverse quand clické
                    if debug_on: #si debug activé
                        off_button = pygame.image.load("img/icon/on.png").convert_alpha() #reçoit button "on"
                        rectangle = pygame.image.load("img/colide/colision_debug.png") #reçoit image du mode debug
                        colid_invader1 = pygame.image.load("img/colide/colid_invader1_debug.png")
                        print('debug :', debug_on) #print dans la console (sert a rien)
                    else:
                        off_button = pygame.image.load("img/icon/off.png").convert_alpha() #reçoit button "off"
                        rectangle = pygame.image.load("img/colide/colision.png") #reçoit image normal
                        colid_invader1 = pygame.image.load("img/colide/colid_invader1.png")
                        print('debug :', debug_on) #print dans la console (sert a rien)
                if rect_close.collidepoint(event.pos): #si croix clické
                    in_option = 0 #ferme la boucle option
        if rect_close.collidepoint(pygame.mouse.get_pos()) or rect_on_son.collidepoint(
                pygame.mouse.get_pos()) or rect_off_son.collidepoint(
                pygame.mouse.get_pos()) or rect_on_debug.collidepoint(
                pygame.mouse.get_pos()) or rect_off_debug.collidepoint(pygame.mouse.get_pos()):
                #si souris survole croix, button on-off son et debug
            nbcurseur = "img/icon/curseur2.png"  # affiche le curseur 2, la main
        else:  # sinon, laisse le curseur 1
            nbcurseur = "img/icon/curseur1.png"
        fenetre.blit(img_back_option, rect_back_option)
        fenetre.blit(close_button, rect_close)
        fenetre.blit(on_button, rect_on_son)
        fenetre.blit(off_button, rect_off_debug)

#-------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------------------------#

def end_menu():
    """
        Procédure du menu fin appelé en fin de partie pour ouvrir le menu "Game Over"
    """
    global nbcurseur, score1
    pygame.mouse.set_visible(False)  # cacher la souris de base pour mettre la nouvelle (personnalisé)
    player = Joueur()
    in_end = 1
    while in_end:
        pointer()
        for event in pygame.event.get():  # On parcourt la liste de tous les événements reçus
            if event.type == QUIT:  # Si un de ces événements est de type QUIT
                sys.exit() # pour fermer correctement
            if event.type == KEYDOWN:  # si une touche pressé
                if event.key == K_ESCAPE:  # si touche echap pressé
                    sys.exit() # pour fermer correctement
                if event.key == K_RETURN:  # si touche echap pressé
                    in_end = 0  # On arrête la boucle
                    jouer() # On appele la procédure du jeu
            if event.type == pygame.MOUSEBUTTONDOWN:  # si click souris pressé
                if rect_leave_button2.collidepoint(event.pos):
                    sys.exit() # pour fermer correctement
                if rect_replay.collidepoint(event.pos):
                    in_end = 0 # On arrête la boucle
                    jouer() # On appele la procédure du jeu
                if rect_menu2.collidepoint(event.pos):
                    in_end = 0 # On arrête la boucle
                    main_menu() # On appele le menu principale
        if rect_replay.collidepoint(pygame.mouse.get_pos()) or rect_leave_button2.collidepoint(
                pygame.mouse.get_pos()) or rect_menu2.collidepoint(pygame.mouse.get_pos()):
                #si curseur survole le button play, quitter ou menu principale
            nbcurseur = "img/icon/curseur2.png"  # affiche le curseur 2, la main
        else:  # sinon, laisse le curseur 1
            nbcurseur = "img/icon/curseur1.png"
        fenetre.blit(img_back_fin, rect_back_fin)
        fenetre.blit(replay_button, rect_replay)
        fenetre.blit(leave_button, rect_leave_button2)
        fenetre.blit(menu_button2, rect_menu2)
        police2 = pygame.font.Font("zorque.otf", 60)
        pt = (f"{score1}")
        rendu = police2.render(str(pt), 1, (0, 255, 162))
        fenetre.blit(rendu, (630,285))
        with open('sav.txt', 'r') as f:  #ouvre le fichier "sav.txt" en mode lecture
            liste = f.read().splitlines() #liste reçoit les info du fichier
            if score1 > int(liste[1]): #si le score actuelle est plus grand que le score du fichier
                score2 = police2.render(str(player.score), 1, (0, 255, 162))
            else: #sinon prend le meilleur score écrit dans le fichier
                score2 = police2.render(str(liste[1]), 1, (0, 255, 162))
        fenetre.blit(score2, (580, 378)) # Blit meilleur score, celui qui est sauvegardé dans un fichier txt
#-------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------------------------#

def pointer():
    """
        procédure qui place une image de curseur sur celui de base en temps réel
    """
    curseur = pygame.image.load(
        nbcurseur).convert_alpha()  # "convert_alpha()" permet d'importer l'image avec sa transparence (png)
    curseur_rect = curseur.get_rect()
    x, y = pygame.mouse.get_pos()  # prend la position de la souris en temps réel
    curseur_rect.x, curseur_rect.y = x, y  # applique les postions de la lignes au dessus au nouveaux curseur
    fenetre.blit(curseur, curseur_rect)  # affiche le nouveau curseur
    pygame.display.flip()  # raffraichit l'écran

#-------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------------------------#

def main_menu():
    """
        Procédure du menu principale appelé en premier lors du lancement du programme
        Peut être appellé a chaque fois que l'on veut retourner au menu
    """
    global nbcurseur, music_on, debug_on, rectangle, img_back_option
    pygame.mixer.music.load("son/back.mp3")
    pygame.mixer.music.play(-1, 0.0, 0)
    pygame.mouse.set_visible(False)  # cacher la souris de base pour mettre la nouvelle (personnalisé)
    menu = 1
    while menu:
        pointer()  # appelle la fonction pour le nouveau pointeur
        for event in pygame.event.get():  # On parcourt la liste de tous les événements reçus
            if event.type == QUIT:  # Si un de ces événements est de type QUIT
                sys.exit() # pour fermer correctement
            if event.type == KEYDOWN:  # si une touche pressé
                if event.key == K_ESCAPE:  # si touche echap pressé
                    sys.exit() # pour fermer correctement
            if rect_play.collidepoint(pygame.mouse.get_pos()) or rect_leave.collidepoint(
                    pygame.mouse.get_pos()) or rect_info.collidepoint(pygame.mouse.get_pos()) or rect_setting.collidepoint(pygame.mouse.get_pos()):
                nbcurseur = "img/icon/curseur2.png"  # affiche le curseur 2, la main
            else:  # sinon, laisse le curseur 1
                nbcurseur = "img/icon/curseur1.png"
            if event.type == pygame.MOUSEBUTTONDOWN:  # si click souris pressé
                if rect_play.collidepoint(event.pos):
                    jouer()
                    menu = 0
                if rect_leave.collidepoint(event.pos):
                    menu = 0
                if rect_info.collidepoint(event.pos):
                    in_info = 1
                    while in_info:
                        pointer()
                        for event in pygame.event.get():  # On parcourt la liste de tous les événements reçus
                            if event.type == QUIT:  # Si un de ces événements est de type QUIT
                                sys.exit() # pour fermer correctement
                            if event.type == KEYDOWN:  # si une touche pressé
                                if event.key == K_ESCAPE:  # si touche echap pressé
                                    in_info = 0  # On arrête la boucle
                            if rect_close.collidepoint(pygame.mouse.get_pos()):
                                nbcurseur = "img/icon/curseur2.png"  # affiche le curseur 2, la main
                            else:  # sinon, laisse le curseur 1
                                nbcurseur = "img/icon/curseur1.png"
                            if event.type == pygame.MOUSEBUTTONDOWN:  # si click souris pressé
                                if rect_close.collidepoint(event.pos):
                                    in_info = 0
                        fenetre.blit(img_back_info, rect_back_info)
                        fenetre.blit(close_button, rect_close)
                elif rect_setting.collidepoint(event.pos):
                    img_back_option = pygame.image.load("img/menu_option.png").convert_alpha()
                    option_menu()

        fenetre.blit(background_menu, rect_backmenu)  # affiche image de fond menu
        fenetre.blit(play_button, rect_play)
        fenetre.blit(leave_button, rect_leave)
        fenetre.blit(info_button, rect_info)
        fenetre.blit(setting_button, rect_setting)

#-------------------------------------------------------------------------------------------------------------#


#-------------------------------------------------------------------------------------------------------------#

### BOUCLE DE JEU  ###
def jouer():
    clip.preview() #lance la vidéo pour annimation
    pygame.mixer.music.load("son/menu.ogg")
    pygame.mixer.music.play(-1, 0.0, 0)
    global nbcurseur, vitessetir, score1
    reload()
    actumechant()
    vitessetir = 80
    pygame.mouse.set_visible(False)  # cacher la souris de base pour mettre la nouvelle (personnalisé)
    running = True # variable pour laisser la fenêtre ouverte
    counter = 0
    while running : # boucle infinie pour laisser la fenêtre ouverte
        pygame.time.Clock().tick(200)  # pour ralentir la boucle de jeu (200)
        colide_pisto_rect.x, colide_pisto_rect.y = player.imagerect.x+10, player.imagerect.y
        player.imagerect2.x, player.imagerect2.y = player.imagerect.x-10, 455

        counter += 1 #reload de la balle
        # dessin du fond
        fenetre.blit(fond,(0,0))

        ### Gestion des événements  ###
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False # running est sur False
                sys.exit() # pour fermer correctement
            if event.type == pygame.KEYDOWN : # si une touche a été tapée KEYUP quand on relache la touche
                if event.key == pygame.K_ESCAPE :
                    in_pause = 1
                    while in_pause:
                        pointer()
                        for event in pygame.event.get():  # On parcourt la liste de tous les événements reçus
                            if event.type == QUIT:  # Si un de ces événements est de type QUIT
                                sys.exit() # pour fermer correctement
                            if event.type == KEYDOWN:  # si une touche pressé
                                if event.key == K_ESCAPE:
                                    in_pause = 0  # On arrête la boucle
                            if event.type == pygame.MOUSEBUTTONDOWN:  # si click souris pressé
                                if rect_resume.collidepoint(event.pos) or rect_close2.collidepoint(event.pos):
                                    in_pause = 0
                                if rect_menu.collidepoint(event.pos):
                                    in_pause = 0
                                    running = 0
                                    for ennemi in listeennemis:
                                        ennemi.disparaitre()
                                    main_menu()
                                if rect_leave_button.collidepoint(event.pos):
                                    sys.exit() # pour fermer correctement
                                if rect_setting2.collidepoint(event.pos):
                                    # img_back_option = pygame.image.load("img/menu_option2.png").convert_alpha()
                                    option_menu()
                        if rect_resume.collidepoint(pygame.mouse.get_pos()) or rect_menu.collidepoint(
                                pygame.mouse.get_pos()) or rect_leave_button.collidepoint(
                                pygame.mouse.get_pos()) or rect_setting2.collidepoint(
                                pygame.mouse.get_pos()) or rect_close2.collidepoint(pygame.mouse.get_pos()):
                            nbcurseur = "img/icon/curseur2.png"  # affiche le curseur 2, la main
                        else:  # sinon, laisse le curseur 1
                            nbcurseur = "img/icon/curseur1.png"
                        fenetre.blit(img_back_pause, rect_back_pause)
                        fenetre.blit(resume_button, rect_resume)
                        fenetre.blit(menu_button, rect_menu)
                        fenetre.blit(leave_button_pause, rect_leave_button)
                        fenetre.blit(setting_button2, rect_setting2)
                        fenetre.blit(close_button, rect_close2)
        k = pygame.key.get_pressed()
        if k[K_LEFT] and k[K_SPACE]:
            player.sens = "gauche"
            if counter > vitessetir:
                player.tirer()
                if music_on == 1:
                    tir_sound.play()
                counter = 0
        elif k[K_RIGHT] and k[K_SPACE]:
            player.sens = "droite"
            if counter  > vitessetir:
                player.tirer()
                if music_on == 1:
                    tir_sound.play()
                counter = 0
        else:
            player.sens = ""
        if k[K_LEFT]:
            player.sens = "gauche"
        elif k[K_RIGHT]:
            player.sens = "droite"
        elif k[K_SPACE]:
            if counter > vitessetir:
                player.tirer()
                if music_on == 1:
                    tir_sound.play()
                counter = 0
        else:
            player.sens = ""

        ### Actualisation de la scene ###
        # Gestions des collisions
        for ennemi in listeennemis:
            for element in player.groupe:
                if element.rect.y < -20:
                    element.kill()
                if element.toucher(ennemi):
                    element.kill()
                    ennemi.disparaitre()
                    element.etat = ""
                    element.hauteur = 500
                    player.marquer()
                    print(f"Score = {player.score} points")
                    print(f"Niveau = {player.level}")
                    # if player.score%10 == 0 and vaisseau.vitesse < 4:
                    #     vaisseau.vitesse +=0.2
                    if player.score%10 == 0 and player.vitesse < 7:
                        player.vitesse += 1
                    if player.score%10 == 0 and vitessetir > 10:
                        vitessetir -= 8
                        element.vitesse += 10
                    if player.score !=0 and player.score%10 == 0:
                        vaisseau.Nbennemis += 1
                        actumechant()
        # placement des objets
        # le joueur
        player.deplacer()
        # # la balle
        for element in player.groupe:
            element.bouger()
            
        
        player.groupe.draw(fenetre)        # appel de la fonction qui dessine la balle du joueur  
        
        fenetre.blit(rectangle,colide_pisto_rect)
        fenetre.blit(player.image,player.imagerect) # appel de la fonction qui dessine le vaisseau du joueur
        # les ennemis
        for ennemi in listeennemis:
            ennemi.avancer()
            fenetre.blit(colid_invader1,colid_invader1_rect)
            fenetre.blit(ennemi.image,ennemi.imagerect) # appel de la fonction qui dessine l'ennemi
            colid_invader1_rect.x, colid_invader1_rect.y = ennemi.imagerect.x, ennemi.imagerect.y
            if colid_invader1_rect.colliderect(colide_pisto_rect) or ennemi.imagerect.y > 600 and ennemi.imagerect.x < 5000:
                ennemi.disparaitre()
                expl_sound.play()
                player.hp()
                print(f"HP = {player.vie} vie")
        
        fenetre.blit(fond2,(0,0))
        fenetre.blit(player.image2,player.imagerect2)
        fenetre.blit(player.image3,player.imagerect3)

        if player.vie == 0:
            with open('sav.txt', 'r') as f: #ouvre le fichier "sav.txt" en mode lecture
                liste = f.read().splitlines() #liste reçoit les info du fichier
                if player.score > int(liste[1]): #si le score est supérieur a celui du fichier
                    sauvegarde = ['best_score', player.score] #la liste "sauvegarde" reçoit le score actuelle
                    with open('sav.txt', 'w') as f: #ouvre le fichier "sav.txt" en mode écriture
                        for item in sauvegarde:
                            f.write(f'{item}\n') #écrit le nouveau score
            score1 = player.score
            for ennemi in listeennemis:
                ennemi.replay()
            running = False
            end_menu()

        police = pygame.font.Font("zorque.otf", 25)
        pt = (f"Score : {player.score}")
        lvl = (f"Niveau : {player.level}")
        afficher = police.render(str(pt), 1, (0, 0, 0))
        afficher2 = police.render(str(lvl), 1, (0, 0, 0))
        if player.score >= 10 and player.score < 100:
            fenetre.blit(afficher, (43,547))
        elif player.score >= 100:
            fenetre.blit(afficher, (35,547))
        else:
            fenetre.blit(afficher, (47,547))
        if player.level >= 10:
            fenetre.blit(afficher2, (940,547))
        else:
            fenetre.blit(afficher2, (950,547))

        pygame.display.update() # pour ajouter tout changement à l'écran

main_menu()