
# date: 2019.07.13
# it shows image and fade to anoter image

import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))

img1 = pygame.image.load('image1.jpg').convert()
img1_rect = img.get_rect()

alpha = pygame.image.load('image2.jpg').convert()
alpha.set_alpha(0)
alpha_rect = alpha.get_rect()

alpha_val = 0
alpha_step = 10

clock = pygame.time.Clock()
running = True
fading = False

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                fading = True

    if fading:
        alpha.set_alpha(alpha_val)
        if alpha_val < 256-alpha_step:
            alpha_val += alpha_step
        else:
            running = False

    screen.blit(img, img_rect)
    screen.blit(alpha, alpha_rect)
                
    pygame.display.flip()
    clock.tick(30)

pygame.quit()    
