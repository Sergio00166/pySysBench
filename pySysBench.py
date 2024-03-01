#Code by Sergio1260

"""
Python CPU benchmark (Single core + Multicore)
No dependencys (Python3)
Based on the Sierpinks Fractal's Chaos rendering method
"""

import random
from multiprocessing import cpu_count, Process, Pool
from time import time
from time import sleep as delay
from sys import argv

class worker:
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
        return point_x, point_y

    def generate_additional_points(initial_point, range):
        for _ in range:
            random_vertex = random.choice([(0, 0), (1, 0), (0.5, 0.866)])
            new_point_x = (initial_point[0] + random_vertex[0]) / 2
            new_point_y = (initial_point[1] + random_vertex[1]) / 2
            initial_point = (new_point_x, new_point_y)

    def generate_parallel_points(num_processes, num_additional_points):
        initial_points = [worker.generate_random_point() for _ in range(num_processes)]
        processes = []
        for i in range(num_processes):
            initial_point = initial_points[i]
            process = Process(target=worker.generate_additional_points, args=(initial_point, num_additional_points))
            process.start()
            processes.append(process)
        start=time()
        for process in processes: process.join()
        end=time(); return end-start

class starter:   
    def benchmark(cores, sizef):
        global size, start ; size=sizef
        points=int((size*size)/cores)
        return worker.generate_parallel_points(cores, range(points))
    def stress():
        initial_point=worker.generate_random_point()
        worker.generate_additional_points(initial_point, iter(int,1))

class main:
    def benchmark():
        run=starter.benchmark
        delay(0.5); print(""); prog=""; percent=0
        print("      Python SysBench v3.0 ",end="\n\n")
        print("\r  Running Single-Core benchmark... ",end="")
        onec=str(int(1/(run(1, 5120)*13)*100000*0.7))
        print("DONE",end="");  delay(1)
        print("\r"+" "*64,end="")
        print("\r  Running Multi-Core benchmark... ",end="")
        allc=str(int(1/run(cpu_count(), 16384)*100000*0.7))
        print("DONE",end="")
        delay(1)
        print("\r"+" "*64+"\r      Printing results... ",end="")
        delay(1.5)
        print("\r   Single-Core performance: "+onec+" "*42)
        print("   Multi-Core  performance: "+allc+"\n")

    def stress():
        proc=[]
        print("\n   PYTHON BASED CPU STRESS-TEST\n")
        delay(0.33)
        print("STARTING...",end="\r")
        for _ in range(cpu_count()):
            proc.append(Process(target=starter.stress))
        for x in proc: x.start()
        delay(2)
        input("RUNNING. Press any key to stop . . .  ")
        for x in proc: x.terminate()

if __name__=="__main__":
    if not len(argv)==1:
        arg=argv[1]
        if arg=="stress":
            main.stress()
        elif arg=="bench":
            main.benchmark()
        else: print("\n   BAD ARGUMENT\n")
    else: main.benchmark()
