import pygame
import time
import math
pygame.init()

screen = pygame.display.set_mode((500, 600))
running = True
clock = pygame.time.Clock()

GREY = (120, 123, 214)
WHITE = (255, 255 ,255)
BLACK = (0, 0, 0)
RED = (171, 54, 19)
timeless = 297

font = pygame.font.SysFont('sans', 50)
text1 = font.render('+', True, BLACK)
text2 = font.render('-', True, BLACK)
text3 = font.render('Start', True, BLACK)
text4 = font.render('Reset', True, BLACK)
total_secs = 0
Min = 0
Sec = 0
start = False
while running:
		clock.tick(60)
		screen.fill(GREY)
		mouse_x, mouse_y = pygame.mouse.get_pos()
		# ve hinh len man hinh
		pygame.draw.rect(screen, WHITE, (100, 50, 50 , 50))
		pygame.draw.rect(screen, WHITE, (200, 50, 50 , 50))
		pygame.draw.rect(screen, WHITE, (100, 200, 50 , 50))
		pygame.draw.rect(screen, WHITE, (200, 200, 50 , 50))
		pygame.draw.rect(screen, WHITE, (300, 50, 150 , 50))
		pygame.draw.rect(screen, WHITE, (300, 200, 150 , 50))
		pygame.draw.rect(screen, WHITE, (100, 500, 300 , 50))
		pygame.draw.circle(screen, WHITE, (250, 380), 100)
		pygame.draw.circle(screen, BLACK, (250, 380), 100, 3)
		pygame.draw.circle(screen, BLACK, (250, 380), 4)
		pygame.draw.rect(screen, BLACK, (100, 500, 300, 50), 4)
		# viết chu len man hinh
		screen.blit(text1, (100, 50))
		screen.blit(text1, (200, 50))
		screen.blit(text2, (100, 200))
		screen.blit(text2, (200, 200))
		screen.blit(text3, (300, 50))
		screen.blit(text4, (300, 200))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					running = False
			if event.type == pygame.MOUSEBUTTONDOWN: # 1: chuột trái, 2: con lăn, 3: chuột phải
				if event.button == 1:
					if (200 < mouse_x < 250) and (50 < mouse_y < 100):
						if total_secs + 1 > 1439:
							total_secs = 0 
						else:
							total_secs += 1
					if (100 < mouse_x < 150) and (50 < mouse_y < 100):
						if total_secs + 60 > 1439:
							total_secs = 0
						else: 
							total_secs += 60
					if (100 < mouse_x < 150) and (200 < mouse_y < 250):
						if total_secs - 60 < 0:
							total_secs = 0
						else: 
							total_secs -= 60
					if (200 < mouse_x < 250) and (200 < mouse_y < 250):
						if total_secs - 1 < 0:
							total_secs = 0
						else: 
							total_secs -= 1
					if (300 < mouse_x < 450) and (200 < mouse_y < 250):
						total_secs = 0
						timeless = 297
					if (300 < mouse_x < 450) and (50 < mouse_y < 100):
						start = True

		if start == True:
			if total_secs > 0:
				total_secs -= 1
				time.sleep(1)
			else:
				start = False
			if total_secs < 60 and total_secs != 0:
				pygame.draw.rect(screen, RED, (102, 502, int(timeless), 47))
				timeless -= timeless // total_secs
		Min = total_secs // 60
		Sec = total_secs - (Min * 60)
		text_clock = font.render(str(Min) + ':' + str(Sec), True, BLACK)
		screen.blit(text_clock, (150, 120))
		pygame.draw.line(screen, BLACK, (250, 380), (int(250 + 90 * math.sin(Sec * 6 * 3.14 / 180)), int(380 - 90 * math.cos(Sec * 6 * 3.14 / 180))))
		pygame.draw.line(screen, BLACK, (250, 380), (int(250 + 45 * math.sin(Min * 30 * 3.14 / 180)), int(380 - 45 * math.cos(Min * 30 * 3.14 / 180))))

		pygame.display.flip()

pygame.quit()