import pygame
from pygame.locals import *
from fighter import fighter
pygame.init()

size = (width,height)= (1000,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Fight")
clock = pygame.time.Clock()
fps = 60

w1_size = 162
w1_scale = 4
w1_offset = [72, 56]
w1_data = [w1_size, w1_scale, w1_offset]
w2_size = 250
w2_scale = 3
w2_offset =[112, 107]
w2_data = [w2_size, w2_scale, w2_offset]

background = pygame.image.load("assets/5.jpg").convert_alpha()
w1_sheet =pygame.image.load("assets\images\warrior\Sprites\warrior.png").convert_alpha()
w2_sheet =pygame.image.load("assets\images\wizard\Sprites\wizard.png").convert_alpha()


w1_animation_steps=[10, 8, 1, 7, 7, 3, 7]
w2_animation_steps=[8, 8, 1, 8, 8, 3, 7]

def draw_bg():
    bg_img = pygame.transform.scale(background,(width,height))
    screen.blit(bg_img,(0,0))
    
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, (255, 255, 0),(x-2, y-2, 404 ,34))
    pygame.draw.rect(screen, (255, 0, 0),(x, y, 400 ,30))
    pygame.draw.rect(screen, (0, 255, 0),(x, y, 400 * ratio,30))

fighter_1 = fighter(200, 410, False, w1_data, w1_sheet, w1_animation_steps)
fighter_2 = fighter(700, 410, True, w2_data, w2_sheet, w2_animation_steps)


run = True
while run :
    clock.tick(fps)
    draw_bg()
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)



    fighter_1.move(width, height, screen, fighter_2)
    #fighter_2.move()

    fighter_1.update()
    fighter_1.update()

    fighter_1.draw(screen)
    fighter_2.draw(screen)
    for event in pygame.event.get():
        if event.type == QUIT :
            run = False
    pygame.display.update()

pygame.quit()

