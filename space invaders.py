import pygame
import random
import math
from pygame import mixer


pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,
								screen_height))

pygame.display.set_caption("Space Invaders\
By f2ddle")



score_val = 0
scoreX = 5
scoreY = 5
font = pygame.font.Font('freesansbold.ttf', 20)


game_over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
	score = font.render("Points: " + str(score_val),
						True, (255,255,255))
	screen.blit(score, (x , y ))

def game_over():
	game_over_text = game_over_font.render("GAME OVER",
										True, (255,255,255))
	screen.blit(game_over_text, (190, 250))

mixer.music.load('background.wav')
mixer.music.play(-1)

playerImage = pygame.image.load('spaceship.png')
player_X = 370
player_Y = 523
player_Xchange = 0


invaderImage = []
invader_X = []
invader_Y = []
invader_Xchange = []
invader_Ychange = []
no_of_invaders = 8

for num in range(no_of_invaders):
	invaderImage.append(pygame.image.load('alien.png'))
	invader_X.append(random.randint(64, 737))
	invader_Y.append(random.randint(30, 180))
	invader_Xchange.append(1.2)
	invader_Ychange.append(50)


bulletImage = pygame.image.load('bullet.png')
bullet_X = 0
bullet_Y = 500
bullet_Xchange = 0
bullet_Ychange = 3
bullet_state = "rest"


def isCollision(x1, x2, y1, y2):
	distance = math.sqrt((math.pow(x1 - x2,2)) +
						(math.pow(y1 - y2,2)))
	if distance <= 50:
		return True
	else:
		return False

def player(x, y):
	screen.blit(playerImage, (x - 16, y + 10))

def invader(x, y, i):
	screen.blit(invaderImage[i], (x, y))

def bullet(x, y):
	global bullet_state
	screen.blit(bulletImage, (x, y))
	bullet_state = "fire"


running = True
while running:
	
	screen.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player_Xchange = -1.7
			if event.key == pygame.K_RIGHT:
				player_Xchange = 1.7
			if event.key == pygame.K_SPACE:
			
				
				if bullet_state is "rest":
					bullet_X = player_X
					bullet(bullet_X, bullet_Y)
					bullet_sound = mixer.Sound('bullet.wav')
					bullet_sound.play()
		if event.type == pygame.KEYUP:
			player_Xchange = 0


	player_X += player_Xchange
	for i in range(no_of_invaders):
		invader_X[i] += invader_Xchange[i]

	
	if bullet_Y <= 0:
		bullet_Y = 600
		bullet_state = "rest"
	if bullet_state is "fire":
		bullet(bullet_X, bullet_Y)
		bullet_Y -= bullet_Ychange

	
	for i in range(no_of_invaders):
		
		if invader_Y[i] >= 450:
			if abs(player_X-invader_X[i]) < 80:
				for j in range(no_of_invaders):
					invader_Y[j] = 2000
					explosion_sound = mixer.Sound('explosion.wav')
					explosion_sound.play()
				game_over()
				break

		if invader_X[i] >= 735 or invader_X[i] <= 0:
			invader_Xchange[i] *= -1
			invader_Y[i] += invader_Ychange[i]
		
		collision = isCollision(bullet_X, invader_X[i],
								bullet_Y, invader_Y[i])
		if collision:
			score_val += 1
			bullet_Y = 600
			bullet_state = "rest"
			invader_X[i] = random.randint(64, 736)
			invader_Y[i] = random.randint(30, 200)
			invader_Xchange[i] *= -1

		invader(invader_X[i], invader_Y[i], i)



	if player_X <= 16:
		player_X = 16;
	elif player_X >= 750:
		player_X = 750


	player(player_X, player_Y)
	show_score(scoreX, scoreY)
	pygame.display.update()
