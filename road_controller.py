from modeles.road_modele import Road
from window import Window
from modeles.constant import default_number_of_lane,curve_width,road_width,line_width, canvas_height, canvas_width

class Road_controller():

    nb_of_lane = default_number_of_lane

    def __init__(self, road_size,nb_of_lines, window):
        self.road = Road(road_size,nb_of_lines)
        self.window = window
        self.nb_of_lines = nb_of_lines
        self.determine_origins_of_sections()
        self.end_road()

    def determine_origins_of_sections(self):
        for i in range (self.road.nb_of_sections -1):
            information = self.road.get_information_of_section(i) #section_type, x1, y1, length, direction, next_section
            if information[0] == 0:
                self.determine_origin_for_vertical(information[1],information[2],information[3],information[4],information[5])
            elif information[0] == 1:
                self.determine_origin_for_horizontal(information[1],information[2],information[3],information[4],information[5])
            else:
                information = self.road.get_information_of_section_curve(i+1)
                if information[0] == 0:
                    self.determine_origin_curve_next_vertical(information[1],information[2],information[3],information[4],information[5])
                elif information [0] == 1:
                    self.determine_origin_curve_next_horizontal(information[1],information[2],information[3],information[4],information[5])
                else:
                    self.determine_origin_curve_next_curve(self.road.origin_x_of_sections[i],
                                                           self.road.origin_y_of_sections[i],
                                                           self.road.direction_of_sections[i],
                                                           self.road.direction_of_sections[i+1],
                                                           self.road.list_of_sections[i])

    def determine_origin_for_horizontal(self, x1, y1, length, direction, next_section):
        x2 = x1 + length*direction
        if next_section == 1:
            y2 = y1
        elif next_section == 2 or next_section == 3:
            origin_south = self.road.nb_of_lines * road_width + line_width*(self.road.nb_of_lines+1) + curve_width
            y2 = y1 + origin_south
        elif next_section == 4 or next_section == 5:
            origin_north = curve_width + line_width
            y2 = y1 - origin_north
        self.road.add_origin_x(x2)
        self.road.add_origin_y(y2)
        
    def determine_origin_for_vertical(self, x1, y1, length, direction, next_section):
        if next_section == 0:
            x2 = x1
        elif next_section == 3 or next_section == 4:
            origin_east = self.road.nb_of_lines * road_width + line_width*(self.road.nb_of_lines+1) + curve_width
            x2 = x1 + origin_east
        elif next_section == 2 or next_section == 5:
            origin_west = curve_width + line_width
            x2 = x1 - origin_west
        y2 = y1 + length*direction
        self.road.add_origin_x(x2)
        self.road.add_origin_y(y2)

    def determine_origin_curve_next_horizontal(self, x1, y1, length, direction, previous_section):
        x2 = x1 + length*(direction-1)
        if previous_section == 1:
            y2 = y1
        elif previous_section == 2 or previous_section == 3:
            origin_south = self.road.nb_of_lines * road_width + line_width*(self.road.nb_of_lines+1) + curve_width
            y2 = y1 - origin_south
        elif previous_section == 4 or previous_section == 5:
            origin_north = curve_width + line_width
            y2 = y1 + origin_north
        self.road.add_origin_x(x2)
        self.road.add_origin_y(y2)

    def determine_origin_curve_next_vertical(self, x1, y1, length, direction, previous_section):
        if previous_section == 0:
            x2 = x1
        elif previous_section == 3 or previous_section == 4:
            origin_east = self.road.nb_of_lines * road_width + line_width*(self.road.nb_of_lines+1) + curve_width
            x2 = x1 + origin_east
        elif previous_section == 2 or previous_section == 5:
            origin_west = curve_width + line_width
            x2 = x1 + origin_west
        y2 = y1 + length*(direction-1)
        self.road.add_origin_x(x2)
        self.road.add_origin_y(y2)

    def determine_origin_curve_next_curve(self, x1, y1, direction1, direction2, section):
        if direction1 == direction2:
            self.road.add_origin_x(x1)
            self.road.add_origin_y(y1)
            return
        x2 = x1
        y2 = y1
        offset = 2 * curve_width + self.nb_of_lines*road_width + (self.nb_of_lines + 2) * line_width
        if (section == 2 and direction1 == 0) or (section == 5 and direction1 == 1):
            x2 += offset
        elif (section == 4 and direction1 == 0) or (section == 3 and direction1 == 1):
            x2 -= offset
        elif (section == 4 and direction1 == 0) or (section == 5 and direction1 == 0):
            y2 += offset
        elif (section == 2 and direction1 == 1) or (section == 3 and direction1 == 0):
            y2 -= offset
        self.road.add_origin_x(x2)
        self.road.add_origin_y(y2)
    
    def end_road(self):
        if (self.road.list_of_sections[-1] == 0) and (self.road.direction_of_sections[-1] == 1):
            self.road.length_of_sections[-1] = canvas_height - self.road.origin_y_of_sections[-1]
        elif (self.road.list_of_sections[-1] == 0) and (self.road.direction_of_sections[-1] == 0):
            self.road.origin_y_of_sections[-1] = 0
            self.road.length_of_sections[-1] = self.road.origin_y_of_sections[-2]
        elif (self.road.list_of_sections[-1] == 1) and (self.road.direction_of_sections[-1] == 1):
            self.road.length_of_sections[-1] = canvas_width - self.road.origin_x_of_sections[-1]
        elif (self.road.list_of_sections[-1] == 1) and (self.road.direction_of_sections[-1] == 0):
            self.road.origin_x_of_sections[-1] = 0
            self.road.length_of_sections[-1] = self.road.origin_x_of_sections[-2]

    def draw_road(self):
        for i in range(self.road.nb_of_sections):
            x = self.road.origin_x_of_sections[i]
            y = self.road.origin_y_of_sections[i]
            length = self.road.length_of_sections[i]
            section_type = self.road.get_section_type(i)
            if section_type == 0:
                self.window.draw_vertical_road(x,y,length,self.nb_of_lines)
            elif section_type == 1:
                self.window.draw_horizontal_road(x,y,length,self.nb_of_lines)
            else:
                angle = 90*(section_type-2)
                self.window.draw_curve(x,y,angle,self.nb_of_lines)

    def get_road_information(self, section_index):
        return self.road.list_of_sections[section_index], self.road.direction_of_sections[section_index], self.road.length_of_sections[section_index]

