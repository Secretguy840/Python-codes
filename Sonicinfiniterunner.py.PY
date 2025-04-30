import pygame, random
pygame.init()
screen = pygame.display.set_mode((800, 300))
sonic = pygame.Rect(50, 200, 30, 30)
obstacles = [pygame.Rect(800, 220, 40, 80)]
clock = pygame.time.Clock()
score = 0

while True:
    screen.fill((135, 206, 235))  # Sky blue
    for event in pygame.event.get():
        if event.type == pygame.QUIT: break
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            sonic.y -= 100  # Jump
    
    sonic.y += 5  # Gravity
    if sonic.y > 200: sonic.y = 200
    
    # Generate obstacles
    if random.random() < 0.02:
        obstacles.append(pygame.Rect(800, 220, 40, 80))
    
    # Move obstacles
    for obs in obstacles[:]:
        obs.x -= 10
        if obs.colliderect(sonic): break  # Game over
        if obs.x < -40: obstacles.remove(obs); score += 1
    
    pygame.draw.rect(screen, (255, 200, 0), sonic)  # Sonic (yellow)
    for obs in obstacles: pygame.draw.rect(screen, (200, 0, 0), obs)  # Red obstacles
    pygame.display.update()
    clock.tick(30)
