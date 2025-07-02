from math import hypot
from random import randint
from pygame import *
init()

window = display.set_mode((800,800))
clock = time.Clock()

my_player = [0, 0, 20]
running = True

class Food:
    def __init__(self, x, y, r, c):
        self.x = x
        self.y = y
        self.r = r
        self.c = c

    def check_collision(self, player_x, player_y, player_r):
        dx = self.x - player_x
        dy = self.y - player_y
        return hypot(dx, dy) <= self.r + player_r
    
foods = [Food(randint(-2000,2000),randint(-2000,2000), 10, (randint(0,255), randint(0,255), randint(0,255)))
         for _ in range(300)]
        

while running:
    window.fill((255, 255, 255))
    scale = max(0.3, min(50/my_player[2],1.5))
    for e in event.get():
        if e.type == QUIT:
            running = False
    draw.circle(window, (0, 255, 0), (375, 375), int(my_player[2] * scale))  

    to_remove = []
    for food in foods:
        if food.check_collision(my_player[0],my_player[1],my_player[2]):
            to_remove.append(food)
            my_player[2] += int(food.r * 0.2)
        else:
            sx = int((food.x -my_player[0]) * scale + 500)
            sy = int((food.y -my_player[0]) * scale + 500)
            draw.circle(window, food.c, (sx,sy), int(food.r * scale))
        for food in to_remove:
            foods.remove(food)
    
    display.update()
    clock.tick(60)

    keys = key.get_pressed()
    if keys[K_w]: my_player[1] -= 15
    if keys[K_s]: my_player[1] += 15
    if keys[K_a]: my_player[0] -= 15
    if keys[K_d]: my_player[0] += 15

quit()
