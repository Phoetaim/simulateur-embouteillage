#!/usr/bin/python3
import random 
from modeles.constant import global_max_acceleration
randomint = lambda min,max: random.randint(min, max)
class Car():
    current_line = 0
    current_section = 0
    current_position = 0
    current_x = 0
    current_y = 0
    max_speed = 0
    speed = 0
    max_acceleration = 0
    acceleration = 0
    color = 'red'
    behavior = 0

    def __init__(self, max_speed, x, y):
        self.max_speed = max_speed
        self.speed = random.randint(1,self.max_speed)
        self.max_acceleration = randomint(5,global_max_acceleration)
        self.current_x = x
        self.current_y = y
        self.acceleration = 0
        self.current_line = 0
        self.current_section = 0
        
    
    def car_acceleration(self):
        if self.acceleration <= self.max_acceleration:
            self.acceleration += 1.05*abs(self.acceleration) + 1
            if self.acceleration > self.max_acceleration:
                self.acceleration = self.max_acceleration
    
    def set_car_speed(self):
        self.speed += self.acceleration
        if self.speed > self.max_speed:
                self.speed = self.max_speed

    def change_section(self):
        self.current_section += 1
        self.current_position = 0

    def car_movement(self, section_type, direction, length):
        if section_type == 0:
            self.car_vertical_movement( direction)
        elif section_type == 1:
            self.car_horizontal_movement( direction)
        
        if self.current_position >= length:
            self.change_section()

    def car_vertical_movement(self, direction):
        self.current_y += self.speed * (direction * 2 - 1)
        self.current_position = self.current_y

    def car_horizontal_movement(self,  direction):
        self.current_x += self.speed * (direction * 2 - 1)
        self.current_position = self.current_x

    def car_curve_movement(self, section_type, direction):
        pass