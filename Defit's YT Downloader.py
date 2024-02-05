# Required modules: 
# pip install tk
# pip install pytube
# pip install ttkthemes

# Libraries used
from tkinter import *
from pytube import YouTube
from ttkthemes import ThemedTk

# Display Window Setup
root = ThemedTk(theme="arc-dark")
root.geometry('500x300')
root.resizable(0,0)
root.title("Defit's Video Downloader")
# ThemedTk(): Used to initialize tkinter to create display window
# root.geometry(): Used to set the window’s width and height
# root.resizable: Set the fix size of window
# root.title(): Sets the title for the window

Label(root,text = 'YT Video Downloader', font ='arial 20').pack()
# Label(): Widget use to display text that users can’t able to modify
# root: The name of the window
# text: Text which is displayed on widget
# font: Font for the text
# pack: organized widget in block

# "Enter Link" Field
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15').place(x= 28 , y = 80)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 110)
# link: A string type variable that stores the youtube video link that the user enters
# Entry(): Widget used when we want to create an input text field
# width: Width of the entry box
# textvariable: Binds the text variable to the entry box so it displays what the user types into the box
# place(): Ues to place the widget at a specific position

# Create Function to Start Downloading
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'Video successfully downloaded!\n Check in the executable folder', font = 'arial 15').place(x= 110 , y = 210)  

Button(root, text='Download video', font='arial 15 bold', bg='#444444', fg='white', padx=2, command=Downloader).place(x=160, y=150)
root.mainloop()
# Button(): Widget used to display buttons on the window
# text: Text which we display on the label
# font: Font in which the text is written
# bg: Background color
# command: used to call the function
# root.mainloop(): method that executes when we want to run the program

# Created by DefeatOf13, please visit defeatof13.github.io