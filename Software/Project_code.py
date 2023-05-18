import pygame
import numpy as np

def play_song(number_str):
    pygame.mixer.music.load('songs/' + number_str + '.mp3')
    pygame.mixer.music.play()

def my_playlist():
    pygame.mixer.init()

    my_list = []
    while True:
        if len(my_list)==20:
            my_list=[]
        number = np.random.randint(1, 21)
        if number not in my_list:
            my_list.append(number)
            number_str = str(number)
            print(f"Now playing: {number_str}.mp3")

            # Start playing the song
            play_song(number_str)

            while pygame.mixer.music.get_busy():
                response = input("Do you want to skip this song? (yes/no): ")
                if response.lower() == "yes":
                    pygame.mixer.music.stop()
                    break
                else:
                    pass
            response = input("Do you want to stop the playlist? (yes/no): ")
            if response.lower() == "yes":
                pygame.mixer.music.stop()
                pygame.mixer.quit()
                return

    pygame.mixer.quit()

for times in range(0, 5):
    my_playlist()