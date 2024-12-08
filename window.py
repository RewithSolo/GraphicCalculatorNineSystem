import tkinter as ttk
from tkinter import font
import tkinter.messagebox as mb
from logic import *



def clear():
    entry.delete(0, len(entry.get()))


def back_space():
    entry.delete(len(entry.get()) - 1)


def typing(text):
    entry.insert(len(entry.get()), text)


def show_info():
     msg = "Программа считает сумму и разность чисел в 9-ной системе счисления.\n " \
           "Ввод выражений с помощью клавиатуры и графического меню. Удаление символов из строки и очистка строки.\n" \
           "Автор Соловьев Иван ИУ7-22Б.\n =)"
     mb.showinfo("Информация о приложении", msg)


def res():
    text = entry.get()
    text = text.replace(" ", "")
    if "-" in text:
        text = text.replace("-", " ")
        txt = text.split(" ")
        result = minus(txt[0], txt[1])
        clear()
        typing(result)
    elif "+" in text:
        text = text.replace("+", " ")
        txt = text.split(" ")
        result = plus(txt[0], txt[1])
        clear()
        typing(result)


root = ttk.Tk()
root.title("Calc N1N3!")
root.geometry("328x430")
root.config(bg="#faf6f5")
root.iconbitmap('nine.ico')
entr = ttk.Frame(root, bg="#262626")
entr.pack()
frame = ttk.Frame(root)
frame.pack()
fonty = font.Font(family= "Arial", size=30, weight="bold", slant="roman", underline=False, overstrike=False)
entry = ttk.Entry(entr, width = 50, font=fonty, bg="#61B4CF", fg="#262626")
entry.pack(padx=8, pady= 8, ipady = 6)
ttk.Button(frame, text="1", height = 5, width=10, command=lambda: typing("1"), bg="#803939", fg="#f5f5f5", highlightbackground="#37d3ff", highlightcolor="#37d3ff", highlightthickness=4, bd=0).grid(column=0, row=0)
ttk.Button(frame, text="2", height = 5, width=10, command=lambda: typing("2"), bg="#803939", fg="#f5f5f5", highlightbackground="#37d3ff", highlightcolor="#37d3ff", highlightthickness=4, bd=0).grid(column=1, row=0)
ttk.Button(frame, text="3", height = 5, width=10, command=lambda: typing("3"), bg="#803939", fg="#f5f5f5", highlightbackground="#37d3ff", highlightcolor="#37d3ff", highlightthickness=4, bd=0).grid(column=2, row=0)
ttk.Button(frame, text="4", height = 5, width=10, command=lambda: typing("4"), bg="#803939", fg="#f5f5f5", highlightbackground="#37d3ff", highlightcolor="#37d3ff", highlightthickness=4, bd=0).grid(column=0, row=1)
ttk.Button(frame, text="5", height = 5, width=10, command=lambda: typing("5"), bg="#803939", fg="#f5f5f5", highlightbackground="#37d3ff", highlightcolor="#37d3ff", highlightthickness=4, bd=0).grid(column=1, row=1)
ttk.Button(frame, text="6", height = 5, width=10, command=lambda: typing("6"), bg="#803939", fg="#f5f5f5", highlightbackground="#37d3ff", highlightcolor="#37d3ff", highlightthickness=4, bd=0).grid(column=2, row=1)
ttk.Button(frame, text="7", height = 5, width=10, command=lambda: typing("7"), bg="#803939", fg="#f5f5f5", highlightbackground="#37d3ff", highlightcolor="#37d3ff", highlightthickness=4, bd=0).grid(column=0, row=2)
ttk.Button(frame, text="8", height = 5, width=10, command=lambda: typing("8"), bg="#803939", fg="#f5f5f5", highlightbackground="#37d3ff", highlightcolor="#37d3ff", highlightthickness=4, bd=0).grid(column=1, row=2)
ttk.Button(frame, text="point", height = 5, width=10, command=lambda: typing("."), bg="#803939", fg="#f5f5f5", highlightbackground="#37d3ff", highlightcolor="#37d3ff", highlightthickness=4, bd=0).grid(column=2, row=2)
ttk.Button(frame, text="0", height = 5, width=10, command=lambda: typing("0"), bg="#803939", fg="#f5f5f5", highlightbackground="#37d3ff", highlightcolor="#37d3ff", highlightthickness=4, bd=0).grid(column=1, row=3)
ttk.Button(frame, text="+", height = 5, width=10, command=lambda: typing("+"), bg="#61B4CF", fg="#262626", highlightbackground="#37d3ff", highlightcolor="#37d3ff", highlightthickness=4, bd=0).grid(column=3, row=0)
ttk.Button(frame, text="-", height = 5, width=10, command=lambda: typing("-"), bg="#61B4CF", fg="#262626", highlightbackground="#37d3ff", highlightcolor="#37d3ff", highlightthickness=4, bd=0).grid(column=3, row=1)
ttk.Button(frame, text="info", height = 5, width=10, bg="#262626",  command=show_info, fg="#61B4CF", highlightbackground="#37d3ff", highlightcolor="#37d3ff", highlightthickness=4, bd=0).grid(column=0, row=3)
ttk.Button(frame, text="C", height = 5, width=10, command=clear, bg="#262626", fg="#FF5D40", highlightbackground="#37d3ff", highlightcolor="#37d3ff", highlightthickness=4, bd=0).grid(column=2, row=3)
ttk.Button(frame, text="=", height = 5, width=10, bg="#262626", fg="#FF5D40", command=res, highlightbackground="#37d3ff", highlightcolor="#37d3ff", highlightthickness=4, bd=0).grid(column=3, row=3)
ttk.Button(frame, text="<-", height = 5, width=10, command=back_space, bg="#262626", fg="#FF5D40", highlightbackground="#37d3ff", highlightcolor="#37d3ff", highlightthickness=4, bd=0).grid(column=3, row=2)
root.mainloop()
