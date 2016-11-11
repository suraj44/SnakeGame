import pygame
import time
import random


pygame.init()



white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

display_width = 800
display_height = 600

block_size = 10


font = pygame.font.SysFont(None, 25)
img = pygame.image.load('snakehead.png')

##f = open("highscore","a")
##g = f.readlines()
##if not g:
##    raise
user_name = raw_input("Enter your name->")
print "Hi", user_name, "!"
print """This is our rendition of the classic game 'Snake'.
The objective of the game is to eat the apple using the snake.

The instructions are fairly simple.
The user is required to control the snake using the arrow keys and eat the apple by
moving the snake's head over the apple.

**RULES**
->If you cross the boundary of the screen, you lose.
->If you eat yourself, you lose.
->If you try to move in the opposite direction, you lose.

**IMPORTANT**
Using the mouse,click the window that pops up after starting the game to take control.


"""
try:
    pygame.mixer.music.load("Music.mp3")
    #pygame.mixer.music.play()
except:
    pass
x = raw_input("Enter any key to start the game.")



user_score = 0

class Snake:
    BlockSize = 10
    def __init__(self):
        self.snakeList = []
        self.snakeLength = 0
        self.lead_x = display_width/2
        self.lead_y = display_height/2
    def snake(self):
        
        if direction == "right":
            head = pygame.transform.rotate(img,270)
        if direction == "left":
            head = pygame.transform.rotate(img,90)
        if direction == "up":
            head = img
        if direction == "down":
            head = pygame.transform.rotate(img,180)
        gameDisplay.blit(head, (self.snakeList[-1][0],self.snakeList[-1][1]))
        for XnY in self.snakeList[:-1]:
            pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],Snake.BlockSize,Snake.BlockSize])  

class Score:
    def __init__(self):
        self.score = 0
        self.snakeLength = 0
    def score_show(self):
        text = font.render("Score: "+str(self.score), True, white)
        gameDisplay.blit(text,[0,0])


def message_to_screen(msg,colour):
    screen_text = font.render(msg, True, colour)
    gameDisplay.blit(screen_text, [display_width/2-300, display_height/2])




gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('The Snake Game')

clock = pygame.time.Clock()
logo = pygame.image.load("logo.png")
gameDisplay.blit(logo, (275,75))

msg = """Welcome to the snake game!"""

screen_text = font.render(msg, True, white)
gameDisplay.blit(screen_text, [display_width/2 - 100, display_height/2+50])
pygame.display.update()
time.sleep(3)

def gameLoop():
    try:
        pygame.mixer.music.play()
    except:
        pass
    global user_name
    global user_score
    apple = pygame.image.load("apple.png")
    global direction
    FPS = 25
    gameExit = False
    gameOver = False

    lead_x_change = 10
    lead_y_change = 0
    direction = "right"
    SNAKE = Snake()
    SNAKE.snakeLength = 1

    sc = Score()

    randAppleX = round(random.randint(0,display_width-block_size)/10.0)*10
    randAppleY = round(random.randint(0,display_height-block_size)/10.0)*10
    
    while not gameExit:

        while gameOver == True:
            f= open("highscore.txt",'r')
            g = f.readlines()
            if sc.score > int(g[1]):
                tmp = "CONGRATULATIONS, YOU BEAT "+str(g[0])+" WITH A NEW RECORD OF "+str(sc.score)
                message_to_screen(tmp,red)
                pygame.display.update()
                time.sleep(3)
                gameDisplay.fill(black)
                tmp =  "Saving...."
                message_to_screen(tmp,red)
                pygame.display.update()
                gameDisplay.fill(black)
                time.sleep(1)
                tempL = [str(user_name)+"\n",str(sc.score)]
                f.close()
                f= open("highscore.txt",'w')
                f.writelines(tempL)
                f.close()
                tmp = "Saved."
                message_to_screen(tmp,red)
                pygame.display.update()
                gameDisplay.fill(black)
                tmp = "PRESS C TO PLAY AGAIN OR Q TO QUIT"
                message_to_screen(tmp,red)
            else:  
                gameDisplay.fill(black)
                tempMes = "GAME OVER    Score " + str(sc.score) + "    PRESS C TO PLAY AGAIN OR Q TO QUIT"
                message_to_screen(tempMes, red)
                pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -10
                    lead_y_change = 0
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = 10
                    lead_y_change = 0
                    direction = "right"
                elif event.key == pygame.K_UP:
                    lead_y_change = -10
                    lead_x_change = 0
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    lead_y_change = 10
                    lead_x_change = 0
                    direction = "down"

        if SNAKE.lead_x >= display_width or SNAKE.lead_x < 0 or SNAKE.lead_y >= display_height or SNAKE.lead_y < 0:
            gameOver = True

        SNAKE.lead_x += lead_x_change
        SNAKE.lead_y += lead_y_change

        gameDisplay.fill(black)
        #pygame.draw.rect(gameDisplay, red, [randAppleX,randAppleY,block_size,block_size])
        gameDisplay.blit(apple, (randAppleX,randAppleY))
        
        snakeHead = []      
        snakeHead.append(SNAKE.lead_x)
        snakeHead.append(SNAKE.lead_y)
        SNAKE.snakeList.append(snakeHead)

        if len(SNAKE.snakeList) > SNAKE.snakeLength:
            del SNAKE.snakeList[0]

        for eachSegment in SNAKE.snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        SNAKE.snake()
        sc.score_show()
        pygame.display.update()
        if SNAKE.lead_x >= randAppleX and SNAKE.lead_x <= randAppleX + 10 or SNAKE.lead_x + 10 <= randAppleX and SNAKE.lead_x + 10 >= randAppleX:
            if SNAKE.lead_y >= randAppleY and SNAKE.lead_y <= randAppleY + 10 or SNAKE.lead_y + 10<= randAppleY and SNAKE.lead_y + 10 >= randAppleY:
                randAppleX = round(random.randint(0,display_width-block_size)/10.0)*10
                randAppleY = round(random.randint(0,display_height-block_size)/10.0)*10
                SNAKE.snakeLength += 1
                sc.score += 1
                FPS +=2

        clock.tick(FPS)
    pygame.quit()
    quit()
#gameLoop()
try:
    gameLoop()
except Exception, e:
    print e.message

