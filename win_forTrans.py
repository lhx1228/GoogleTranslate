import sys
import tkinter
import GoogleTranslate
from tkinter import *
from tkinter import filedialog


textLyric = ''
e1 = ''

def adjust():
    #print(e1.get())
    textLyric.delete(0.0, END)  # Text清空
    trans_res = GoogleTranslate.main(e1.get())
    trans_res = '{}'.format(trans_res)
    
    textLyric.insert(END, trans_res)

def Input_songName():
    global e1
    frame = tkinter.Frame(master)
    frame.pack(side=tkinter.LEFT, fill=tkinter.Y)
    lv = tkinter.StringVar()
    listBox = tkinter.Listbox(frame, selectmode=tkinter.BROWSE,
                              width=30, height=30, bg="#FFFFFF", listvariable=lv)
    listBox.pack()
    e1 = Entry(frame, bg='#FFFFFF')
    # e1.grid()
    e1.place(x=50, y=100)
    Word = e1.get()
    #print(Word)
    tkinter.Label(master, text="输入", fg='#000000',
                  bg="#FFFFFF").place(x=10, y=98)
    Button(master, text='翻译',command=adjust).place(x=90, y=130)

def Init():
    global textLyric
    frame = tkinter.Frame(master)
    frame.pack(side=tkinter.TOP, fill=tkinter.Y)
    S = tkinter.Scrollbar(frame)
    textLyric = tkinter.Text(frame, bg="#FFFFFF", height=50)
    S.pack(side=RIGHT, fill=Y)
    textLyric.pack(side=LEFT, fill=Y)
    S.config(command=textLyric.yview)
    textLyric.config(yscrollcommand=S.set)
    adjust()
    
if __name__ == '__main__':
    master = tkinter.Tk()
    master.title('GoogleTranslate')
    master.geometry("500x300+200+100")
    Input_songName()
    Init()
    master.mainloop()
