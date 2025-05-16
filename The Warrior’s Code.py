def conquer_goals():
    obstacles = ["fear", "doubt", "procrastination"]
    while True:
        for obstacle in obstacles:
            print(f"🔥 Smashing {obstacle.upper()}!")
            obstacles.remove(obstacle)
        if not obstacles:
            print("🚀 YOU ARE UNSTOPPABLE!")
            break

conquer_goals()
