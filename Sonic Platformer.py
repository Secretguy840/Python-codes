import pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))
sonic = pygame.Rect(50, 300, 20, 40))
platforms = [pygame.Rect(0, 350, 600, 50)), pygame.Rect(200, 250, 100, 20))]
vel_y = 0

while True:
    screen.fill((135, 206, 235))
    for p in platforms: pygame.draw.rect(screen, (50, 150, 50), p)
    pygame.draw.rect(screen, (255, 200, 0), sonic)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: sonic.x -= 5
    if keys[pygame.K_RIGHT]: sonic.x += 5
    if keys[pygame.K_SPACE] and sonic.y == 300: vel_y = -15
    
    vel_y += 1  # Gravity
    sonic.y += vel_y
    if sonic.y > 300: sonic.y = 300; vel_y = 0
    
    pygame.display.update()
