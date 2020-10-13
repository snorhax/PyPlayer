import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer


class MusicPlayer:
    window = None

    def __init__(self, window):
        self.window = window
        window.geometry('320x100')
        window.title('Little Music Player')
        window.resizable(0, 0)
        Load = Button(window, text='Load', width=10, font=('Times', 10), command=self.load)
        Play = Button(window, text='Play', width=10, font=('Times', 10), command=self.play)
        Pause = Button(window, text='Pause', width=10, font=('Times', 10), command=self.pause)
        Stop = Button(window, text='Stop', width=10, font=('Times', 10), command=self.stop)
        Load.place(x=0, y=20)
        Play.place(x=110, y=20)
        Pause.place(x=220, y=20)
        Stop.place(x=110, y=60)
        self.music_file = None
        self.playing_state = False

    def load(self):
        path_string = filedialog.askopenfilename()
        if os.path.isfile(path_string):
            print('Path knows that it\'s a path')
            self.music_file = path_string
            self.window.title = os.path.basename(path_string)  # not reflecting in gui for some reason
            print('Window title is now:', self.window.title)

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
