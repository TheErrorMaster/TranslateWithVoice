from tkinter import *
from googletrans import Translator 
import googletrans
from gtts import gTTS
import os

root = Tk()
root.title("Easy Translator")

def speak(inp,la):
    optionValue = list(op.values())
    opk = list(op.keys()) #make another one or it will not work
    index1=optionValue.index(la)
    langs=opk[index1]
    talk = gTTS(text=inp, lang=langs,slow=False)
    talk.save("speak.mp3")
    os.system("afplay speak.mp3&")

def translation(lan):
    input = entry.get()
    loc = str(lan.get())
    translator = Translator(service_urls=['translate.google.com'])
    translated = translator.translate(input, dest=loc)
    speak(translated.text,loc)
    trans_output.config(text=translated.text)

op = googletrans.LANGUAGES
optionKey = list(op.values())
something = StringVar()
something.set(optionKey[21])

trans_lbl = Label(root, text="Translate English to: ")
drop = OptionMenu(root,something,*optionKey)
entry = Entry(root,width=15)
trans_btn = Button(root, text="Translate", command=lambda: translation(something))# use lambda to use arguments
trans_btn.grid(row=1, column=1)
trans_output = Label(root)

trans_lbl.grid(row=0,sticky=E)
drop.grid(row=0,column=1,sticky=W)
entry.grid(row=1, column=0)
trans_btn.grid(row=1, column=1)
trans_output.grid(row=2)

root.mainloop()