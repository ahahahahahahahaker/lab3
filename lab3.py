from tkinter import *
import random

window = Tk()
window.geometry('1400x1000')
alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def generate_key(number):

    digits = [int(d) for d in str(number)]

    block_digits1 = random.sample(digits[3:], 3)
    block3_1 = int(str(block_digits1[0]) + str(block_digits1[1]) + str(block_digits1[2]))

    block_digits2 = random.sample(digits[:3], 3)
    block3_2 = int(str(block_digits2[0]) + str(block_digits2[1]) + str(block_digits2[2]))

    block_letters1 = random.sample(alfabet, 3)

    block_letters2 = random.sample(alfabet, 3)

    block3 = block3_1 + block3_2

    return f"{ ''.join(map(str, block_digits1 + block_letters1)) }-\
{ ''.join(map(str, block_digits2 + block_letters2)) } { block3 }"


def clicked():
    number = txt.get()
    key = generate_key(number)
    lbl_key = Label(window, text='Ваш ключ: ' + key, font=("Arial Bold", 20))
    lbl_key.grid(column=1, row=3, padx=30, pady=0)


image_ = PhotoImage(file='wall.png')
bg_label = Label(window, image=image_)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

lbl = Label(window, text='Введите 6-значное число:', font=("Times New Roman", 20))
lbl.grid(column=1, row=0, padx=30, pady=30)
txt = Entry(window, width=3, font=("Times New Roman", 20))
txt.focus()
txt.grid(column=2, row=0, padx=0, pady=30)
btn = Button(window, text="ПИП!", font=("Times New Roman", 20), command=clicked)
btn.grid(column=3, row=0, padx=30, pady=30)
txt = Entry(window, width=3, font=("Times New Roman", 20))
txt.focus()
txt.grid(column=2, row=0, padx=0, pady=30)
window.mainloop()
