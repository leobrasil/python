import pygame

pygame.init()

GREEN = (0,145,117)
BLUE = (0,0,255)
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

fps = pygame.time.Clock()

display = pygame.display.set_mode((1280,720))
player1 = pygame.Rect(0,0,30,150)
player1_speed = 0
player2 = pygame.Rect(1250,0,30,150)
ball    = pygame.Rect(600,350,15,15)
ball_x = 5
ball_y = 5

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_speed =-1
            if event.key == pygame.K_s:
                player1_speed = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1_speed =0
            if event.key == pygame.K_s:
                player1_speed = 0
        


    display.fill(GREEN)
    pygame.draw.rect(display,BLUE,player1)
    if player1.y<=0:
        player1.y = 0
    if player1.y >= 570:
        player1.y = 570

    player1.y += player1_speed

    if ball.x <=0:
        ball.x=600
    if ball.x >= 1280:
        ball.x=600
    if ball.y <= 15:
        ball_y *= -1
    if ball.y >=705:
        ball_y *= -1
    
    ball.x -=ball_x
    ball.y -=ball_y

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_x *=-1

    pygame.draw.rect(display,RED,player2)
    pygame.draw.circle(display,BLACK,ball.center,8)

    fps.tick(60)
    pygame.display.flip()