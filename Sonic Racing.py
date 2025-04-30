import pygame
pygame.init()
screen = pygame.display.set_mode((600, 800))
car = pygame.Rect(300, 700, 30, 50)
road = pygame.Rect(200, 0, 200, 800))

while True:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (100, 100, 100), road)  # Road
    pygame.draw.rect(screen, (255, 200, 0), car)   # Sonic's car
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car.x > 210: car.x -= 5
    if keys[pygame.K_RIGHT] and car.x < 360: car.x += 5
    
    pygame.display.update()
