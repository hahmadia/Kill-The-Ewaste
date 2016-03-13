# Game made by Hossein Ahmadian-Yazdi , inspired by the siddiqi brothers , and marked by (the almighty) Mr.Ching
# Spaceship Game 
# "If music be the food of love, then play on!" - Shakespeare

# Initilizing python and defining all my variables
from pygame import *
from random import *
cheats = 0

while True:
    name = raw_input("What is your full name? ")
    # Checks if user is making up their name (Length of name chosen based on my full name which i dont think anyone will exceed.) or if they entered nothing at all
    if len(name) > 22:
        print "Your name was too long, please type a shorter form of your name."
    elif len(name) <= 0:
        print "You did not enter a valid name, please try again."
    else:
        break
    
    
if name.lower() == "mr.ching" or name.lower() == "mr. ching" or name.lower() == "hossein" :
    cheats = input("Would you like god mode to be activated? (1 for yes, 2 for no): ")

init()
SIZE = (500,500)
screen = display.set_mode(SIZE)
WHITE = (255,255,255)
ROYAL_BLUE=(135,206,250)
GREY = (139,131,134)
BLACK = (0,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
RAINBOW = (randint(0,255),randint(0,255),randint(0,255))
running = True
myClock = time.Clock()
spaceshipX = 40
spaceshipY = 430
SPACESHIP_WIDTH = 10
SPACESHIP_LENGTH= 10
spaceshipMinX= 40
spaceshipMaxX = 50
spaceshipMaxY = 50
i = 0
info = 0
info1 = 0
highscore1 = 0
highscore = 0
nameFile = 0
nameTrack = 0
shotDecrease = 5

star = []
starX = 0
starY = 0
starRad = 0

# Square size ( L stands for length , sq means sqaure) (SS = SPACESHIP)
LSQ = 10
spaceShipMovement = 4

random_Move = 0
random_Move1 = 0
moveSpeed = randint(1,10)
SHOT_LAG = 20

MIN_SCREEN_LENGTH = 0
MAX_SCREEN_LENGTH = 500

CELLPHONE_MAX_X = 26
TV_MAX_X = 50
CELLPHONE_MAX_Y = 55
TV_MAX_Y = 50

displayText = True

random_Move_Counter=0
score = 0
STARTING_SPEED = 5

highscoreCord = 280
highscoreCord1 = 190
highscoreCord2 = 300
highscoreCord3 = 150


# File Initilization
music = mixer.Sound("music"+str(randint(1,3))+".wav")
laserSound = mixer.Sound("laser.wav")
explosionSound = mixer.Sound("explosion.wav")

font1 = font.SysFont("Times New Roman" , 30)
font3 = font.SysFont("Times New Roman" , 25)
font2 = font.SysFont("Times New Roman" , 55)
mainMenu = True
mainMenuTitle = font2.render("KILL THE E-WASTE!",1,GREEN)
mainMenuDesc = font3.render("The E-waste are taking over the planet!",1,YELLOW)
mainMenuDesc1 = font3.render("Help the astronaut kill them with his spaceship!",1,YELLOW)
mainMenuDesc2 = font3.render("Use the arrow keys to move",1,ROYAL_BLUE)
mainMenuDesc3 = font3.render("and hold spacebar to shoot at the nasty E-waste.",1,ROYAL_BLUE)
mainMenuDesc4 = font3.render("Dont let the E-waste touch you",1,WHITE)
mainMenuDesc5 = font3.render("otherwise you will be dead.",1,WHITE)
startGame = font3.render("PLAY GAME!",1,BLACK)
viewHighscore = font3.render("View Highscores!",1,WHITE)
madeHighscore = font1.render("YOU MADE THE HIGHSCORES!",1,RAINBOW)
outputHighscore = 0
outputHighName = 0
highscoreY = 0
text = font1.render(str(score),1,GREEN)



# Shot variables
shot_x = (spaceshipX + SPACESHIP_WIDTH) / 2
shot_y = spaceshipY + 5
shooting = False
shot_counter = 0
shot_cord = []


# Enemy variables
enemy_cord = []
loopCounter = 0
ENEMY_NUM = 10

# Assigning beginning movement speed for enemy
move = []
resetVar = False
running1 = True

if cheats == 1:
    spaceShipMovement = 20
    SHOT_LAG = 5
    shotDecrease = 20
else:
    pass
    


# Method to check if the enemy has collided with the player
def playerHit(playerX,playerY,enemyX,enemyY,enemyType):
    # Checks to see if the shot cordinate is inside the enemy
    if enemyType == 1:
        width = CELLPHONE_MAX_X
        height = CELLPHONE_MAX_Y
    else:
        height = TV_MAX_Y
        width = TV_MAX_X
    
    # Checking to see if each row of the spaceship has collided with the enemy
    for i in range(1,6):
        if playerX+LSQ*i >= enemyX and playerX-(i-1)*LSQ <= enemyX+width and playerY + (i-1)*LSQ <= enemyY+height and playerY + i*LSQ >= enemyY:
            return True
    return False #all the checks failed
            
# Method for checking if enemy has been hit. 
def enemyHit(bulletx,enemyx,bullety,enemyy,enemyType):
    # Checks to see if the shot cordinate is inside the enemy
    if enemyType == 1:
        # Checks if the cellphone has been hit with a bullet
        if bulletx >= enemyx and bulletx <= enemyx + CELLPHONE_MAX_X and bullety <= enemyy + CELLPHONE_MAX_Y and bullety >= enemyy:
            return True
        else:
            return False
    elif enemyType == 2:
        # Checks if the TV has been hit with a bullet
        if bulletx >= enemyx and bulletx <= enemyx + TV_MAX_X and bullety <= enemyy + TV_MAX_Y and bullety >= enemyy:
            return True
        else:
            return False

#Method for the star drawing
def drawStar(x,y,radius):
    draw.circle(screen,WHITE,(x,y),radius)



# Method for drawing my enemies
def enemy(x,y,type1):
    if type1 == 1: # Phone
        draw.rect(screen, YELLOW, Rect(x, y+10, 26, 45)) # Body of phone
        draw.rect(screen, WHITE, Rect(x+24, y, 2, 10)) # Antenna
        draw.rect(screen, BLACK, Rect(x+3, y+13, 20, 14)) # Screen
        draw.rect(screen, GREY, Rect(x+2, y+32,  6, 6)) # Buttons
        draw.rect(screen, GREY, Rect(x+10, y+32, 6, 6))
        draw.rect(screen, GREY, Rect(x+18, y+32, 6, 6))
        draw.rect(screen, GREY, Rect(x+2, y+40, 6, 6))
        draw.rect(screen, GREY, Rect(x+10, y+40, 6, 6))
        draw.rect(screen, GREY, Rect(x+18, y+40, 6, 6))
        draw.rect(screen, GREY, Rect(x+2, y+48, 6, 6))
        draw.rect(screen, GREY, Rect(x+10, y+48, 6, 6))
        draw.rect(screen, GREY, Rect(x+18, y+48, 6, 6))

    else: # TV
        draw.rect(screen, WHITE, Rect(x,y, 50 , 50 )) # Body
        draw.rect(screen, BLACK, Rect(x+2,y+2, 45 , 30 )) # Screen
        draw.rect(screen, GREY, Rect(x+3,+y+40, 6 , 6 ))# Buttons
        draw.rect(screen, GREY, Rect(x+10,y+40, 6 , 6 ))
        draw.rect(screen, GREY, Rect(x+17,y+40, 6 , 6 ))
        draw.line(screen, (WHITE), (x+47,y-20), (x+47,y), 3) # Antenna
        draw.circle(screen, ROYAL_BLUE,(x+40,y+40),6)  # Knob


# Method to draw my spaceship  
def spaceship(x,y):
    draw.rect(screen, ROYAL_BLUE, Rect(x,y, SPACESHIP_LENGTH , SPACESHIP_WIDTH ))
    draw.rect(screen, ROYAL_BLUE, Rect(x-10,y+10, SPACESHIP_LENGTH , SPACESHIP_WIDTH ))
    draw.rect(screen, ROYAL_BLUE, Rect(x+10,y+10, SPACESHIP_LENGTH , SPACESHIP_WIDTH ))
    draw.rect(screen, ROYAL_BLUE, Rect(x-20,y+20, SPACESHIP_LENGTH , SPACESHIP_WIDTH ))
    draw.rect(screen, ROYAL_BLUE, Rect(x+20,y+20, SPACESHIP_LENGTH , SPACESHIP_WIDTH ))
    draw.rect(screen, ROYAL_BLUE, Rect(x-30,y+30, SPACESHIP_LENGTH , SPACESHIP_WIDTH ))
    draw.rect(screen, ROYAL_BLUE, Rect(x+30,y+30, SPACESHIP_LENGTH , SPACESHIP_WIDTH ))
    draw.rect(screen, ROYAL_BLUE, Rect(x-40,y+40, SPACESHIP_LENGTH , SPACESHIP_WIDTH ))
    draw.rect(screen, ROYAL_BLUE, Rect(x+40,y+40, SPACESHIP_LENGTH , SPACESHIP_WIDTH ))
    draw.rect(screen, ROYAL_BLUE, Rect(x-20,y+40, SPACESHIP_LENGTH , SPACESHIP_WIDTH ))
    draw.rect(screen, ROYAL_BLUE, Rect(x,y+40, SPACESHIP_LENGTH , SPACESHIP_WIDTH ))
    draw.rect(screen, ROYAL_BLUE, Rect(x+20,y+40, SPACESHIP_LENGTH , SPACESHIP_WIDTH ))

# Method to draw the bullet for the spaceship
def shot(x,y):
    draw.line(screen, (YELLOW), (x,y), (x,y+10), 3)
 
# Removes duplicate elements from a list
def removeRepeats(l):
    seen = [] #keeps track of everything we've seen in the list
    result = [] #the list that we return from this method
    for i in l:
        if not i in seen: # if we haven't seen the number in the list we have passed through the method in the list seen
            seen.append(i) # then add it to seen so we know that we have already "seen" it
            result.append(i) # add it to out final result list
        else:
            pass # otherwise if the number is already in the list seen , then skip over to the next number
    return result


    
    
RAINBOW = (randint(0,255),randint(0,255),randint(0,255))

# Start playing that funky music!!
music.play(-1)     
# Game Main Menu
def menu():
    global mainMenu , mx , my , resetVar , quitting , displayText,info,info1,highscore1,nameTrack,highscore,nameFile,outputHighscore,highscoreY,outputHighName,highscoreCord,highscoreCord1,highscoreCord2,highscoreCord3
    
    mainMenu = True
    mx,my = 0,0    
    resetVar = False
    
    while mainMenu:
        
        

        if displayText == True:
            screen.fill(RAINBOW)        
            
            
        # Checks if user has quit the main menu
        for evnt in event.get():
            if evnt.type == QUIT:
                mainMenu = False
                
            if evnt.type == MOUSEBUTTONDOWN:
                mx, my = evnt.pos
                button = evnt.button            
        
        
       # Starting the game !
        if mx <= 25+200 and mx > 25  and  my <= 320+100 and my > 320 and displayText == True:
            mainMenu = False
            resetVar = True
           
                       
        # Viewing highscores  
        elif mx <= highscoreCord+highscoreCord1 and mx > highscoreCord  and  my <= highscoreCord2+highscoreCord3 and my > highscoreCord2:
            displayText = False
            mx,my = 0,0
            highscoreCord=0
            highscoreCord1=0
            highscoreCord2=0
            highscoreCord3=0
            
            screen.fill(BLACK)
                  
               
            # Opens highhighscors in read mode, and makes empty list
            info = open("highscore.txt","r")
            info1 = open("name.txt","r")
            highscore1 = []
            nameTrack = []
                
            # Reads each line and write to the list
            for i in range(10):
                highscore = int(info.readline())
                nameFile = (info1.readline())
                if "\n" in nameFile:
                    nameFile = nameFile.replace("\n","")
                highscore1.append(highscore)
                nameTrack.append(nameFile) 
            
            # Outputs the highscore on the screen
            for i in range(len(highscore1)):
                outputHighscore = font1.render(str(highscore1[i]),1,WHITE)
                screen.blit(outputHighscore,Rect(430,highscoreY,1,1))
                outputHighName = font1.render(nameTrack[i],1,WHITE)
                screen.blit(outputHighName,Rect(0,highscoreY,1,1))                
                highscoreY += 50
        
            # Closes high score file    
            info.close()
            info1.close()
            
        # Checks to see if user has clicked anywhere on the screen to exit the highscores
        if mx < 500  and mx > 0 and my < 500 and my > 0 and displayText == False:
            highscoreCord = 280
            highscoreCord1 = 190
            highscoreCord2 = 300
            highscoreCord3 = 150
            displayText = True               
            mx,my = 0,0
            highscoreY = 0       
        
        # Displays main menu
        if displayText == True:            
            screen.blit(mainMenuTitle,Rect(10,10,50,50))
            screen.blit(mainMenuDesc,Rect(80,70,50,100))
            screen.blit(mainMenuDesc1,Rect(10,100,10,100))
            screen.blit(mainMenuDesc2,Rect(100,130,50,100))
            screen.blit(mainMenuDesc3,Rect(10,160,50,100))
            screen.blit(mainMenuDesc4,Rect(80,190,50,100))
            screen.blit(mainMenuDesc5,Rect(100,220,50,100))
            
            
            draw.ellipse(screen, GREEN, Rect(25,320,200,100 ))
            draw.rect(screen, ROYAL_BLUE, Rect(280,300,190,150 ))
            screen.blit(startGame,Rect(50,350,50,100))
            screen.blit(viewHighscore,Rect(283,350,50,100))
            screen.blit(font.SysFont("Times New Roman" , 20).render("Made by: Hossein A. , Inspired by: Dave and Shams Siddiqi",1,(255,0,0)),Rect(10,470,1,1))
        
        display.flip()

 
       




def game():
    global running, loopCounter, shot_counter, random_Move_Counter, SHOT_LAG , moveSpeed, spaceshipX,spaceshipY,text,random_Move1,score,shooting,shot_x,shot_y,counter,shot_cord,enemy_cord,running1,info,highscore1,highscore,nameFile,nameTrack,info1
    menu()
    
    
    #Decides if it should reset values or quit the game
    if resetVar == True:
        running = True
        spaceshipX = 40
        spaceshipY = 430
        spaceshipMinX= 40
        i = 0
        moveSpeed = randint(1,10)
        random_Move_Counter=0
        score = 0
        text = font1.render(str(score),1,GREEN)
        # Shot variables
        shot_x = (spaceshipX + SPACESHIP_WIDTH) / 2
        shot_y = spaceshipY + 5
        shooting = False
        shot_counter = 0
        shot_cord = []
        # Enemy variables
        enemy_cord = []
        loopCounter = 0
        ENEMY_NUM = 10
        # Assigning beginning movement speed for enemy
        move = []    
        
        # While loop that adds random enemy cord with random type
        while len(enemy_cord) < 5:
            enemy_randx = randint(0,450)
            enemy_randy = randint(0,150)
            enemy_cord.append([enemy_randx,enemy_randy,randint(1,2)])
         
        star=[]   
        for i in range(200):
            starX = randint(2,498)
            starY = randint(2,498)
            starRad = randint(1,3)
            star.append([starX,starY,starRad])         
    else:
        running = False
        running1 = False
        
    
    
    # Main game loop
    while running:
        
           
        # Enemy spawn counter ( Time needed for next enemy to spawn)
        loopCounter += 1
        
        # Timer for shots
        shot_counter += 1
    
        #Time for random movement
        random_Move_Counter +=1
        
        # Checks if user has quit the game
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                mainMenu = False
                running1 = False
       
        keys = key.get_pressed()
        
        # Checks for movement (of player)
        if keys[K_UP] == 1:
            spaceshipY -= spaceShipMovement
        if keys[K_DOWN] == 1:
            if spaceshipY + spaceshipMaxY < MAX_SCREEN_LENGTH:
                spaceshipY += spaceShipMovement
        if keys[K_LEFT] == 1:
            spaceshipX -= spaceShipMovement
            if spaceshipX - spaceshipMinX <= MIN_SCREEN_LENGTH:
                spaceshipX += spaceShipMovement 
                spaceshipX -= (spaceshipX - spaceshipMinX)
        if keys[K_RIGHT] == 1:
            spaceshipX += spaceShipMovement
            if spaceshipX + spaceshipMaxX >= MAX_SCREEN_LENGTH:
                spaceshipX -= spaceShipMovement
                spaceshipX += (MAX_SCREEN_LENGTH - (spaceshipX + spaceshipMaxX))
                
                
        # Shot lag timer
        if shot_counter >= SHOT_LAG:
            shooting = True
        
        # Checks to see if player has pressed spacebar and wants to shoot
        if keys[K_SPACE] == 1 and shooting == True:
            shot_x = (spaceshipX + (SPACESHIP_WIDTH/2)) # Calculating the middle of the spaceship
            shot_y = spaceshipY + 5
            laserSound.play()
            shot_cord.append([shot_x,shot_y]) # Adding it to the shot_cord list
            shot_counter = 0 # Resetting our shot lag counter
            shooting = False # Resetting our shot lag boolean
            
            
        # Decreases shots y value (so that it looks like its going up the screen and towards the enemy)
        for num in range (len(shot_cord)):
            shot_cord[num][1] -= shotDecrease
            counter = num
        
        # Checks to see if shot has gone off screen. If yes, then delete it from the list
        if len(shot_cord) > 0:
            if shot_cord[counter][1] + 10 <= 0:
                del shot_cord[counter]
        
        # Enemy Movement (Side to Side)
        for j in range (len(enemy_cord)):
            # Adds the randomly generated move starting speed for all of them toward the direction of left
            for i in range(len(enemy_cord)):
                move.append(moveSpeed*-1)  
                
            # Enemy movement right to left    
            enemy_cord[j][0] += move[j] # Adds the movement speed to the enemy x cord
            moveSpeed = randint(1,10) # Generate a new movement speed
            if enemy_cord[j][0] <= MIN_SCREEN_LENGTH: # Checks to see if enemy has reached the left side of the screen and makes it go in the opposite direction
                move[j] = moveSpeed
            # Otherwise it checks if its gone all the way to the right of the screen and makes the enemy go in the opposite direction with a new speed
            elif enemy_cord[j][0] + CELLPHONE_MAX_X >= MAX_SCREEN_LENGTH and enemy_cord[j][2] == 1 or enemy_cord[j][0] + TV_MAX_X >= MAX_SCREEN_LENGTH and enemy_cord[j][2] == 2 :
                move[j] = moveSpeed*-1
                
        # Randomly switches direction of the enemy (to make it harder for user)  
        if random_Move_Counter % 50 == 0:
            # checks to see if the randomly generated number is in between the restrictions set and if there is more than one enemy on the screen
            if randint(0,1000000) > 500000  and len(enemy_cord) > 1 :
                # Picks a random enemy 
                random_Move = randint(0,len(enemy_cord)-1)
                if random_Move != random_Move1:
                    move[random_Move] = move[random_Move]*-1 # That random enemy movement speed is reversed
                    enemy_cord[random_Move][0] += move[random_Move] # Gets added onto the enemy 
                    random_Move1 = random_Move # Makes sure enemy cant switch direction right after he just switched direction
        
        # Descending Speed of enemy          
        if random_Move_Counter % 10 == 0:           
            for j in range(len(enemy_cord)):
                # adds a starting speed of 5 and every 100 times through the loop, it adds one to the starting speed
                enemy_cord[j][1] += (STARTING_SPEED + loopCounter/300)
                                     
        
        #New enemy spawn 
        #Every 150 times through the loop, adds 5 new enemies at random locations
        if loopCounter % 150 == 0:
            for i in range(5):
                enemy_cord.append([randint(0,450),randint(0,50),randint(1,2)])
            
            
        # Checks to see if player has been hit by enemy        
        for i in range(len(enemy_cord)):
            if playerHit(spaceshipX,spaceshipY,enemy_cord[i][0],enemy_cord[i][1], enemy_cord[i][2]):
                
                # Draws the updated collision when the player and enemy collide so user cant say they never got hit
                screen.fill(BLACK)
                
                # Draws the stars 
                for i in range(len(star)):
                    drawStar(star[i][0],star[i][1],star[i][2])          
                
                # Draws spaceship, shots, and enemies
                spaceship(spaceshipX,spaceshipY)
                for num in range(len(shot_cord)):
                    shot(shot_cord[num][0],shot_cord[num][1])
                for i in range(len(enemy_cord)):    
                    enemy(enemy_cord[i][0],enemy_cord[i][1],enemy_cord[i][2])    
                
                     
            
                # Outputs score on screen
                screen.blit(text,Rect(0,0,30,30)) 
                
                # Updates screen        
                display.flip()
              
                # Writing highscore into files              
                info = open("highscore.txt","r")
                info1 = open("name.txt","r")
                highscore1 = []
                nameTrack = []
                
                #Reads highscore from files and adds to a list
                for i in range(10):
                    highscore = int(info.readline())
                    nameFile = (info1.readline())
                    highscore1.append(highscore)
                    nameTrack.append(nameFile)
                
                # Checks for new high score and fixes the list accordingly (Pushes everything 1 down the list :) )
                for i in range(10):
                    if score>highscore1[i]:
                        # Outputs made highscore if they made it then updates screen and allows user to view the message
                        screen.blit(madeHighscore,Rect(30,200,1,1)) 
                        display.flip()
                        time.wait(1000)
                        
                        if i < 9:
                            for j in range(8,i-1,-1):
                                highscore1[j+1] = highscore1[j]
                                nameTrack [j+1] = nameTrack[j]
                        highscore1 [i] = score
                        nameTrack [i] = name+"\n"
                       
                        break
             
                # Erases everything from the file   
                open("highscore.txt","w").close()
                open("name.txt","w").close()
                
                # Writes back the new stuff into the file
                for i in range(10):
                    info = open("highscore.txt","a")
                    info1 = open("name.txt","a")
                    info.write(str(highscore1[i])+"\n")                
                    info1.write(nameTrack[i])
                
                # closes the file   
                info.close()
                info1.close()
                
                
                
                
                running = False
                
        
        # Creating two list which keep track of the enemies that have been by bullets and the bullets that have hit the enemy 
        # Need to delete these later
        enemies_Hit = []
        shots_Hit = []
        
        # Checks every shot against every enemy (first shot fired, has it hit any of the enemies?)
        for j in range (len(shot_cord)):
            for l in range(len(enemy_cord)):
                
                # Checking to see if the shot has hit an enemy
                if enemyHit(shot_cord[j][0],enemy_cord[l][0],shot_cord[j][1],enemy_cord[l][1], enemy_cord[l][2]) == True:
                    # Increase score by 1
                    score += 1
                    # Render new score
                    text = font1.render(str(score),1,GREEN)
                    # Plays explosion sound when enemy is hit
                    explosionSound.play()

                    # add the enemies and bullets index number to the list so we can delete it later
                    enemies_Hit.append(l)
                    shots_Hit.append(j)
                    
        # sorts out the index of shots and enemies list so that it does not cause the index out of range error
        enemies_Hit.sort()
        shots_Hit.sort()
        
        # Checks to see there is any repeats in the enemies hit and shots hit (Ex. 1 shot hits 2 enemies, that one shot will appear twice in shots_hit so we have to remove the repeated
        # hit because you cannot delete the shot twice from the list)
        enemies_Hit = removeRepeats(enemies_Hit)
        shots_Hit = removeRepeats(shots_Hit)
        
        # runs through a loop to delete all the enemies cords and shots cords from the lists.
        while len(enemies_Hit) > 0:
            del enemy_cord[enemies_Hit.pop()]
            
        while len(shots_Hit) > 0:
            del shot_cord[shots_Hit.pop()]
         
        # Checks to see if enemy has gone off screen
        enemyOffScreen= []
        for i in range(len(enemy_cord)):
            if enemy_cord[i][1] > MAX_SCREEN_LENGTH:
                enemyOffScreen.append(i)
                score -= 1
                text = font1.render(str(score),1,GREEN)
                
        # Deletes the enemies off screen
        for i in range(len(enemyOffScreen)):
            del enemy_cord[enemyOffScreen[i]]
            
              
         
        # Decesnding the shots
        for i in range(len(star)):
            star [i][1] += 1
        # Checks to see if stars are off the page , redraws back at top, creates a scrolling efffect
        for i in range(len(star)):
            if star[i][1] - star[i][2] >= MAX_SCREEN_LENGTH:
                star [i][0] = randint(3,497)
                star [i][1] = 0
                star [i][2] = randint(1,3)
                
                
         
                
         
        
        screen.fill(BLACK)
        # Draws the stars 
        for i in range(len(star)):
            drawStar(star[i][0],star[i][1],star[i][2])          
        # Draws spaceship, shots, and enemies
        spaceship(spaceshipX,spaceshipY)
                 
        for num in range(len(shot_cord)):
            shot(shot_cord[num][0],shot_cord[num][1])
        for i in range(len(enemy_cord)):    
            enemy(enemy_cord[i][0],enemy_cord[i][1],enemy_cord[i][2])    
        
             
    
        # Outputs score on screen
        screen.blit(text,Rect(0,0,30,30)) 
        
                
        display.flip()
        myClock.tick(60)


while running1:
    game()

  
quit()
