import random

words = [
    "future", "system", "network", "project", "vision",
    "energy", "signal", "process", "digital", "memory"
]

for _ in range(10):
    print(" ".join(random.choices(words, k=random.randint(5, 12))))