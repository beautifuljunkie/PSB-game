import pygame
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

#game window
bottom_panel = 246
screen_width = 1311
screen_height = 512 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')



#define fonts
font = pygame.font.SysFont('Times New Roman', 26)



#load images
#background image
background_img = pygame.image.load('img/Background/background.png').convert_alpha()
#panel image
panel_img = pygame.image.load('img/Icons/panel.png').convert_alpha()

#function for drawing background
def draw_bg():
	screen.blit(background_img, (0, 0))


#function for drawing panel
def draw_panel():
	screen.blit(panel_img, (0, screen_height - bottom_panel))
	
class Warrior():
	def __init__(self, x, y, name, max_hp, strength, potions):
		self.name = name
		self.max_hp = 100
		self.hp = max_hp
		self.strength = strength
		self.start_potions = potions
		self.potions = potions
		self.alive = True
		img = pygame.image.load(f'img/{self.name}/Idle/0.png')
		self.image = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

class Tanker():
	def __init__(self, x, y, name, max_hp, strength, potions):
		self.name = name
		self.max_hp = 100
		self.hp = max_hp
		self.strength = strength
		self.start_potions = potions
		self.potions = potions
		self.alive = True
		img = pygame.image.load(f'img/{self.name}/Idle/0.png')
		self.image = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		
		def draw(self):
			screen.blit(self.image, self.rect)
		
warrior = Warrior(200, 260, 'Warrior', 30, 10, 3)
tanker = Tanker(200, 260, 'Tanker', 30, 10, 3)
wizard = Warrior(550, 270, 'Wizard', 20, 6, 1)
worm = Tanker(700, 270, 'Worm', 20, 6, 1)
		
run = True
while run:

	clock.tick(fps)

	#draw background
	draw_bg()

	#draw panel
	draw_panel()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()

