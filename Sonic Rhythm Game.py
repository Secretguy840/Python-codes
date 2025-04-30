import time, random
notes = [random.choice(["A", "S", "D"]) for _ in range(20)]
print("Hit the notes as they appear (A/S/D)!")
for note in notes:
    print(f"\n{note}")
    start = time.time()
    if input().upper() != note: print("Miss!"); break
    delay = time.time() - start
    print(f"{delay:.2f}s")
print("Score:", len(notes))
