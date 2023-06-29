import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x200")

        self.song_label = tk.Label(root, text="No song selected")
        self.song_label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select Song", command=self.select_song)
        self.select_button.pack(pady=5)

        self.play_button = tk.Button(root, text="Play", state=tk.DISABLED, command=self.play_song)
        self.play_button.pack(pady=5)

        self.pause_button = tk.Button(root, text="Pause", state=tk.DISABLED, command=self.pause_song)
        self.pause_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop", state=tk.DISABLED, command=self.stop_song)
        self.stop_button.pack(pady=5)

    def select_song(self):
        song_path = filedialog.askopenfilename(title="Select Song", filetypes=(("MP3 Files", "*.mp3"),))
        if song_path:
            self.song_label.config(text=os.path.basename(song_path))
            self.play_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)
            pygame.mixer.init()
            pygame.mixer.music.load(song_path)

    def play_song(self):
        pygame.mixer.music.play()

    def pause_song(self):
        pygame.mixer.music.pause()

    def stop_song(self):
        pygame.mixer.music.stop()

root = tk.Tk()
music_player = MusicPlayer(root)
root.mainloop()
