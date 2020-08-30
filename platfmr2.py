from tkinter import *
import random
import time

class Game:
    def __init__(self):     #функция инициализации. Аргумент Self дает функции класса возможность вызывать другие функции этого класса и его предков
        self.tk = Tk()  #создаем обьект Tk
        self.tk.title("Dragon & Knight")    #выводим название игры
        self.tk.resizable(0, 0)     #задаем фиксированый размер окна
        self.tk.wm_attributes("-topmost", 1)    #размещаем окно поверх всех окон
        self.canvas = Canvas(self.tk, width=500, height=833, highlightthickness=0)  # создаем холст со свойствами высоты и ширины, без рамки
        self.canvas.pack()          #
        self.tk.update()            #
        self.canvas_height = 833    # задаем высоту
        self.canvas_width = 500     # задаем ширину
        self.bg = PhotoImage(file="Backgraund.gif")     # загрузка и отображение фонового рисунка
        #w = self.bg.width()     # сохраняем размер изображения
       # h = self.bg.height()    # сохраняем размер изображения
       # for x in range(0, 5):   # заполняем холст изображением х 5 по х
        #    for y in range(0, 5):   # заполняем холст изображением х 5 по у
        #self.canvas.create_image(x * w, y * h, image=self.bg, anchor='nw')      # получаем отступ от левого края и отступ от верхнего края, выводизображение в этой позиции
        self.canvas.create_image(0, 0, image=self.bg, anchor='nw')
        self.sprites = []   # пустой список спрайтов
        self.running = True     #
        self.game_over_text = self.canvas.create_text(250, 250, text='ПЕРЕМОГА!', state='hidden')   #

    def mainloop(self):     # управление игровой анимацией
        while 1:       # главный цыкл работает до закрытия окна игры
            if self.running == True:    # проверяем свойство
           #if self.running:
                for sprite in self.sprites:     # перебираем в цыкле все спрайты
                    sprite.move()   # вызываем для спрайтов функцию move
            else:
                time.sleep(1)   # 
                self.canvas.itemconfig(self.game_over_text, state='normal') #
            self.tk.update_idletasks()  # принудительная перерисовка єкрана
            self.tk.update()    #
            time.sleep(0.01)    # пауза десятую долю секунды

class Coords:   # Класс для размещения спрайтов на экране, здесь хранятся позиции всех графических элементов в игре
    def __init__(self, x1=0, y1=0, x2=0, y2=0):     #
        self.x1 = x1    #
        self.y1 = y1    #
        self.x2 = x2    #
        self.y2 = y2    #

#def within_x(co1, co2):     # пересечение по горизонталт х1 и х2
#    if co1.x1 > co2.x1 and co1.x1 < co2.x2:
#        return True #
#    elif co1.x2 > co2.x1 and co1.x2 < co2.x2:
#        return True #
#    elif co2.x1 > co1.x1 and co2.x1 < co1.x2:
#        return True   #
#    elif co2.x2 > co1.x1 and co2.x2 < co1.x1:
#        return True     #
#    else:   #
#        return False    #

def within_x(co1, co2):
    if (co1.x1 > co2.x1 and co1.x1 < co2.x2) \
            or (co1.x2 > co2.x1 and co1.x2 < co2.x2) \
            or (co2.x1 > co1.x1 and co2.x1 < co1.x2) \
            or (co2.x2 > co1.x1 and co2.x2 < co1.x1):
        return True
    else:
        return False

#def within_y(co1, co2):     # пересечение по вертикали у1 и у2
#    if co1.y1 > co2.y1 and co1.y1 < co2.y2:
#        return True
#    elif co1.y2 > co2.y1 and co1.y2 < co2.y2:
#        return True
#    elif co2.y1 > co1.y1 and co2.y1 < co1.y2:
#        return True
#    elif co2.y2 > co1.y1 and co2.y2 < co1.y1:   #
#        return True     #
#    else:   #
#        return False    #

def within_y(co1, co2):
    if (co1.y1 > co2.y1 and co1.y1 < co2.y2) \
            or (co1.y2 > co2.y1 and co1.y2 < co2.y2) \
            or (co2.y1 > co1.y1 and co2.y1 < co1.y2) \
            or (co2.y2 > co1.y1 and co2.y2 < co1.y1):
        return True
    else:
        return False

def collided_left(co1, co2):    # столкновение спрайтов слева
    if within_y(co1, co2):      #
        if co1.x1 <= co2.x2 and co1.x1 >= co2.x1:   #
            return True     #
    return False    #

def collided_right(co1, co2):   # столкновение спрайтов справа
    if within_y(co1, co2):  #
        if co1.x2 >= co2.x1 and co1.x2 <= co2.x2:   #
            return True     #
    return False    #

def collided_top(co1, co2):     # столкновение спрайтов сверху
    if within_x(co1, co2):      #
        if co1.y1 <= co2.y2 and co1.y1 >= co2.y1:   #
            return True     #
    return False    #

def collided_bottom(y, co1, co2):   # столкновение спрайтов снизу
    if within_x(co1, co2):  #
        y_calc = co1.y2 + y     #
        if y_calc >= co2.y1 and y_calc <= co2.y2:   #
            return True     #
    return False    #

class Sprite:   # клас спрайтов нужен чтобі каждій спрайт имелдоступ к списку остальніх спрайтов в игре
    def __init__(self, game):   #
        self.game = game    #
        self.endgame = False    # свойство сигнализирующее об окончании игры
        self.coordinates = None
        #
    def move(self):     # перемещение спрайта
        pass    #
    def coords(self):   # возвращение текущей позиции на игровом єкране
        return self.coordinates     #

class PlatformSprite(Sprite):   #
    def __init__(self, game, photo_image, x, y, width, height):     #
        Sprite.__init__(self, game)     #
        self.photo_image = photo_image      #
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor='nw')    #
        self.coordinates = Coords(x, y, x + width, y + height)  #
 
class MovingPlatformSprite(PlatformSprite):     #
    def __init__(self, game, photo_image, x, y, width, height):     #
         PlatformSprite.__init__(self, game, photo_image, x, y, width, height)   #
         self.x = 2      #
         self.counter = 0    #
         self.last_time = time.time()    #
         self.width = width      #
         self.height = height    #

    def coords(self):   #
        xy = self.game.canvas.coords(self.image)    #
        self.coordinates.x1 = xy[0]     #
        self.coordinates.y1 = xy[1]     #
        self.coordinates.x2 = xy[0] + self.width    #
        self.coordinates.y2 = xy[1] + self.height   #
        return self.coordinates     #

    def move(self):
        if time.time() - self.last_time > 0.03:     #
            self.last_time = time.time()    #
            self.game.canvas.move(self.image, self.x, 0)    #
            self.counter += 1   #
            if self.counter > 20:   #
                self.x *= -1    #
                self.counter = 0    #

class CastleSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):  #
        Sprite.__init__(self, game)     #
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor='nw')
        self.coordinates = Coords(x, y, x + (width / 2), y + height)
        self.endgame = True
        self.closed_Castle = PhotoImage(file="Castle.gif")     #
        self.open_Castle = PhotoImage(file="CastleDragon.gif")   #
        self.image = game.canvas.create_image(x, y, image=self.closed_Castle, anchor='nw')    #
        self.coordinates = Coords(x, y, x + (width / 2), y + height)    #
        self.endgame = True     #

    def openCastle(self):     #
         self.game.canvas.itemconfig(self.image, image=self.open_Castle)   #
         self.game.tk.update_idletasks()     #

    def closeCastle(self):    #
         self.game.canvas.itemconfig(self.image, image=self.closed_Castle)     #
         self.game.tk.update_idletasks()

class StickFigureSprite(Sprite):    # анимация изображения героя
    def __init__(self, game):   #
        Sprite.__init__(self, game)     #
        self.images_left = [PhotoImage(file="figure-L1.gif"), PhotoImage(file="figure-L2.gif"), PhotoImage(file="figure-L3.gif")]
        self.images_right = [PhotoImage(file="figure-R1.gif"), PhotoImage(file="figure-R2.gif"), PhotoImage(file="figure-R3.gif")    #
        ]
        self.image = game.canvas.create_image(250, 600, image=self.images_left[0], anchor='nw') #
        self.x = 0     # величині на которіе смещаем фигурку по горизонтали, при старте фигурка сдвинется влево
        self.y = 0      # по вертикали
        self.current_image = 0  # индекс текущего изображения
        self.current_image_add = 1      # число которое нужно прибавить к индексу чтобі біла анимация
        self.jump_count = 0     # счетчик пріжков
        self.last_time = time.time()    # последняя смена кадров фигуры
        self.coordinates = Coords()     #
        game.canvas.bind_all('<KeyPress-Left>', self.turn_left)     # привязка к нажатию клавишь
        game.canvas.bind_all('<KeyPress-Right>', self.turn_right)   #
        game.canvas.bind_all('<KeyPress-Up>', self.jump)   #

    def turn_left(self, evt):   # evt  обьект событие
        if self.y == 0:     # 
            self.x = -1     #

    def turn_right(self, evt):      #
        if self.y == 0:     #
            self.x = 1      #

    def jump(self, evt):    #
        if self.y == 0:     # чтобы в прыжке нельзя было прыгнуть еще раз проверяем в прыжке ли мы и не падаем ли
            self.y = -5     # движение вверх
            self.jump_count = 0     # счетчик ограничения длительности прыжка,обнукляем

    def animate(self):
        if self.x != 0 and self.y == 0:     # проверяем движется ли фигурка х, у фигурка не падает и не в прыжке
            if time.time() - self.last_time > 0.1:  # смена кадров изображения от предыдущего вызова функции
                self.last_time = time.time()    # сбрасываем таймер если время превышает
                self.current_image += self.current_image_add    # добавляем индекс изображения изначально равен 1
                if self.current_image >= 2:     #
                    self.current_image_add = -1     #
                if self.current_image <= 0:     #
                    self.current_image_add = 1      #
        if self.x < 0:  # сиена кадров: если фигурка движется влево 
            if self.y != 0:     # проверяем в прыжке или падает фигурка
                self.game.canvas.itemconfig(self.image, image=self.images_left[2])  # меняем изображение фигурки
            else:   #
                self.game.canvas.itemconfig(self.image, image=self.images_left[self.current_image])     #
        elif self.x > 0:    # идентично левой части
            if self.y != 0:     #
                self.game.canvas.itemconfig(self.image, image=self.images_right[2])     #
            else:   #
                self.game.canvas.itemconfig(self.image, image=self.images_right[self.current_image])    #

    def coords(self):   #
        xy = self.game.canvas.coords(self.image)    # обьект холст, возвращает координаты изображения(идентификатор изображения - аргумент)
        self.coordinates.x1 = xy[0]     # координаты верхнего левого угла изображения
        self.coordinates.y1 = xy[1]     #
        self.coordinates.x2 = xy[0] + 124    # размер фигурки прибавляем для вычисления координат
        self.coordinates.y2 = xy[1] + 110    #
        return self.coordinates     #

    def move(self):     #
        self.animate()      #
        if self.y < 0:      # проверка в прыжке ли фигурка, отрицательное значение соответставует движению вверх
            self.jump_count += 1    # увеличиваем счетчик
            if self.jump_count > 20:    #проверяем не большели прыжок 
                self.y = 4      # организовываем падение
        if self.y > 0:      #
            self.jump_count -= 1    # уменьшаем счетчик
        co = self.coords()  #
        left = True     # переменные для проверки на столкновение
        right = True       #
        top = True      #
        bottom = True   #
        falling = True  #
        if self.y > 0 and co.y2 >= self.game.canvas_height:     # высота фигурки сравнивается с высотой холста
            self.y = 0      # останавливаем падение
            bottom = False      #
        elif self.y < 0 and co.y1 <= 0:     # проверяем столкновение с верхней границей холста
            self.y = 0      # останавливаем движение ввенрх
            top = False     #
        if self.x > 0 and co.x2 >= self.game.canvas_width:      # проверяем на столкновение с правой стороной
            self.x = 0      # останавливаем горизонтальное движение
            right = False   #
        elif self.x < 0 and co.x1 <= 0:     # проверяем на столкновение с левой стороной
            self.x = 0      #  останавливаем горизонтальное движение
            left = False    #
        for sprite in self.game.sprites:    # столкновение со спрайтами
            if sprite == self:      # перебираем список спрайтов, сравнение с самим собой не нужно делать
                continue    # продолжаем
            sprite_co = sprite.coords()     # получаем координаты спрайта и проверяем условия столкновения
            if top and self.y < 0 and collided_top(co, sprite_co):      # равна ли переменная истине, в прыжке ли фигурка, столкновение со спрайтом
                self.y = -self.y    # меняем значение чтобы фигурка начала падать
                top = False     #
            if bottom and self.y > 0 and collided_bottom(self.y, co, sprite_co):    # равна ли переменная истине, падает ли фигурка, столкнулась ли она со спрайтом нижней стороной
                self.y = sprite_co.y1 - co.y2   # разница между верхней у-координатой спрайта и нижней координатой фигурки у
                if self.y < 0:  # проверяем не отрицательное ли число чтобы фигурка не начала подыматься
                    self.y = 0      # если получилосьобнуляем
                bottom = False      #
                top = False     #
            if bottom and falling and self.y == 0 and co.y2 < self.game.canvas_height and collided_bottom(1, co, sprite_co): #падение с платформы: две переменные истина, фигурка не падает, низ фигурки соприкасантся с платформой
                falling = False     #
            if left and self.x < 0 and collided_left(co, sprite_co):    # столкновение с левой границей: движется ли фигурка влево, столкнуласьли левой стороной со спрайтом
                self.x = 0  # останавливаем фигурку
                left = False    #
                if sprite.endgame:  #
                    self.game.running = False
                    self.end(sprite)    #
            if right and self.x > 0 and collided_right(co, sprite_co):      # столкновение с правой границей
                self.x = 0      #
                right = False   #
                if sprite.endgame:  #
                    self.game.running = False
                    self.end(sprite)    #
            if falling and bottom and self.y == 0 and co.y2 < self.game.canvas_height:      # падение
                self.y = 4      #
            self.game.canvas.move(self.image, self.x, self.y)   #

   #
     
    def end(self, sprite):  #
         self.game.running = False   #
         sprite.openCastle()   #
         time.sleep(1)   #
         self.game.canvas.itemconfig(self.image, state='hidden')     #
         sprite.closeCastle()  #

g = Game()  # создаем обьект класса Game и сохраняем его в переменной g
platform1 = PlatformSprite(g, PhotoImage(file="platform1.gif"), 50, 800, 120, 31)    # 9 создаем платформу 1 и ее позицию
platform2 = PlatformSprite(g, PhotoImage(file="platform1.gif"), 170, 800, 120, 31)      #   8
platform3 = PlatformSprite(g, PhotoImage(file="platform1.gif"), 20, 650, 120, 31)      #
#platform4 = PlatformSprite(g, PhotoImage(file="platform1.gif"), 350, 450, 120, 31)     #
#platform5 = PlatformSprite(g, PhotoImage(file="platform2.gif"), 250, 750, 150, 39)      #   10
#platform5 = MovingPlatformSprite(g, PhotoImage(file="platform2.gif"), 250, 750, 150, 39)     #
#platform6 = PlatformSprite(g, PhotoImage(file="platform2.gif"), 50, 460, 390, 39)    # 3
#platform7 = PlatformSprite(g, PhotoImage(file="platform2.gif"), 50, 580, 300, 39)   #   5
#platform8 = PlatformSprite(g, PhotoImage(file="platform2.gif"), 290, 250, 250, 39)     # 1
#platform9 = PlatformSprite(g, PhotoImage(file="platform3.gif"), 270, 550, 150, 44)  #   4
#platform9 = MovingPlatformSprite(g, PhotoImage(file="platform3.gif"), 270, 550, 150, 44)     #
#platform10 = PlatformSprite(g, PhotoImage(file="platform3.gif"), 190, 350, 50, 44)      #   2
g.sprites.append(platform1)     #
g.sprites.append(platform2)     #
g.sprites.append(platform3)     #
#g.sprites.append(platform4)     #
#g.sprites.append(platform5)     #
#g.sprites.append(platform6)     #
#g.sprites.append(platform7)     #
#g.sprites.append(platform8)     #
#g.sprites.append(platform9)     #
#g.sprites.append(platform10)       #
Castle = CastleSprite(g, PhotoImage(file="Castle.gif"), 0, 0, 300, 270)    #
g.sprites.append(Castle)      #
sf = StickFigureSprite(g)   #
g.sprites.append(sf)    #
g.mainloop()    # вызывается функция созданого обьекта чтобы заработал главный цыкл
