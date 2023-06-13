import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x650")
canvas.config(bg='black')

rootpath = "C:\\Users\\acer\\OneDrive\\Desktop\\music"
pattern = "*.mp3"

mixer.init()

def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(os.path.join(rootpath, listBox.get("anchor")))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1 if next_song else 0
    next_song_name = listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(os.path.join(rootpath, next_song_name))
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def play_prev():
    prev_song = listBox.curselection()
    prev_song = prev_song[0] - 1 if prev_song else listBox.size() - 1
    prev_song_name = listBox.get(prev_song)
    label.config(text=prev_song_name)

    mixer.music.load(os.path.join(rootpath, prev_song_name))
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(prev_song)
    listBox.select_set(prev_song)

def pause_song():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"

listBox = tk.Listbox(canvas, fg="cyan", bg="black", width=80, font=('poppins', 18))
listBox.pack(padx=15, pady=15)

label = tk.Label(canvas, text='', bg='black', fg='red', font=('poppins', 20))
label.pack(pady=15)

top = tk.Frame(canvas, bg="black")
top.pack(padx=10, pady=5, anchor='center')

prevButton = tk.Button(top, text="Prev", command=play_prev)
prevButton.pack(pady=15, side='left')

stopButton = tk.Button(top, text="Stop", command=stop)
stopButton.pack(pady=15, side='left')

playButton = tk.Button(top, text="Play", command=select)
playButton.pack(pady=15, side='left')

pauseButton = tk.Button(top, text="Pause", command=pause_song)
pauseButton.pack(pady=15, side='left')

nextButton = tk.Button(top, text="Next", command=play_next)
nextButton.pack(pady=15, side='left')

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

canvas.mainloop()
