# Data Visualization Backend Designer (DVBD)
# Justin Pizano

# Import Libraries
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.figure import Figure
import matplotlib.colors as pltcolors

# Module "inputter" can be found on GitHub through jp21jp41
import inputter

hex_strings = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
               "A", "B", "C", "D", "E", "F"]

def hex_to_rgba(hex_value, a = 1):
    try:
        r1 = (hex_strings.index(hex_value[1]) 
              + hex_strings.index(hex_value[2]) * 16) / 256
        g1 = (hex_strings.index(hex_value[3]) 
        + hex_strings.index(hex_value[4]) * 16) / 256
        b1 = (hex_strings.index(hex_value[5]) 
        + hex_strings.index(hex_value[6]) * 16) / 256
        return((r1, g1, b1, a))
    except:
        return("g")
    


def digits(integer, digit_count):
    while len(integer) < digit_count:
        integer = "0" + integer
    return integer

def hex(integer, total = ""):
    if integer / 16 >= 1:
        new_integer = integer // 16
        remainder = integer % 16
        hex_dig = hex_strings[remainder]
        total = hex_dig + total
        return(hex(new_integer, total))
    else:
        hex_dig = hex_strings[integer]
        return(hex_dig + total)
    

# figureProfile class works with graphical user interfaces that allow plots
# to be added and changed.
class figureProfile:
    # initializer
    def __init__(self, raw_name, data, directory):
        self.raw_name = raw_name
        self.data = data
        self.directory = directory
        self.forget_canvas = False
        self.forget_choices = False
        self.horiz = False
        self.filler = 0
        self.color = 'g'
        
    # function to change out the data set
    def data_edit(self, data):
        self.data = data
    
    # function to change or keep the choice menu
    def choice_menu_set(self, choices, choice_quote, same):
        if choices == 0:
            if self.forget_choices:
                if same:
                    return
                else:
                    self.choice_menu.destroy()
                    return
            else:
                return
        if self.forget_choices:
            if same:
                return
            else:
                self.choice_menu.destroy()
                self.forget_choices = False
                self.choice_menu_set(choices, choice_quote, same)
        else:
            self.forget_choices = True
            choice_str = tk.StringVar(frame)
            choice_str.set(choice_quote)
            choice_menu = tk.OptionMenu(frame, choice_str, *choices)
            choice_menu.grid()
            self.choice_menu = choice_menu
    
    
    # function to add the canvas
    def canvas_set(self):
        if self.forget_canvas:
            pass
        else:
            self.forget_canvas = True
            flip_button = tk.Button(frame, text= "Flip Axis", 
                              command = lambda : self.flip()) 
            flip_button.grid(column = 1) 
            save_button = tk.Button(frame, text= "Save Figure",
                                    command = lambda : self.save())
            save_button.grid(column = 2, row = 1)
            color_frame = tk.Tk()
            color_frame.geometry("400x400")
            color_canvas = tk.Canvas(frame, width = 320, height = 320)
            color_x = np.arange(0, 15)
            color_y = np.arange(0, 15)
            fill_value = 0
            for x_v in color_x:
                for y_v in color_y:
                    hex_x = digits(hex(x_v**2), 2)
                    hex_y = digits(hex(y_v**2), 2)
                    fill_color = "#" + hex_x + hex_y + "00"
                    
                    exec(self.raw_name + ".fill" + str(fill_value) + " = \"" + 
                         str(fill_color) + "\"")
                    exec("color_rect = tk.Button(" +
                        "color_frame" + ", width = 20, " +
                        "height = 20, bg = fill_color, " +
                        "command = lambda:" + self.raw_name + ".color_select(" +
                        self.raw_name + ".fill" + str(fill_value) + "))")
                    exec("color_rect.place(x = 20*x_v, y = 20*y_v)")
                    """
                    color_rect = color_frame.button(20*x_v, 20*y_v, 
                                                  20*x_v + 20, 20*y_v + 20,
                                                  fill = fill_color,
                                                  tags = fill_color)
                    color_rect.tag_bind(color_rect, '<Button-1>', 
                                          lambda color_choice: 
                                              self.color_select(color_choice,
                                                                color_rect,
                                                                fill_color))
                    """
                    """
                    try:
                        exec("self.color_dict.update({" + str(color_rect) +
                             " : " + fill_color + "})")
                    except:
                        execself.color_dict = {color_rect : fill_color}
                    """
                    fill_value += 1
            color_canvas.grid(column = 2, row = 2)
        try:
            figs_saved.current_canvas_widget.destroy()
        except:
            pass
        self.initial_img = Figure(figsize=(5, 4), dpi = 100) 
        self.ax = self.initial_img.add_subplot(111) 
        self.canvas = FigureCanvasTkAgg(self.initial_img, master= frame) 
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row = 1)
        self.current_canvas_widget = self.canvas.get_tk_widget()
    
    
    def color_select(self, fill_color):
        self.color = fill_color
        self.basic_plot(self.plot_type)
    
    # function to change the orientation variable
    def flip(self):
        if self.horiz == False:
            self.horiz = True
        else:
            self.horiz = False
        self.basic_plot(self.plot_type)
    
    def toggle_animation(self):
        if self.animated == False:
            self.animated = True
        else:
            self.animated = False
        
    
    def save(self):
        self.initial_img.savefig(self.directory + str(self.filler))
        self.filler += 1
    
    # function to plot onto the GUI
    def basic_plot(self, plot_type):
        self.canvas_set()
        try:
            if self.plot_type == plot_type:
                same = True
            else:
                self.plot_type = plot_type
                same = False
        except:
            self.plot_type = plot_type
            same = False
        if self.plot_type == "Histogram":
            hist_counts, hist_bins = np.histogram(self.data)
            plt.stairs(hist_counts, hist_bins)
            if self.horiz:
                self.ax.hist(hist_bins[:-1], hist_bins, weights= hist_counts, 
                        orientation = "horizontal", color = self.color) 
            else: 
                self.ax.hist(hist_bins[:-1], hist_bins, weights= hist_counts, 
                        color = self.color)
            self.choice_menu_set(0, "", same)
        elif self.plot_type == "Bar Graph":
            if self.horiz:
                self.ax.barh(asker_object.current_column, 
                             max(asker_object.current_column), color = self.color)
            else:
                self.ax.bar(asker_object.current_column, 
                            max(asker_object.current_column), color = self.color)
            choices = ["Original", "Labeled", "Stacked", "Grouped", "Hat", 
                       "Bar of Pie", "Nested Pie", "Polar Axis"]
            self.choice_menu_set(choices, "Select a type of bar graph", same)
        elif self.plot_type == "Boxplot":
            plt.style.use('_mpl-gallery')
            if self.horiz:
                self.ax.boxplot(self.data, widths=1.5, vert= False)
            else:
                self.ax.boxplot(self.data, widths=1.5)
            self.choice_menu_set(0, "", same)
        elif self.plot_type == "Distribution":
            if self.horiz:
                pass
            else:
                self.ax.plot(self.data, color = self.color)
        elif self.plot_type == "Pie":
            self.ax.pie(self.data, colors = [hex_to_rgba(self.color)])
            
            
        



# Inputter object
asker_object = inputter.adv_inputters()
# Storing working directory to replace
prev_wd = os.getcwd()
# Asking for folder directory
asker_object.basic_read("Please choose the folder directory:", "dir")

# Making new directory to add to
os.makedirs(os.getcwd() + '\\visuals', exist_ok = True)

# Directory list to take a file
print("Here are your options: ")
print(os.listdir())
asker_object.basic_read(str_statement = "Please enter the name" + 
                        " of the file to use", readtype = "file", 
                        init_input = os.getcwd() + '\\')




# Column select
print("Here are the column choices: " + 
      str([x.name for x in asker_object.data]))
asker_object.basic_read(str_statement = "Please select the column you" +
                        " seek to visualize data from.", readtype = "column")


# Plot types
plot_types = ["Histogram", "Bar Graph", "Boxplot", "Distribution", "Pie"]
# While-loop base case
not_finished = True
# figureProfile Object
figs_saved = figureProfile("figs_saved", asker_object.current_column, asker_object.directory)


# A while-loop that is supposed to
# start a plot
while not_finished:
    frame = tk.Tk()
    frame.geometry("900x400")
    plot_choice = tk.StringVar(frame)
    plot_choice.set("Plot Type")
    plot_menu = tk.OptionMenu(frame, plot_choice, *plot_types,
                              command= lambda x : figs_saved.basic_plot(x))
    plot_menu.grid()
    frame.title("Data Visualization Interface")
    frame.mainloop()
    not_finished = asker_object.basic_ask(
        "Are you finished selecting visuals?")



# Reclaiming previous directory
os.chdir(prev_wd)



# Made with the help of various API reference pages such as those of
# Matplotlib, Pandas, Numpy, and Tkinter

