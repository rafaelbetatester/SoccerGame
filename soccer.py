import pygame
from INI import *
from Field import *
from Ball import *
from Player import *
#print(y)
        
pygame.init()
pygame.font.init()

window = pygame.display.set_mode((win_width, win_height))
BackGround = Background('Field.jpg', [0,0])

player1 = player(window)
ball1 = Ball(window)

def collision (x1, y1, r1, x2, y2, r2):
    if ((x1-x2)**2 + (y1-y2)**2) <= (r1 + r2)**2:
        #print(x1)
        #print((x1-x2)**2 + (y1-y2)**2)
        return True
    else:
        return False

while True:

    event = pygame.event.poll()
    if event.type == pygame.QUIT:        
        pygame.quit()
        sys.exit() 

    #playerDir = [0 , 0]
    dirX = 0
    dirY = 0
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] : 
        dirY += -1
    if pressed[pygame.K_DOWN]                      : 
        dirY += 1
    if pressed[pygame.K_LEFT]                      : 
        dirX += -1
    if pressed[pygame.K_RIGHT]                     : 
        dirX += 1

    playerDir = [dirX , dirY]
    
    
  #  drawSoccer(window)

#    pygame.draw.circle(window, black, (int(ball_pos[x]), int(ball_pos[y])), radius)
#    drawBall(window)
    

#    Background.blit()
    window.fill([255, 255, 255])
    window.blit(BackGround.image, BackGround.rect)

    player1.move(playerDir)

    if collision(player1.X,player1.Y,player1.radius,ball1.X,ball1.Y,ball1.radius):
        if pressed[pygame.K_SPACE]                     :
            ball1.speed = [8*ball1.speed[0], 8*ball1.speed[1]]
        else:
            ball1.speed = [4*dirX, 4*dirY]
    #else:
     #   ball1.speed = [0,0]
    ball1.move([0,0])
    pygame.display.update()
    
    clock = pygame.time.Clock().tick(60)
