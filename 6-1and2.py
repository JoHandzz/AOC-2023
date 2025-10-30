import math

"""
Time:        54     70     82     75
Distance:   239   1142   1295   1253
"""

data_parced = [
    (54,239),
    (70,1142),
    (82,1295),
    (75,1253)
]  


def quadtratic(goal_time, dis):
    a = -1
    b = goal_time - 0.001
    c = -dis

    d = (b**2) - (4*a*c)

    sol1 = (-b - math.sqrt(d)) / (2*a)
    sol2 = (-b + math.sqrt(d)) / (2*a)

    return math.floor(sol1) - math.ceil(sol2) + 1

my_val = 1
for time, dis in data_parced:
    my_val *= quadtratic(time,dis)
    
print(my_val)



print(quadtratic(54708275, 239114212951253))

