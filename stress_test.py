#Code by Sergio1260

"""
PYTHON CPU STRESS TEST
based on the sierpinsk fractal
using the chaos method
"""

import random
from time import sleep as delay
from multiprocessing import cpu_count, Process

def generate_random_point():
    vertices = [(0, 0), (1, 0), (0.5, 0.866)]
    vertex = random.choice(vertices)
    r1 = random.random()
    r2 = random.random()
    if r1 + r2 >= 1:
        r1 = 1 - r1
        r2 = 1 - r2
    point_x = vertex[0] * (1 - r1 - r2) + vertices[(vertices.index(vertex) + 1) % 3][0] * r1 + vertices[(vertices.index(vertex) + 2) % 3][0] * r2
    point_y = vertex[1] * (1 - r1 - r2) + vertices[(vertices.index(vertex) + 1) % 3][1] * r1 + vertices[(vertices.index(vertex) + 2) % 3][1] * r2
    return (point_x, point_y)

def worker():
    initial_point=generate_random_point()
    while True:
        random_vertex = random.choice([(0, 0), (1, 0), (0.5, 0.866)])
        new_point_x = (initial_point[0] + random_vertex[0]) / 2
        new_point_y = (initial_point[1] + random_vertex[1]) / 2
        initial_point = (new_point_x, new_point_y)

def main():
    proc=[]
    print("\n   PYTHON BASED CPU STRESS-TEST\n")
    delay(0.33)
    print("STARTING...",end="\r")
    for _ in range(cpu_count()):
        proc.append(Process(target=worker))
    for x in proc: x.start()
    delay(2)
    input("RUNNING. Press any key to stop . . .  ")
    for x in proc: x.terminate()

if __name__=="__main__": main()


