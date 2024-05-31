import network   
import urequests 
import utime     
import ujson     
from machine import Pin, PWM  
import random   


wlan = network.WLAN(network.STA_IF) 
wlan.active(True) 

#ssid = 'iPhone (7)'
#password = 'Pooky123'

#ssid = 'Sirius'
#password = 'chartres528'
ssid = 'Pixel_7deLivia'
password = 'Marionchou'
wlan.connect(ssid, password) 
url = "https://hp-api.lainocs.fr/characters"


pwm_ledR = PWM(Pin(17, mode=Pin.OUT)) #led rouge
pwm_ledR.freq(1000) 

pwm_ledV = PWM(Pin(18, mode=Pin.OUT)) #led verte
pwm_ledV.freq(1000) 

pwm_ledB = PWM(Pin(19, mode=Pin.OUT)) #led bleue
pwm_ledB.freq(1000) 


#dico contenant les maisons avec leurs couleurs
houses = {"Gryffindor":[15000,1000,1000], #rouge
          "Slytherin":[1000, 15000, 1000], #vert
          "Hufflepuff":(int((227*15000)/255), 5000, 1000), #jaune
          "Ravenclaw":(int((30*15000)/255), int((144*15000)/255), 15000), #bleu
          "":[15000,15000,15000]} # blanc = par defaut ou rien (pour ceux qui n'ont pas de maison)


while not wlan.isconnected():
    print("pas co") # si le Raspberry n'arrive pas à se connecter
    utime.sleep(1)
    pass

while(True): #boucle infinie
    try:
        characNum = random.randint(1, 30) #aleatoire entre 1 et 30 ==> permet de choisir un personnage au hasard
        print("GET") #verifie si on est bien connecte
        print(characNum) # affiche le numero du personnage (verification)
        r = urequests.get(url) # lance une requete sur l'url
        print(r.json()) # traite sa reponse en Json
        
        maison = r.json()[characNum]["house"] #recupere la maison
        nom = r.json()[characNum]["name"] # recupere le nom du personnage
        
        print(nom) #doit afficher le nom du personnage
        print(maison) #doit afficher le nom de la maison
        
        pwm_ledR.duty_u16(houses[maison][0]) #s'occupe de l'intensite de la led rouge
        pwm_ledB.duty_u16(houses[maison][2]) #s'occupe de l'intensite de la led bleue
        pwm_ledV.duty_u16(houses[maison][1]) #s'occupe de l'intensite de la led verte
        
        
        r.close() # ferme la demande
        utime.sleep(2)  #attend deux secondes avant de recommancer
    except Exception as e:
        print(e)
        