#!/usr/bin/python3
import time

#time
time_in_millis = lambda: int(round(time.time() * 1000))
fps = 30
time_interval = round(1000/30)
#window
window_width = 800
window_height = 600
canvas_width = 600
canvas_height = 600
#Road
road_width = 20
line_width = 3

default_number_of_lane = 3
curve_width = 1.5 * road_width
type_of_road = {'straight_vertical', 'straight_horizontal', 'curve_0','curve_90','curve_180', 'curve_270'}
#Cars

car_radius = road_width//2 -line_width
global_max_acceleration = 30