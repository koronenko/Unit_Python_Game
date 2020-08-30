from tkinter import *

tk = Tk()  #создаем обьект Tk
tk.title("Dragon & Knight")    #выводим название игры
tk.resizable(0, 0)     #задаем фиксированый размер окна
tk.wm_attributes("-topmost", 1)    #размещаем окно поверх всех окон
canvas = Canvas(tk, width=500, height=833, highlightthickness=0)  # создаем холст со свойствами высоты и ширины, без рамки
canvas.pack()          #
bg = PhotoImage(file="Backgraund.gif")
canvas.create_image(0, 0, anchor='nw', image=bg)      # получаем отступ от левого края и отступ от верхнего края, выводизображение в этой позиции
        
