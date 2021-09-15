# one dimetional motion hence just a point moving along a line with constant acceleration
from time import sleep
import os

print("everything in SI system")
sleep(3)
os.system("clear")

initial_position = float(input("enter initial position : "))
initial_velocity = float(input("enter initial velocity : "))
acceleration = float(input("enter acceleration of point: "))
time = float(input("enter the time from where you want to track: "))

os.system("clear")

while True:
    position = initial_position+initial_velocity*time+1/2*acceleration*time*time
    velocity = initial_velocity+acceleration*time
    axis = []
    for i in range(int(position)-10, int(position)+10):
        axis.append(str(i))
    axis = " ".join(axis)

    print("position: ", position)
    print("velocity: ", velocity)
    print("time    : ", time)
    for j in range(5):
        print()
    print((len(axis)//2)*' '+"*")
    print(len(axis)*"_")
    print(axis)

    sleep(1)
    time += 1
    os.system("clear")
