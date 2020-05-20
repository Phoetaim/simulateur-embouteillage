from tkinter import Canvas, Button, Frame, BOTH, Tk
from modeles.constant import road_width,line_width,curve_width,canvas_height,canvas_width,car_radius
class Window(Frame):
    
    def __init__(self):
        master = Tk()
        master.geometry("800x600")
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()
        self.stay = True

    #Creation of init_window
    def init_window(self):
        self.UI = Canvas(self.master, bg="green", height=canvas_height, width=canvas_width)

        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        quitButton = Button(self, text="Quit",command=self.client_exit)

        # placing the button on my window
        quitButton.place(x=650, y=0)
        self.UI.place(x=0,y=0)

    def client_exit(self):
        self.stay = False

    def window_update(self):
        self.master.update()
    #########################
    ######### Roads #########
    #########################
    def draw_horizontal_road(self, x,y,length, nb_of_lines):
        total_road_width=nb_of_lines * road_width + line_width * (nb_of_lines)
        self.UI.create_rectangle(x,y,x+length,y+total_road_width,outline='gray',fill='gray')
        self.UI.create_line(x,y,x+length,y,width=line_width,fill='white')
        self.UI.create_line(x,y+total_road_width,x+length,y+total_road_width,width=line_width,fill='white')
        for i in range(nb_of_lines-1):
            self.UI.create_line(x, y + (line_width+road_width) * (i+1), x + length, y + (line_width+road_width) * (i+1), width=line_width, fill='white', dash=(6, 3))
    
    def draw_vertical_road(self, x,y,length, nb_of_lines):
        total_road_width=nb_of_lines * road_width + line_width * (nb_of_lines)
        self.UI.create_rectangle(x,y,x+total_road_width,y+length,outline='gray',fill='gray')
        self.UI.create_line(x,y,x,y+length,width=line_width,fill='white')
        self.UI.create_line(x+total_road_width,y,x+total_road_width,y+length,width=line_width,fill='white')
        for i in range(nb_of_lines-1):
            self.UI.create_line(x+(line_width+road_width)*(i+1),y,x+(line_width+road_width)*(i+1),y+length,width=line_width,fill='white',dash=(6, 3))
    
    def draw_curve(self, center_x,center_y, angle, nb_of_lines):
        offset = nb_of_lines*road_width+line_width*(nb_of_lines+1) + curve_width     
        self.UI.create_arc(center_x-offset,center_y-offset,center_x+offset,center_y+offset,start = angle, extent = 90,outline = 'gray', width = line_width,fill='gray')
        self.UI.create_arc(center_x-offset,center_y-offset,center_x+offset,center_y+offset, start = angle, extent = 90, outline = 'white', width = line_width, style = 'arc')
        offset -=  (road_width + line_width)
        for _ in range (nb_of_lines -1):
            self.UI.create_arc(center_x-offset,center_y-offset,center_x+offset,center_y+offset, start = angle, extent = 90, outline = 'white', width = line_width,dash=(6, 3), style = 'arc')
            offset -=  (road_width + line_width)
        self.UI.create_arc(center_x-offset,center_y-offset,center_x+offset,center_y+offset,start = angle,extent = 90,outline = 'white',style = 'arc', width = line_width)
        offset -= line_width
        self.UI.create_arc(center_x-offset,center_y-offset,center_x+offset,center_y+offset,start = angle,extent = 90,outline = 'green', width = line_width, fill = 'green')

    ########################
    ######### Cars #########
    ########################

    def draw_car(self,x,y,color):
        self.UI.create_arc(x-car_radius,y-car_radius,x+car_radius,y+car_radius,start = 0, extent = 359, outline = color, fill = color)