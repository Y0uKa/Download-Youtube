from os import path
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil


#functions
def select_path():
    #allows user to select a path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget('text')
    screen.title('Downloading..')
    #download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #move files to selected directory
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete! Download Another Files...')

screen = Tk()
title = screen.title('YouLoad')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()


#image logo
logo_img = PhotoImage(file='Logo.png')
#resize
logo_img = logo_img.subsample(1, 1)
canvas.create_image(250, 80, image=logo_img)

#link filed
link_field = Entry(screen, width=50)
link_label = Label(screen, text='Give me this Link : ', font=('Arial', 15))

#by Y0uKA (1)
path_label = Label(screen, text= 'By Y0uKa#0949', font=('Arial', 10) )
select_btn = Button(screen, text='By Y0uKa#0949',)
#by Y0uKa (2)
canvas.create_window(450, 490, window=path_label)



#Select path for saving the files
path_label = Label(screen, text= 'Select Path For Download', font=('Arial', 15) )
select_btn = Button(screen, text='Select', command=select_path)
#add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

#add widgets tp window
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

#Download btns
download_btn = Button(screen, text='Download File', command=download_file)
#add to canvas
canvas.create_window(250, 390, window=download_btn)

screen.mainloop()