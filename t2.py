import pygame

class fighter():
    def __init__(self, x, y, flip, data, sprite_sheet, animation_steps):
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = flip
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100
        


    def load_images(self, sprite_sheet, animation_steps):
        animation_list = []
        for y, animation in enumerate(animation_steps):
            
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x *self.size, y*self.size, self.size, self.size)
                pygame.transform.scale(temp_img,(self.size * self.image_scale, self.size * self.image_scale))
                temp_img_list.append(pygame.transform.scale(temp_img,(self.size * self.image_scale, self.size * self.image_scale)))
            animation_list.append(temp_img_list)        
        return animation_list        

    def move(self, WIDTH, HEIGHT, surface, target):
        speed = 5
        gravity = 2
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        
        if self.attacking == False:

            if key[pygame.K_a]:
                dx = -speed
            if key[pygame.K_d]:
                dx = speed

            if key[pygame.K_w] and self.jump == False:
                self.vel_y = -32
                self.jump = True

            if key[pygame.K_z] or  key[pygame.K_x]:
                self.attack(surface, target)

                if key[pygame.K_z] :
                    self.attack_type = 1
                       
                if key[pygame.K_x] :
                    self.attack_type = 2  
                    
        self.vel_y += gravity
        dy += self.vel_y
           


        if self.rect.left +dx < 0 :
            dx = 0 - self.rect.left
        if self.rect.right +dx > WIDTH :
            dx = WIDTH - self.rect.right 
        
        if self.rect.bottom + dy > HEIGHT - 10 :
           self.vel_y = 0
           self.jump = False

           dy = HEIGHT - 10 - self.rect.bottom

        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else :
            self.flip = True     
      
        self.rect.x += dx
        self.rect.y += dy 


    def update(self):
        animation_cooldown = 50
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0    

    def attack (self, surface, target):

        self.attacking = True
        attack_rect = pygame.Rect(self.rect.centerx- (2* self.rect.width * self.flip), self.rect.y, 2*self.rect.width, self.rect.height)
        if attack_rect.colliderect(target.rect):           
            target.health -= 10

        pygame.draw.rect(surface, (255, 0, 255), attack_rect)      

    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        pygame.draw.rect(surface, (255, 255, 0), self.rect)
        surface.blit(img, (self.rect.x- (self.offset[0]*self.image_scale), self.rect.y- (self.offset[1]*self.image_scale)))    