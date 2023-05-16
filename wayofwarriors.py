import pygame
from pygame.locals import *
from fighter import fighter
from pygame import mixer

mixer.init()
pygame.init()

size = (width,height)= (1000,600)
screen = pygame.display.set_mode(size)
icon = pygame.image.load("assets\images\icons\icon.png")
pygame.display.set_icon(icon)

pygame.display.set_caption("Way of the Warriors ")
clock = pygame.time.Clock()
fps = 60

intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0 , 0]
round_over = False
round_over_cd = 3000

w1_size = 200
w1_scale = 3.5
w1_offset = [87, 69.5]
w1_data = [w1_size, w1_scale, w1_offset]
w2_size = 200
w2_scale = 3.5
w2_offset =[85, 75.8]
w2_data = [w2_size, w2_scale, w2_offset]


sword_fx = pygame.mixer.Sound("assets/audio/sword.wav")
sword_fx.set_volume(0.4)

background = pygame.image.load("assets/images/background/5.jpg").convert_alpha()
w1_sheet =pygame.image.load("assets\images\warrior1\Sprites\w1.png").convert_alpha()
w2_sheet =pygame.image.load("assets\images\warrior2\Sprites\w2.png").convert_alpha()



w1_animation_steps=[3, 4, 5, 6, 5, 6, 1 , 1]
w2_animation_steps=[3, 4, 5, 6, 7, 8, 2 , 1]

count_font = pygame.font.Font("assets/fonts/turok.ttf ", 180)
vic_font = pygame.font.Font("assets/fonts/turok.ttf ", 180)
vic_text =  vic_font.render("Victory", 1, (255, 0, 0))
                           

score_font = pygame.font.Font("assets/fonts/turok.ttf ", 30)

def draw_text(text, font , text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x,y))

def draw_bg():
    bg_img = pygame.transform.scale(background,(width,height))
    screen.blit(bg_img,(0,0))
    pause_img = pygame.transform.scale(pygame.image.load('assets\images\icons\pausebut.png'), (40, 40))
    play_img = pygame.transform.scale(pygame.image.load('assets\images\icons\playbut.png'), (40, 40))
    btn_size = 40
    play_btn_rect = pygame.Rect(20, 100, btn_size, btn_size)
    pause_btn_rect = pygame.Rect(20,  150, btn_size, btn_size)
    screen.blit(play_img, play_btn_rect)
    screen.blit(pause_img, pause_btn_rect)

    
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, (0, 51, 0),(x-2, y-2, 404 ,34))
    pygame.draw.rect(screen, (128, 0, 0),(x, y, 400 ,30))
    pygame.draw.rect(screen, (0, 128, 0),(x, y, 400 * ratio,30))

 

fighter_1 = fighter(1, 200, 410, False, w1_data, w1_sheet, w1_animation_steps, sword_fx)
fighter_2 = fighter(2, 700, 410, True, w2_data, w2_sheet, w2_animation_steps, sword_fx)


run = True
while run :
    clock.tick(fps)
    draw_bg()
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)
    draw_text("P1: " + str(score[0]), score_font, (255, 0, 0), 20, 60)
    draw_text("P2: " + str(score[1]), score_font, (255, 0, 0), 580, 60)

    

    if intro_count <= 0:  

        fighter_1.move(width, height, fighter_2, round_over)
        fighter_2.move(width, height, fighter_1, round_over)
    else:
        draw_text(str(intro_count),  count_font , (255, 0, 0), width/2-40, height/3)
        if (pygame.time.get_ticks()-last_count_update) >= 1000:
            intro_count -= 1
            last_count_update = pygame.time.get_ticks()


    fighter_1.update()
    fighter_2.update()

    fighter_1.draw(screen)
    fighter_2.draw(screen)


    if round_over == False:
        if fighter_1.alive == False:
            score[1] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
        elif fighter_2.alive == False:
            score[0] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()

    else:
        screen.blit(vic_text, (width/2-275,height/2-90))
        if pygame.time.get_ticks()- round_over_time > round_over_cd:
            round_over = False
            intro_count = 3 
            fighter_1 = fighter(1, 200, 410, False, w1_data, w1_sheet, w1_animation_steps , sword_fx)
            fighter_2 = fighter(2, 700, 410, True, w2_data, w2_sheet, w2_animation_steps, sword_fx)          

    for event in pygame.event.get():
        if event.type == QUIT :
            run = False

        elif event.type == MOUSEBUTTONDOWN:
              
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                btn_size = 40
                play_btn_rect = pygame.Rect(20, 100, btn_size, btn_size)
                pause_btn_rect = pygame.Rect(20,  150, btn_size, btn_size)
                     
                if play_btn_rect.collidepoint(mouse_pos):
                        pygame.mixer.music.load('assets/audio/music2.mp3')
                        pygame.mixer.music.set_volume(0.5)
                        pygame.mixer.music.play(-1) 
                        is_music_playing = True

                    
                elif pause_btn_rect.collidepoint(mouse_pos):
                        pygame.mixer.music.stop()
                        is_music_playing = False
    
    pygame.display.update()

pygame.quit()
