#detecte la présence avec ultrason. ça va l'afficher la distence, plus c'est proche plus il va allumer les lumieres
from machine import Pin, PWM  
import time
#personne : bleu
#loin: vert
#moyenne distence: orange
#proche: rouge

ledB = Pin(17, mode=Pin.OUT) #led bleue
ledR = Pin(22, mode=Pin.OUT) #led rouge
ledO = Pin(14, mode=Pin.OUT) #led orange
ledV = Pin(10, mode=Pin.OUT) #led verte

#test pour voir si la led change bien d'etat
#ledB.toggle()
#ledR.toggle()
#ledO.toggle()
#ledV.toggle()


trigger_pin=21 # on indique le trigger pin
echo_pin=20 # on indique le echo pin
trigger=Pin(trigger_pin, Pin.OUT)
echo=Pin(echo_pin, Pin.IN)

while True: # boucle infinie
    trigger.high()
    time.sleep_us(1)
    trigger.low()
    while (echo.value()==0):
        pass #wait for echo
    lastreadtime=time.ticks_us() # record the time when signal went HIGH
    while (echo.value()==1):
        pass #wait for echo to finish
    echotime=time.ticks_us()-lastreadtime
    if echotime>37000: 
        print("Aucun obstacle détecté")
    else:
        distance = (echotime * 0.034) / 2
        print("Obstacle à {}cm".format(distance)) # dans la console on indique la distence precise
        if distance <= 10: # si l'obstacle est très proche alors on eteind tout et allume juste la led rouge
            ledV.off()
            ledR.on()
            ledO.off()
            ledB.off()
        elif distance > 10 and distance <= 30: # si l'obstacle est proche alors on eteind tout et allume juste la led orange
            ledV.off()
            ledR.off()
            ledO.on()
            ledB.off()
        elif distance > 30 and distance <= 80: # si l'obstacle est a moyenne distance alors on eteind tout et allume juste la led verte
            ledV.on()
            ledR.off()
            ledO.off()
            ledB.off()
        elif distance > 80: # si l'obstacle est loin ou qu'il n'y en a pas alors on eteind tout et allume juste la led bleue
            ledV.off()
            ledR.off()
            ledO.off()
            ledB.on()
    time.sleep(1)
