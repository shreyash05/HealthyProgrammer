import pygame
from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}")

if __name__ == '__main__':
    #
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersec = 5
    exsec = 5
    eyessec = 5

    while True:
        if time() - init_water > watersec:
            print("Water drinking time.enter '1' to close reminder :")
            musiconloop('water_tone.mp3', '1')
            init_water = time()
            log_now("Drank water at:\n")
        if time() - init_eyes > eyessec:
            print("Eye exercise time. Enter '2' to close reminder : ")
            musiconloop('eyes.mp3', '2')
            init_eyes = time()
            log_now("Eyes relaxed at at:\n")

        if time() - init_exercise > exsec:
            print("Physical activity time.enter '3' to close reminder :")
            musiconloop('exercise.mp3', '3')
            init_exercise = time()
            log_now("Physical Activity done at\n:")
        print("Enter 'e' for exit or press 'ENTER' button for continue:")
        a=input()

        if a=='e' :
            mixer.music.stop()
            break