import math
import tkinter as tk

CANVAS_ELEMENTS = 2


class Graph(tk.Frame): 
    """
    Graph class used to present the pie and bar views

    ...

    Attributes
    ----------
    width : int 
        width of window 
    height : int 
        height of window
    pie : tk.Canvas 
        Canvas for pie chart 
    bar : tk.Canvas 
        Canvas for bar chart 

    Methods
    -------
    create_view():
        places the canvas objects
        
    draw_pie(data):
        draws pie chart

    draw_bar(data):
        draws bar chart 
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        """
        Parameters
        ----------
        parent : tk.Frame 
            Parent frame for the Grap class 
        controller : Controller instance 
            Controller class instance to handle logic 
        """

        self.width = self.winfo_width() 
        self.height = self.winfo_height()
        self.bind("<Configure>", self.on_resize)
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        self.pie = tk.Canvas(self, bg="#F5F5F5")
        self.bar = tk.Canvas(self, bg='#F5F5F5')

    def create_view(self):
        """places the pie chart on canvas with grid manager.

        """

        self.pie.grid(row=1, column=0, sticky="nsew")
        self.bar.grid(row=1, column=1, sticky="nsew")

    def draw_pie(self, data):
        """to draw the pie chart on canvas.

        Parameters
        ----------
        data : list
            type and amount of expenditures 
        """

        self.update()
        width = self.winfo_width() / CANVAS_ELEMENTS 
        height = self.winfo_height()
        self.pie.delete("all")

        gap = 100
        self.diameter = min(width, height)-gap
        self.sw_corner = (int((width - self.diameter) / 2 ), 
                int(height - (height - self.diameter) / 2))
        self.ne_corner = (self.sw_corner[0] + self.diameter, self.sw_corner[1] - self.diameter)
        self.center = (int(self.width / 4), int(self.height / 2))
        colors = ['red', 'yellow', 'green', 'blue', 'pink', '#34f423']
        total = sum(map(lambda d: d[1], data)) 
        if total == 0:
            return
        width_scale = 360.0 / total
        wedge_start = 0
        color_index = 0

        for name, pie_val in data:
            wedge_width = pie_val * width_scale 
            wedge_width = wedge_width if wedge_width < 360 else 359.9 # edge case if only one expenditure categorie
            self.draw_wedge(wedge_start, wedge_width, colors[color_index])
            wedge_start += wedge_width
            color_index += 1

        wedge_start = 0            

        for name, pie_val in data:
            wedge_width = pie_val * width_scale
            label_angle = wedge_start + (wedge_width / 2)
            self.draw_label(label_angle, name)
            wedge_start += wedge_width
            color_index += 1

    def draw_wedge(self, start, width, color):
        """helper-method to draws the wedges of the pie chart on canvas.

        Parameters
        ----------
        start : float
            value for the start of the pie wedge
        width : float
            value for the shape of the pie wedge
        color : str
            color for the pie wedges
        """

        self.pie.create_arc(self.sw_corner[0], self.sw_corner[1], self.ne_corner[0], 
                self.ne_corner[1], start=start, extent=width, fill=color)

    def draw_label(self, angle, text):
        """helper-method to draws the labels of the pie chart on canvas.

        Parameters
        ----------
        angle : float 
            angle for the placement of the text 
        text : str
            text to display
        """

        def deg_to_coord():
            r = (self.diameter / 2) - 10
            x_offset = int(r * math.cos(math.radians(angle)).real)
            y_offset = int(r * math.sin(math.radians(angle)).real)
            return self.center[0] + x_offset, self.center[1] - y_offset

        x,y = deg_to_coord()
        self.pie.create_text(x, y, text=text)

    def draw_bar(self, data):
        """to draw the bar chart on canvas.

        Parameters
        ----------
        data : list 
            amount of expenditures and income 
        """

        colors = ['red', 'green']
        self.bar.delete("all")
        c_width = self.width / CANVAS_ELEMENTS 
        c_height = self.height 

        # The variables below size the bar graph
        padding_bottom = 20  
        padding_top = 3*padding_bottom
        y_stretch = c_height-padding_top  # The hight of the bar
        x_gap = 30  
        x_padding = 70  
        x_width = (c_width-(2*x_padding)) / 2  # The width of the bar 
        color_index = 0

        for x, y in enumerate(data):
            # Bottom left coordinate
            x0 = x * x_gap + x * x_width + x_padding
            # Top left coordinates
            y0 = c_height - (y[1] * y_stretch + padding_bottom)
            # Bottom right coordinates
            x1 = x * x_gap + x * x_width + x_width + x_padding
            # Top right coordinates
            y1 = c_height - padding_bottom
            
            self.bar.create_rectangle(x0, y0, x1, y1, fill=colors[color_index])
            self.bar.create_text(x0 + 2, y0, anchor=tk.SW, text=str(y[0]))

            color_index += 1

    def on_resize(self, event):
        """Helper Method the scale the canvas objects on window resize

        Parameters
        ----------
        event : tkinter.Event 
            event triggert to handle window resize 
        """

        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height

        self.width = wscale*self.width
        self.height = hscale*self.height

        # resize the canvases 
        self.pie.scale("all",1,0,wscale,hscale)
        self.bar.scale("all",1,0,wscale,hscale)

