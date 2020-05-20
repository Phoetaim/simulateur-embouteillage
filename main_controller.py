#!/usr/bin/python3
from tkinter import Tk
from window import Window
from road_controller import Road_controller
from modeles.constant import time_in_millis,time_interval, line_width, road_width, car_radius
from modeles.car_modele import Car

class Main_controller():
    
    def __init__(self):
        self.app = Window()
        self.max_speed = 15
        self.traffic = 30
        self.car_list = []
        self.road_controller = Road_controller('medium', 2, self.app)
        self.road_controller.draw_road() 
        self.timer = time_in_millis()
        coordonates = self.determine_car_spawn_location()
        self.car_spawn(coordonates[0],coordonates[1])
        self.main_loop()

    def main_loop(self):
        while self.app.stay:
            if time_in_millis() - self.timer > time_interval:
                self.list_car_movement()
                self.app.window_update()
                self.timer = time_in_millis()

    def list_car_movement(self):
        for index in range(len(self.car_list)):
            self.road_controller.draw_road()
            information = self.road_controller.get_road_information(self.car_list[index].current_section)
            self.car_list[index].car_movement(information[0], information[1], information[2])
            self.app.draw_car(self.car_list[index].current_x, self.car_list[index].current_y,self.car_list[index].color)

    def determine_car_spawn_location(self):
        x = 0
        y = 0
        information = self.road_controller.get_road_information(0)
        section_type = information[0]
        section_direction = information[1]
        big_offset =  line_width * (self.road_controller.nb_of_lines) + round(road_width *(self.road_controller.nb_of_lines - 0.5))
        if section_direction == 1 and section_type == 0:
            x = self.road_controller.road.origin_x_of_sections[0] + line_width + round(road_width/2)
        elif section_direction == 0 and section_type == 0:
            x = self.road_controller.road.origin_x_of_sections[0] + big_offset
        elif section_direction == 1 and section_type == 1:
            y = self.road_controller.road.origin_y_of_sections[0] + big_offset
        elif section_direction == 0 and section_type == 1:
            y = self.road_controller.road.origin_y_of_sections[0] + line_width + round(road_width/2)
        return x,y   

    def car_spawn(self,x,y):
        new_car = Car(self.max_speed, x, y)
        self.car_list.append(new_car)

    def user_exit(self):
        exit()
