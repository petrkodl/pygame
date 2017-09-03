#!/usr/bin/env python3.6
import sys, pygame

pygame.init()

size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0
white = 255,255,255
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
bomb = pygame.image.load("explosion.png")
ballrect = ball.get_rect()
bombrect = bomb.get_rect()
explosion= pygame.mixer.Sound("bomb.wav")
jump = pygame.mixer.Sound("jump.wav")

padx = 10
pady = 470

paddle = pygame.draw.rect(screen, white, (padx, pady, 50, 10))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        padx = max(padx - 5, 0)
    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        padx = min(padx + 5, 640 - 50)
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        jump.play()
    if ballrect.top < 0:
        speed[1] = -speed[1]
        jump.play()
    if ballrect.bottom > height-5:
        if abs((padx + 25)-.5 * (ballrect.left + ballrect.right)) < 25:
            speed[1] = -speed[1]
            jump.play()
        else:
            screen.fill(black)
            xx = (width - bombrect.width)/2
            yy = (height- bombrect.height)/2
            screen.blit(bomb,(xx,yy))
            pygame.display.flip()
            explosion.play()
            pygame.time.wait(3000)
            sys.exit(0)
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.draw.rect(screen, white, (padx, pady, 50, 10))
    pygame.display.flip()
    clock.tick(60)
