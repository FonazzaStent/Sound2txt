"""Sound to Text 1.1.2 - Convert sound files to text.
Copyright (C) 2023  Fonazza-Stent

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
#import base64
import os
import shutil
from pydub import AudioSegment
from pydub import effects
#import ffmpeg

#Create app window
def create_app_window():
        global top
        global root
        img=b'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'
        root= tk.Tk()
        top= root
        top.geometry("600x450+468+138")
        top.resizable(1,1)
        top.title("Sound to Text")
        favicon=tk.PhotoImage(data=img) 
        root.wm_iconphoto(True, favicon)

#Textbox
def create_textbox():
        global textbox
        textbox = Text(top)
        textbox.place(relx=0.033, rely=0.022, relheight=0.918, relwidth=0.933)
        scroll_1=Scrollbar (top)
        scroll_1.pack(side=RIGHT, fill=Y)
        textbox.configure(yscrollcommand=scroll_1.set)
        scroll_1.configure(command=textbox.yview)
        textbox.configure(state=DISABLED)

#Open File
def open_file():
    global soundfile
    global soundfilename
    data=[('Sound Files', '*.wav *.mp3')]
    soundfilename=askopenfilename(filetypes=data)
    if str(soundfilename)!='':
        sound = AudioSegment.from_file(soundfilename)
        sound = sound.set_frame_rate(8000)
        #sound=sound.set_sample_width(1)
        #sound=effects.normalize(sound)
        sound.export("tempsoundfile.pcm", format="u8")
        soundfile=open("tempsoundfile.pcm",'rb')
        encode()

#encode
def encode():
    global soundtext
    global tempfile
    tempfile=open("tempfile",'w')
    soundtext=''
    soundtext2=''
    soundfile.seek(44)
    filename=str(soundfilename)
    soundfile_size= os.path.getsize("tempsoundfile.pcm")
    step=int(soundfile_size/1200)
    for chars in range (1,soundfile_size,step):
        #print (chars)
        soundfile.seek(chars)
        bytea=soundfile.read(1)
        #print (chars,bytea)
        bytevalue=int.from_bytes(bytea, "big")
        if bytevalue>=127:
            char=chr(int((bytevalue-127)/5.08)+97)
        else:
            char=chr(int((127-bytevalue)/5.08)+97)
        char2=chr(int(bytevalue/9)+97)
        soundtext=soundtext+char
        soundtext2=soundtext2+char2
    textbox.configure(state=NORMAL)
    textbox.delete(1.0,END)
    textbox.insert(INSERT,"Algorithm 1 - Straight text\n\n")
    textbox.insert(INSERT,soundtext[0:20000])
    tempfile.write("Algorithm 1 - Straight text\n\n")
    tempfile.write(soundtext)
    tempfile.write('\n\n')
    soundtext=soundtext[::-1]
    textbox.insert(INSERT,"\n\n")
    textbox.insert(INSERT,"Algorithm 1 - Reverse text\n\n")
    textbox.insert(INSERT,soundtext[0:20000])
    tempfile.write("Algorithm 1 - Reverse text\n\n")
    tempfile.write(soundtext)
    tempfile.write('\n\n')
    textbox.insert(INSERT,"\n\n")
    textbox.insert(INSERT,"Algorithm 2 - Straight text\n\n")
    textbox.insert(INSERT,soundtext2[0:20000])
    tempfile.write("Algorithm 2 - Straight text\n\n")
    tempfile.write(soundtext2)
    tempfile.write('\n\n')
    soundtext2=soundtext2[::-1]
    textbox.insert(INSERT,"\n\n")
    textbox.insert(INSERT,"Algorithm 2 - Reverse text\n\n")
    textbox.insert(INSERT,soundtext2[0:20000])
    tempfile.write("Algorithm 2 - Reverse text\n\n")
    tempfile.write(soundtext2)
    textbox.configure(state=DISABLED)
    tempfile.close()
    soundfile.close()
    os.remove("tempsoundfile.pcm")

#Copy Code
def copy_text():
    textbox.tag_add(SEL, "1.0", END)
    textbox.event_generate(("<<Copy>>"))

#Save to file
def Save_to_file():
        data=[('Text','*.txt')]
        reportfile=asksaveasfilename(filetypes=data, defaultextension=data)
        if str(reportfile)!='':
            shutil.copy("tempfile",reportfile)

#Quit
def QuitApp():
    okcancel= messagebox.askokcancel("Quit?","Do you want to quit the app?",default="ok")
    if okcancel== True:
        os.remove("tempfile")
        top.destroy()

#menu
def create_menu():
    menubar=tk.Menu(top, tearoff=0)
    top.configure(menu=menubar)
    sub_menu=tk.Menu(top, tearoff=0)
    menubar.add_cascade(menu=sub_menu,compound="left", label="File")
    sub_menu.add_command(compound="left", label="Open", command=open_file, accelerator="Alt+O")
    sub_menu.add_command(compound="left",label="Copy", command=copy_text, accelerator="Alt+C")
    sub_menu.add_command(compound="left",label="Save", command=Save_to_file,accelerator="Alt+S")
    sub_menu.add_command(compound="left",label="Quit", command=QuitApp, accelerator="Alt+Q")
    top.bind_all("<Alt-o>",open_file_hotkey)
    top.bind_all("<Alt-c>",copy_hotkey)
    top.bind_all("<Alt-s>",Save_hotkey)
    top.bind_all("<Alt-q>",Quit_hotkey)
    menubar.bind_all("<Alt-f>",menubar.invoke(1))

def open_file_hotkey(event):
    open_file()

def copy_hotkey(event):
    copy_text()

def Save_hotkey(event):
    Save_to_file()

def Quit_hotkey (event):
    QuitApp()

#contextmenu
def context_menu(event):
        try:
                menucopy.tk_popup(event.x_root, event.y_root)
        finally:
                menucopy.grab_release()
def create_context_menu():
        global menucopy
        root.bind("<Button-3>", context_menu)
        menucopy = Menu(root, tearoff = 0)
        menucopy.add_command(label="Copy", command=copy_text)

#main procedure
def main():
    create_app_window()
    create_textbox()
    create_menu()
    create_context_menu()


main()
root.mainloop()
