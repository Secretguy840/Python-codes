import curses
import random
import time

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    
    sh, sw = stdscr.getmaxyx()
    car = ["  ██████  ", " ██∙∙∙∙██ ", "██∙∙∙∙∙∙██", "██∙∙∙∙∙∙██", " ██∙∙∙∙██ ", "  ██████  "]
    road_width = 20
    road_x = sw//2 - road_width//2
    car_x = sw//2 - 5
    car_y = sh - 10
    
    obstacles = []
    score = 0
    speed = 0.1
    
    while True:
        stdscr.clear()
        
        # Draw road
        stdscr.addstr(0, road_x, "█" * road_width)
        for y in range(1, sh-1):
            stdscr.addstr(y, road_x, "█")
            stdscr.addstr(y, road_x + road_width - 1, "█")
        
        # Draw car
        for i, line in enumerate(car):
            stdscr.addstr(car_y + i, car_x, line)
        
        # Move car
        key = stdscr.getch()
        if key == curses.KEY_LEFT and car_x > road_x + 2:
            car_x -= 2
        elif key == curses.KEY_RIGHT and car_x < road_x + road_width - 12:
            car_x += 2
        
        # Add obstacles
        if random.random() < 0.05:
            obs_x = random.randint(road_x + 2, road_x + road_width - 4)
            obstacles.append([0, obs_x])
        
        # Move and draw obstacles
        for obs in obstacles[:]:
            stdscr.addstr(obs[0], obs[1], "▓▓▓")
            obs[0] += 1
            if obs[0] > sh:
                obstacles.remove(obs)
                score += 1
            
            # Collision detection
            if (obs[0] >= car_y and obs[0] < car_y + 6 and 
                obs[1] >= car_x and obs[1] < car_x + 10):
                stdscr.addstr(sh//2, sw//2 - 10, "GAME OVER! Score: {}".format(score))
                stdscr.refresh()
                time.sleep(2)
                return
        
        stdscr.addstr(0, 2, f"Score: {score}")
        stdscr.refresh()
        time.sleep(speed)
        speed = max(0.01, speed * 0.999)

curses.wrapper(main)
