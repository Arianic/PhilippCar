import pygame
import time
import random


''' 
TODO:



Far future:
jump function? (sideways boxes)
auto update with esky and webdav?
look at input bugs (if even possible with pygame)
character models 

FINISHED:
background % floor
start menu 
pause & resume function
better hitboxes
sfx
'''



pygame.init()

display_width = 800
display_height = 600

pause = False
black = (0,0,0)
white = (255,255,255)
red = (150,0,0)
green = (0,150,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
car_width = 50
block_color = (53, 155, 255)
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Catcar')
clock = pygame.time.Clock()
carImg = pygame.image.load('ela3.png')
deadcatImg = pygame.image.load('sadface2.png')
dog = pygame.image.load('Capture4.png')
blood2 = pygame.image.load('blood2.png')
blood4 = pygame.image.load('blood4.png')
blood6 = pygame.image.load('blood6.png')
backgroundImg = pygame.image.load('background2.png').convert()
gameIcon = pygame.image.load('sadface5.png')
crash_sound = pygame.mixer.Sound("crashmusic.wav")
pygame.mixer.music.load("backgroundmusic.wav")
menu_music = pygame.mixer.Sound("menumusic.wav")
pygame.display.set_icon(gameIcon)
thingx1 = random.randrange(0, display_width)
thingy1 = -600


def quit_game():
	pygame.quit()
	quit()

def things_dodged(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Dodged: " + str(count), True, black)
	gameDisplay.blit(text, (0,0))

def boosts(boostcount):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Boosts left: " + str(3 - boostcount), True, black)
	gameDisplay.blit(text, (0,25))
	

def things(thingx, thingy, thingx1, thingy1):
	gameDisplay.blit(dog, (thingx, thingy))
	gameDisplay.blit(dog, (thingx1, thingy1))
    	
    
    	


def car(x,y):
	gameDisplay.blit(carImg,(x,y))

def deadcat(x1,y1):
	pass

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',60)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():

	pygame.mixer.music.stop()
	pygame.mixer.Sound.play(crash_sound)

	message_display("Hoe ben je zo slecht??")


def button(msg, x, y, w, h, ic, ac, action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x + w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
		if click[0] == 1 and action != None:
			action()
	else:
		pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

	smallText = pygame.font.Font("freesansbold.ttf", 20)
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = ((x+(w/2), y+(h/2)))
	gameDisplay.blit(textSurf, textRect)

def unpause():
	global pause
	pause = False
	pygame.mixer.music.unpause()




def paused():
	pygame.mixer.music.pause()

	

	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.blit(backgroundImg, [0, 0])
		largeText = pygame.font.Font('freesansbold.ttf',60)
		TextSurf, TextRect = text_objects("Paused", largeText)
		TextRect.center = ((display_width/2),(display_height/2))
		gameDisplay.blit(TextSurf, TextRect)

		button("Continue", 150,450,100,50, green, bright_green, unpause)
		button("Exit", 550,450,100,50, red, bright_red, quit_game)

		pygame.display.update()
		clock.tick(15)




def game_intro():
	pygame.mixer.Sound.play(menu_music)

	intro = True

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.blit(backgroundImg, [0, 0])
		largeText = pygame.font.Font('freesansbold.ttf',80)
		TextSurf, TextRect = text_objects("Catcar", largeText)
		TextRect.center = ((display_width/2),(display_height/2))
		gameDisplay.blit(TextSurf, TextRect)

		button("Start", 150,450,100,50, green, bright_green, game_loop)
		button("Exit", 550,450,100,50, red, bright_red, quit_game)

		pygame.display.update()
		clock.tick(15)


def game_loop():
	global pause
	pygame.mixer.Sound.stop(menu_music)
	pygame.mixer.music.play(-1)
	x = (display_width * 0.45)
	y = (display_height * 0.8)
	x1 = (display_width * 0.45)
	y1 = (display_height * 0.8)


	x_change = 0

	thing_startx = random.randrange(0, display_width)
	thing_starty = -600
	thing_speed = 2.5

	dodged = 0
	boostcount = 0
	gameExit = False

	while not gameExit:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_LEFT:
					if event.mod & pygame.KMOD_SHIFT and boostcount < 3:
						x_change = -15
						boostcount += 1
						boosts(boostcount)
					else:
						x_change = -5
				if event.key == pygame.K_RIGHT:
					if event.mod & pygame.KMOD_SHIFT and boostcount < 3:
						x_change = 15
						boostcount += 1
						boosts(boostcount)
					else:
						x_change = 5

				if event.key == pygame.K_a:
					if event.mod & pygame.KMOD_SHIFT and boostcount < 3:
						x_change = -15
						boostcount += 1
						boosts(boostcount)
					else:
						x_change = -5
				if event.key == pygame.K_d:
					if event.mod & pygame.KMOD_SHIFT and boostcount < 3:
						x_change = 15
						boostcount += 1
						boosts(boostcount)
					else:
						x_change = 5
				if event.key == pygame.K_p:
					pause = True
					paused()


			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or pygame.K_d:
					x_change = 0

		x += x_change
		x1 += x_change
		gameDisplay.blit(backgroundImg, [0, 0])


		things(thing_startx, thing_starty, thingx1, thing_starty-300)
		thing_starty += thing_speed
		car(x,y)
		things_dodged(dodged)
		boosts(boostcount)
		thing_width1 = thing_startx +85
		thing_height1 = thing_starty +85



		if x > display_width - car_width or x < 0:
			deadcat(x1,y1)

			crash()

		if thing_starty and thing_starty-300 > display_height:
			thing_starty = 0 - 52
			thing_startx = random.randrange(0,display_width)
			dodged += 1
			thing_speed += 0.4
		
		if thing_starty > y + 60:
			pass
		elif y < thing_starty+85:
			if x + 60 > thing_startx and x < thing_startx + 85:
				crash()
		
		if thing_starty-300 > y + 60:
			pass
		elif y < thing_starty-300+85:
			if x + 60 > thingx1 and x < thingx1 + 85:
				crash()


		
				



		pygame.display.update()
		clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()





