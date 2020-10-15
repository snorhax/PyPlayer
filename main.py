import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer


class MusicPlayer:
    """Little Music Player"""
    def __init__(self, window):
        window.title('Little Music Player')
        window.geometry('320x150')
        window.resizable(0, 0)
        Load = Button(window, text='Load', width=10, font=('Times', 10), command=self.load)
        Play = Button(window, text='Play', width=10, font=('Times', 10), command=self.play)
        Pause = Button(window, text='Pause', width=10, font=('Times', 10), command=self.pause)
        Stop = Button(window, text='Stop', width=10, font=('Times', 10), command=self.stop)
        self.music_file = None
        self.SongLabel = Label(window, text=self.music_file)
        Load.place(x=15, y=20)
        Play.place(x=110, y=20)
        Pause.place(x=220, y=20)
        Stop.place(x=110, y=60)
        self.SongLabel.place(x=110, y=100)
        self.playing_state = False
        self.music_window = window

    def load(self):
        path_string = filedialog.askopenfilename()
        if os.path.isfile(path_string):
            self.music_file = path_string
            self.SongLabel['text'] = os.path.basename(path_string)

    def play(self):
        if os.path.isfile(self.music_file):
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
        else:
            print('File does not exist.')

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False

    def stop(self):
        mixer.music.stop()


root = Tk()
app = MusicPlayer(root)
root.mainloop()
