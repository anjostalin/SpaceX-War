# GAME
import pygame
import random
import math
from pygame import mixer
import sys


def space_x_war():
    # To initialise pygame
    pygame.init()
    # Game title and icon
    pygame.display.set_caption("Space X WAR - by Anjo Stalin")
    game_icon = pygame.image.load("game_icon.png")
    pygame.display.set_icon(game_icon)
    game_running = True
    screen = pygame.display.set_mode((1500, 900))

    screen.fill((0, 0, 0))
    while game_running:
        start_image = pygame.image.load("space_x_war_image.jpg")
        screen.blit(start_image, (0, 0))
        pygame.display.update()        

        for event in pygame.event.get():             # checks the events happening in the game
            if event.type == pygame.QUIT:  
                game_running = False 
                pygame.quit()   
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    Button_sound = mixer.Sound("click_sound.wav")
                    Button_sound.play()
                    main_menu()
                    sys.exit()

music_sound="on"

def main_menu():
    # To initialise pygame
    pygame.init()
    # Game title and icon
    pygame.display.set_caption("Space X WAR - by Anjo Stalin")
    game_icon = pygame.image.load("game_icon.png")
    pygame.display.set_icon(game_icon)
    game_running = True
    screen = pygame.display.set_mode((1500, 900))

    screen.fill((0, 0, 0))
    while game_running:
        start_image = pygame.image.load("main_menu.jpg")
        screen.blit(start_image, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():             # checks the events happening in the game
            if event.type == pygame.QUIT:  
                game_running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if music_sound=="on":
                        Button_sound = mixer.Sound("click_sound.wav")
                        Button_sound.play()
                        start_game()
                        sys.exit()
                    if music_sound=="off":
                        start_game()
                        sys.exit()
                if event.key == pygame.K_s:
                    if music_sound=="on":
                        Button_sound = mixer.Sound("click_sound.wav")
                        Button_sound.play()
                        high_score()
                        sys.exit()
                    if music_sound=="off":
                        high_score()
                        sys.exit()
                if event.key == pygame.K_c:
                    if music_sound=="on":
                        Button_sound = mixer.Sound("click_sound.wav")
                        Button_sound.play()
                        controls()
                        sys.exit()
                    if music_sound=="off":
                        controls()
                        sys.exit()
                if event.key == pygame.K_h:
                    if music_sound=="on":
                        Button_sound = mixer.Sound("click_sound.wav")
                        Button_sound.play()
                        instructions2()
                        sys.exit()
                    if music_sound=="off":
                        instructions2()
                        sys.exit()                    
                if event.key == pygame.K_v:
                    if music_sound=="on":
                        Button_sound = mixer.Sound("click_sound.wav")
                        Button_sound.play()
                        sound()     
                        sys.exit()
                    if music_sound=="off":
                        sound()     
                        sys.exit()          
                if event.key == pygame.K_q:
                    #pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                    
def controls():
    # To initialise pygame
    pygame.init()
    # Game title and icon
    pygame.display.set_caption("Space X WAR - by Anjo Stalin")
    game_icon = pygame.image.load("game_icon.png")
    pygame.display.set_icon(game_icon)
    game_running = True
    screen = pygame.display.set_mode((1500, 900))

    screen.fill((0, 0, 0))
    while game_running:
        start_image = pygame.image.load("controls.jpg")
        screen.blit(start_image, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():             # checks the events happening in the game
            if event.type == pygame.QUIT:  
                game_running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_m:
                    if music_sound=="on":
                        Button_sound = mixer.Sound("click_sound.wav")
                        Button_sound.play()
                        main_menu()
                        sys.exit()
                    if music_sound=="off":
                        main_menu()
                        sys.exit()
                        
def sound():
    # To initialise pygame
    pygame.init()
    
    global music_sound
    # Game title and icon
    pygame.display.set_caption("Space X WAR - by Anjo Stalin")
    game_icon = pygame.image.load("game_icon.png")
    pygame.display.set_icon(game_icon)
    game_running = True
    screen = pygame.display.set_mode((1500, 900))

    screen.fill((0, 0, 0))
    while game_running:
        start_image = pygame.image.load("game_sound.jpg")
        screen.blit(start_image, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():             # checks the events happening in the game
            if event.type == pygame.QUIT:  
                game_running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_o:
                    Button_sound = mixer.Sound("click_sound.wav")
                    Button_sound.play()
                    music_sound="on"
                    main_menu()
                    sys.exit()
                if event.key == pygame.K_f:
                    music_sound="off"
                    main_menu()
                    sys.exit()
                    
def high_score():
    # To initialise pygame
    pygame.init()   
    
    # Game title and icon
    pygame.display.set_caption("Space X WAR - by Anjo Stalin")
    game_icon = pygame.image.load("game_icon.png")
    pygame.display.set_icon(game_icon)
    game_running = True          
    screen = pygame.display.set_mode((1500, 900))
    screen.fill((0, 0, 0))    
    
    while game_running:
        start_image = pygame.image.load("high_score.jpg")
        screen.blit(start_image, (0, 0))        
        myfile=open("MAIN SCORE.txt","r")
        real_high_score1=myfile.read()
        real_high_score=int(real_high_score1)
        myfile.close()
        
        if real_high_score>999:
            high_score_font = pygame.font.Font("IntegralCF-DemiBold.otf", 140)
            high_score_text = high_score_font.render(
                "High Score : " + str(real_high_score), True, (255, 255, 255))        #255, 255, 255
            screen.blit(high_score_text, (40, 305))
        elif real_high_score<1000 and real_high_score>99:
            high_score_font = pygame.font.Font("IntegralCF-DemiBold.otf", 150)
            high_score_text = high_score_font.render(
                "High Score : " + str(real_high_score), True, (255, 255, 255))        #255, 255, 255
            screen.blit(high_score_text, (45, 295))        
        else:
            high_score_font = pygame.font.Font("IntegralCF-DemiBold.otf", 160)
            high_score_text = high_score_font.render(
                "High Score : " + str(real_high_score), True, (255, 255, 255))        #255, 255, 255
            screen.blit(high_score_text, (55, 290))
               
        
        pygame.display.update()

        for event in pygame.event.get():             # checks the events happening in the game
            if event.type == pygame.QUIT: 
                game_running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_m:
                    if music_sound=="on":
                        Button_sound = mixer.Sound("click_sound.wav")
                        Button_sound.play()
                        main_menu()
                        sys.exit()
                    if music_sound=="off":
                        main_menu()
                        sys.exit()

def instructions2():
    # To initialise pygame
    pygame.init()
    # Game title and icon
    pygame.display.set_caption("Space X WAR - by Anjo Stalin")
    game_icon = pygame.image.load("game_icon.png")
    pygame.display.set_icon(game_icon)
    game_running = True
    screen = pygame.display.set_mode((1500, 900))
    screen.fill((0, 0, 0))
    
    while game_running:
        start_image = pygame.image.load("instructions_2.jpg")
        screen.blit(start_image, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():             # checks the events happening in the game
            if event.type == pygame.QUIT: 
                game_running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    if music_sound=="on":
                        Button_sound = mixer.Sound("click_sound.wav")
                        Button_sound.play()
                        instructions3()
                        sys.exit()
                    if music_sound=="off":
                        instructions3()
                        sys.exit()

def instructions3():
    # To initialise pygame
    pygame.init()
    # Game title and icon
    pygame.display.set_caption("Space X WAR - by Anjo Stalin")
    game_icon = pygame.image.load("game_icon.png")
    pygame.display.set_icon(game_icon)
    game_running = True
    screen = pygame.display.set_mode((1500, 900))
    screen.fill((0, 0, 0))
    
    while game_running:
        start_image = pygame.image.load("instructions_3.jpg")
        screen.blit(start_image, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():             # checks the events happening in the game
            if event.type == pygame.QUIT:
                game_running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_m:
                    if music_sound=="on":
                        Button_sound = mixer.Sound("click_sound.wav")
                        Button_sound.play()
                        main_menu()
                        sys.exit()
                    if music_sound=="off":
                        main_menu()
                        sys.exit()

def start_game():
    # To initialise pygame
    pygame.init()
    global music_sound    
    # Game title and icon
    pygame.display.set_caption("Space X WAR - by Anjo Stalin")
    game_icon = pygame.image.load("game_icon.png")
    pygame.display.set_icon(game_icon)
    game_running = True
    screen = pygame.display.set_mode((1500, 900))
    screen.fill((0, 0, 0))
    
    while game_running:
        start_image = pygame.image.load("start_game.png")
        screen.blit(start_image, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():             # checks the events happening in the game
            if event.type == pygame.QUIT:  
                game_running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_s:
                    if music_sound=="on":                        
                        run_game()
                        sys.exit()
                    if music_sound=="off":
                        run_game1()
                        sys.exit()
                        
Bullet_state = "Ready"

myfile=open("MAIN SCORE.txt","r")
real_high_score1=myfile.read()
real_high_score=int(real_high_score1)
myfile.close()

def run_game():
    print("rungame")  

    # To initialise pygame
    pygame.init()

    # To create game screen      width(x),height(y)
    screen = pygame.display.set_mode((1500, 900))

    # Background image
    background_image = pygame.image.load("background.jpg")

    # Backgound sound
    mixer.music.load("background.wav")
    mixer.music.play(-1)

    # Game title and icon
    pygame.display.set_caption("Space X WAR - by Anjo Stalin")
    game_icon = pygame.image.load("game_icon.png")
    pygame.display.set_icon(game_icon)

    # Game player
    game_player = pygame.image.load("game_player.png")  # creating player
    # player coordinates
    player_Xaxis = 718
    player_Yaxis = 780
    player_Xaxis_change = 0

    # Enemies
    enemyImage = []
    enemy_Xaxis = []
    enemy_Yaxis = []
    enemy_Xaxis_change = []
    enemy_Yaxis_change = []
    number_of_enemies = 30
    for i in range(number_of_enemies):
        enemyImage.append(pygame.image.load("enemy.png"))  # creating enemy
        # enemy coordinates
        # to create random starting positions for the enemy in the x axis
        enemy_Xaxis.append(random.randint(0, 1435))
        # to create random starting positions for the enemy in the y axis
        enemy_Yaxis.append(random.randint(80, 450))
        enemy_Xaxis_change.append(2)  
        enemy_Yaxis_change.append(40)

    # Bullet
    # creating bullet
    BulletImage = pygame.image.load("bullet.png")
    # bullet coordinates
    Bullet_Xaxis = 0  # to create random starting positions for the enemy in the x axis
    Bullet_Yaxis = 780  # to create random starting positions for the enemy in the y axis
    Bullet_Xaxis_change = 0
    Bullet_Yaxis_change = 10
    # Ready means the bullet is behind the spaceship i.e. its not fired
    global Bullet_state
    # Fire means the bullet is fired and we can see it

    # Game score
    global game_score
    game_score = 0
    score_font = pygame.font.Font("IntegralCF-DemiBold.otf", 40)
    score_text_Xaxis = 30
    score_text_Yaxis = 15    

    def player_score(x, y):
        score = score_font.render(
            "Score : " + str(game_score), True, (255, 255, 255))
        screen.blit(score, (x, y))   
    
    def player_high_score(x, y):        
        high_score_text = score_font.render(
            "High Score : " + str(real_high_score), True, (255, 255, 255))        #255, 255, 255
        screen.blit(high_score_text, (x, y))       
        
    def level_text(x, y):       
        level = score_font.render(
            "LEVEL : " + str(1), True, (255, 255, 255))
        screen.blit(level, (x, y))

    def player_position(x, y):
        screen.blit(game_player, (x, y))

    def enemy_position(x, y, i):
        screen.blit(enemyImage[i], (x, y))

    def bullet_fire(x, y):
        global Bullet_state
        Bullet_state = "Fire"
        screen.blit(BulletImage, (x+16, y+10))

    def collision(enemy_Xaxis, enemy_Yaxis, Bullet_Xaxis, Bullet_Yaxis):
        #distance=math.sqrt((math.pow(enemy_Xaxis-Bullet_Xaxis,2)) +(math.pow(enemy_Yaxis-Bullet_Yaxis,2)))
        # distance=math.sqrt((enemy_Xaxis-Bullet_Xaxis)**2+(enemy_Yaxis-Bullet_Yaxis)**2)       #To check the distance between the bullet and the enemy, if very less the bullet has hit the enemy and the score increases
        distance = math.sqrt(math.pow(enemy_Xaxis - Bullet_Xaxis, 2) +
                             (math.pow(enemy_Yaxis - Bullet_Yaxis, 2)))
        if distance < 20:
            return True
        else:
            return False
    #distance=math.sqrt((math.pow(enemy_Xaxis-Bullet_Xaxis,2)) +(math.pow(enemy_Yaxis-Bullet_Yaxis,2)))
    # D=sqrt((x2-x1)**2+(y2-y1)**2)

    # Game loop
    game_running = True
    while game_running:

        #            R,G,B (Red, Green, Blue)
        # all other things to be added in the game should be after this line because this is the main background screen
        screen.fill((0, 0, 0))

        # Background image
        screen.blit(background_image, (0, 0))

        for event in pygame.event.get():  # checks the events happening in the game
            if event.type == pygame.QUIT:
                game_running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_running = False
                    pygame.quit()
                    sys.exit()                

            # checking if the key pressed is left arrow key or right arrow key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_Xaxis_change = -1  # moving player to the left
                if event.key == pygame.K_RIGHT:
                    player_Xaxis_change = +1  # moving player to the right
                if event.key == pygame.K_UP:
                    if Bullet_state == "Ready":
                        Bullet_sound = mixer.Sound("laser.wav")
                        Bullet_sound.play()
                        # To get the x coordinate of the spaceship
                        Bullet_Xaxis = player_Xaxis
                        bullet_fire(Bullet_Xaxis, Bullet_Yaxis)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_Xaxis_change = 0

        player_Xaxis += player_Xaxis_change  # moving player to the left or right

    # Giving boundaries to the spaceship so that it doesn't go out of the screen
        if player_Xaxis <= 0:
            player_Xaxis = 0
        elif player_Xaxis >= 1436:
            player_Xaxis = 1436

        for i in range(number_of_enemies):

            # Game Over
            if enemy_Yaxis[i] > 720:
                for j in range(number_of_enemies):
                    enemy_Yaxis[j] = 2000
                    player_Xaxis = 5000
                    Bullet_Xaxis = 5000                                    
                mixer.music.stop()
                game_over_sound = mixer.Sound("game_over_sound.wav")
                game_over_sound.play()
                
                global real_high_score                
                
                if game_score>real_high_score:
                    myfile1=open("MAIN SCORE.txt","w")
                    myfile1.write(str(game_score))
                    myfile1.close()
                    print("NEW HIGH SCORE CREATED")
                    restart_game1()
                    sys.exit()
                else:
                    print("HIGH SCORE UNBREAKABLE")
                    restart_game2()
                    sys.exit()        

            enemy_Xaxis[i] += enemy_Xaxis_change[i]

    # Giving boundaries to the enemy so that it doesn't go out of the screen
            if enemy_Xaxis[i] <= 0:
                enemy_Xaxis_change[i] = 2
                enemy_Yaxis[i] += enemy_Yaxis_change[i]
            elif enemy_Xaxis[i] >= 1436:
                enemy_Xaxis_change[i] = -2
                enemy_Yaxis[i] += enemy_Yaxis_change[i]

            # Collision checking
            col = collision(enemy_Xaxis[i], enemy_Yaxis[i],
                            Bullet_Xaxis, Bullet_Yaxis)
            if col:
                Collision_sound = mixer.Sound("explosion.wav")
                Collision_sound.play()
                Bullet_Yaxis = 780
                Bullet_state = "Ready"
                game_score += 10               
                
                myfile2=open("NEW SCORE.txt","w")
                myfile2.write(str(game_score))
                myfile2.close()

                print(game_score)          
                
                enemy_Xaxis[i] = random.randint(0, 1435)
                enemy_Yaxis[i] = random.randint(50, 250)

            # calling the enemy_position function
            enemy_position(enemy_Xaxis[i], enemy_Yaxis[i], i)

        # Bullet movement
        if Bullet_Yaxis <= 0:
            Bullet_Yaxis = 780
            Bullet_state = "Ready"
        if Bullet_state == "Fire":
            bullet_fire(Bullet_Xaxis, Bullet_Yaxis)
            Bullet_Yaxis -= Bullet_Yaxis_change

        # calling the player_position function
        player_position(player_Xaxis, player_Yaxis)

        player_score(score_text_Xaxis, score_text_Yaxis)      
        
        player_high_score(570, score_text_Yaxis)        
        
        level_text(1260, score_text_Yaxis)       

        pygame.display.update()  # to update everything that's happening in the screen

def run_game1():
    print("rungame1")   

    # To initialise pygame
    pygame.init()

    # To create game screen      width(x),height(y)
    screen = pygame.display.set_mode((1500, 900))

    # Background image
    background_image = pygame.image.load("background.jpg")

    # Game title and icon
    pygame.display.set_caption("Space X WAR - by Anjo Stalin")
    game_icon = pygame.image.load("game_icon.png")
    pygame.display.set_icon(game_icon)

    # Game player
    game_player = pygame.image.load("game_player.png")  # creating player
    # player coordinates
    player_Xaxis = 718
    player_Yaxis = 780
    player_Xaxis_change = 0

    # Enemies
    enemyImage = []
    enemy_Xaxis = []
    enemy_Yaxis = []
    enemy_Xaxis_change = []
    enemy_Yaxis_change = []
    number_of_enemies = 30
    for i in range(number_of_enemies):
        enemyImage.append(pygame.image.load("enemy.png"))  # creating enemy
        # enemy coordinates
        # to create random starting positions for the enemy in the x axis
        enemy_Xaxis.append(random.randint(0, 1435))
        # to create random starting positions for the enemy in the y axis
        enemy_Yaxis.append(random.randint(80, 450))
        enemy_Xaxis_change.append(2)  
        enemy_Yaxis_change.append(40)

    # Bullet
    # creating bullet
    BulletImage = pygame.image.load("bullet.png")
    # bullet coordinates
    Bullet_Xaxis = 0  # to create random starting positions for the enemy in the x axis
    Bullet_Yaxis = 780  # to create random starting positions for the enemy in the y axis
    Bullet_Xaxis_change = 0
    Bullet_Yaxis_change = 10
    # Ready means the bullet is behind the spaceship i.e. its not fired
    global Bullet_state
    # Fire means the bullet is fired and we can see it

    # Game score
    global game_score
    game_score = 0
    score_font = pygame.font.Font("IntegralCF-DemiBold.otf", 40)
    score_text_Xaxis = 30
    score_text_Yaxis = 15   

    def player_score(x, y):
        score = score_font.render(
            "Score : " + str(game_score), True, (255, 255, 255))
        screen.blit(score, (x, y))   
    
    def player_high_score(x, y):       
        high_score_text = score_font.render(
            "High Score : " + str(real_high_score), True, (255, 255, 255))        #255, 255, 255
        screen.blit(high_score_text, (x, y))       
        
    def level_text(x, y):       
        level = score_font.render(
            "LEVEL : " + str(1), True, (255, 255, 255))
        screen.blit(level, (x, y))

    def player_position(x, y):
        screen.blit(game_player, (x, y))

    def enemy_position(x, y, i):
        screen.blit(enemyImage[i], (x, y))

    def bullet_fire(x, y):
        global Bullet_state
        Bullet_state = "Fire"
        screen.blit(BulletImage, (x+16, y+10))

    def collision(enemy_Xaxis, enemy_Yaxis, Bullet_Xaxis, Bullet_Yaxis):
        #distance=math.sqrt((math.pow(enemy_Xaxis-Bullet_Xaxis,2)) +(math.pow(enemy_Yaxis-Bullet_Yaxis,2)))
        # distance=math.sqrt((enemy_Xaxis-Bullet_Xaxis)**2+(enemy_Yaxis-Bullet_Yaxis)**2)       #To check the distance between the bullet and the enemy, if very less the bullet has hit the enemy and the score increases
        distance = math.sqrt(math.pow(enemy_Xaxis - Bullet_Xaxis, 2) +
                             (math.pow(enemy_Yaxis - Bullet_Yaxis, 2)))
        if distance < 20:
            return True
        else:
            return False
    #distance=math.sqrt((math.pow(enemy_Xaxis-Bullet_Xaxis,2)) +(math.pow(enemy_Yaxis-Bullet_Yaxis,2)))
    # D=sqrt((x2-x1)**2+(y2-y1)**2)

    # Game loop
    game_running = True
    while game_running:

        #            R,G,B (Red, Green, Blue)
        # all other things to be added in the game should be after this line because this is the main background screen
        screen.fill((0, 0, 0))

        # Background image
        screen.blit(background_image, (0, 0))

        for event in pygame.event.get():  # checks the events happening in the game
            if event.type == pygame.QUIT:
                game_running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_running = False
                    pygame.quit()
                    sys.exit()        

            # checking if the key pressed is left arrow key or right arrow key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_Xaxis_change = -1  # moving player to the left
                if event.key == pygame.K_RIGHT:
                    player_Xaxis_change = +1  # moving player to the right
                if event.key == pygame.K_UP:
                    if Bullet_state == "Ready":
                        # To get the x coordinate of the spaceship
                        Bullet_Xaxis = player_Xaxis
                        bullet_fire(Bullet_Xaxis, Bullet_Yaxis)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_Xaxis_change = 0

        player_Xaxis += player_Xaxis_change  # moving player to the left or right

    # Giving boundaries to the spaceship so that it doesn't go out of the screen
        if player_Xaxis <= 0:
            player_Xaxis = 0
        elif player_Xaxis >= 1436:
            player_Xaxis = 1436

        for i in range(number_of_enemies):
            # Game Over
            if enemy_Yaxis[i] > 720:
                for j in range(number_of_enemies):
                    enemy_Yaxis[j] = 2000
                    player_Xaxis = 5000
                    Bullet_Xaxis = 5000 
                
                global real_high_score                
                
                if game_score>real_high_score:
                    myfile1=open("MAIN SCORE.txt","w")
                    myfile1.write(str(game_score))
                    myfile1.close()
                    print("NEW HIGH SCORE CREATED")
                    restart_game1()
                    sys.exit()
                else:
                    print("HIGH SCORE UNBREAKABLE")
                    restart_game2()
                    sys.exit()          

            enemy_Xaxis[i] += enemy_Xaxis_change[i]

    # Giving boundaries to the enemy so that it doesn't go out of the screen
            if enemy_Xaxis[i] <= 0:
                enemy_Xaxis_change[i] = 2
                enemy_Yaxis[i] += enemy_Yaxis_change[i]
            elif enemy_Xaxis[i] >= 1436:
                enemy_Xaxis_change[i] = -2
                enemy_Yaxis[i] += enemy_Yaxis_change[i]

            # Collision checking
            col = collision(enemy_Xaxis[i], enemy_Yaxis[i],
                            Bullet_Xaxis, Bullet_Yaxis)
            if col:
                Bullet_Yaxis = 780
                Bullet_state = "Ready"
                game_score += 10           
                
                myfile2=open("NEW SCORE.txt","w")
                myfile2.write(str(game_score))
                myfile2.close()

                print(game_score)               
                
                enemy_Xaxis[i] = random.randint(0, 1435)
                enemy_Yaxis[i] = random.randint(50, 250)

            # calling the enemy_position function
            enemy_position(enemy_Xaxis[i], enemy_Yaxis[i], i)

        # Bullet movement
        if Bullet_Yaxis <= 0:
            Bullet_Yaxis = 780
            Bullet_state = "Ready"
        if Bullet_state == "Fire":
            bullet_fire(Bullet_Xaxis, Bullet_Yaxis)
            Bullet_Yaxis -= Bullet_Yaxis_change

        # calling the player_position function
        player_position(player_Xaxis, player_Yaxis)

        player_score(score_text_Xaxis, score_text_Yaxis)        
        
        player_high_score(570, score_text_Yaxis)        
        
        level_text(1260, score_text_Yaxis)      

        pygame.display.update()  # to update everything that's happening in the screen

def restart_game1():
    # To initialise pygame
    pygame.init()
    global music_sound
    global real_high_score
    global game_score
    real_high_score = game_score
    # Game title and icon
    pygame.display.set_caption("Space X WAR - by Anjo Stalin")
    game_icon = pygame.image.load("game_icon.png")
    pygame.display.set_icon(game_icon)
    game_running = True
    screen = pygame.display.set_mode((1500, 900))
    screen.fill((0, 0, 0))
    
    while game_running:
        restart_image = pygame.image.load("restart1.jpg")
        screen.blit(restart_image, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():             # checks the events happening in the game
            if event.type == pygame.QUIT:  
                game_running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    if music_sound=="on":
                        run_game()
                        sys.exit()
                    if music_sound=="off":
                        run_game1()
                        sys.exit()    
                    
def restart_game2():
    # To initialise pygame
    pygame.init()
    global music_sound
    # Game title and icon
    pygame.display.set_caption("Space X WAR - by Anjo Stalin")
    game_icon = pygame.image.load("game_icon.png")
    pygame.display.set_icon(game_icon)
    game_running = True
    screen = pygame.display.set_mode((1500, 900))
    screen.fill((0, 0, 0))
    
    while game_running:
        restart_image = pygame.image.load("restart2.jpg")
        screen.blit(restart_image, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():             # checks the events happening in the game
            if event.type == pygame.QUIT:
                game_running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    if music_sound=="on":
                        run_game()
                        sys.exit()
                    if music_sound=="off":
                        run_game1()
                        sys.exit()

space_x_war()

