#!/usr/bin/python3

class Road():
    nb_of_sections = 0
    list_of_sections = []
    length_of_sections = []
    direction_of_sections = []
    nb_of_lines = 0
    first_section_start = [0,0]
    origin_x_of_sections = []
    origin_y_of_sections = []

    def __init__(self, road_size, nb_of_lines):
        self.nb_of_lines = nb_of_lines
        if (road_size == "small"):
            self.create_small_road()
        elif (road_size == "medium"):
            self.create_medium_road()
        else:
            self.create_large_road()
    def create_small_road(self):
        self.nb_of_sections = 5
        self.list_of_sections = [1,2,0,4,1] # means, horizontal, curve to south, vertical, curve to east and horizontal
        self.length_of_sections = [250,1,200,1,0]
        self.direction_of_sections = [1,0,1,1,1] # 1 : left to right, up to down and trigonometric direction else 0
        self.origin_x_of_sections.append(0)
        self.origin_y_of_sections.append(50)
    
    def create_medium_road(self):
        self.nb_of_sections = 13
        self.list_of_sections = [1,5,3,1,5,0,2,1,4,3,1,5,0] 
        self.length_of_sections = [200,1,1,20,1,50,1,150,1,1,200,1,0]
        self.direction_of_sections = [1,1,0,1,1,0,1,0,0,0,1,1,0] # 1 : left to right, up to down and trigonometric direction else 0
        self.origin_x_of_sections.append(0)
        self.origin_y_of_sections.append(500)
    
    def create_large_road(self):
        print("to implement") 

    def get_section_type(self, i):
        return self.list_of_sections[i]

    def add_origin_x(self,x):
        self.origin_x_of_sections.append(x)

    def add_origin_y(self,y):
        self.origin_y_of_sections.append(y)

    def get_information_of_section(self,i):
        section = self.list_of_sections[i]
        x = self.origin_x_of_sections[i]
        y = self.origin_y_of_sections[i]
        length = self.length_of_sections[i]
        direction = self.direction_of_sections[i]
        next_section = self.list_of_sections[i+1]
        return [section,x,y, length, direction, next_section]
    
    def get_information_of_section_curve(self,i):
        section = self.list_of_sections[i]
        x = self.origin_x_of_sections[i-1]
        y = self.origin_y_of_sections[i-1]
        length = self.length_of_sections[i]
        direction = self.direction_of_sections[i]
        previous_section = self.list_of_sections[i-1]
        return [section,x,y, length, direction, previous_section]


    