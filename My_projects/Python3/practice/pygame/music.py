from tkinter import*
import pygame
from pygame import mixer

pygame.mixer.init()
root = Tk()
root.title("Music_0.0.1")
root.geometry("800x600")

playButton = Button(root, text = "Play", command = lambda: play_music())
playButton.place(x = 10, y = 100)
stopButton = Button(root, text = "Stop", command = lambda: play_stop())
stopButton.place(x = 80, y = 100)
def play_music():
    mixer.music.load("zene.mp3")
    mixer.music.play()

def play_stop():
    mixer.music.stop()

play_music()
play_stop()

root.mainloop()