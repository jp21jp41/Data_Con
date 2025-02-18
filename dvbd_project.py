# Data Visualization Backend Designer (DVBD)
# Justin Pizano

# Import Libraries
import pandas as pnd
import os
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.figure import Figure


# NOTE: inputter is a python module that I have personally designed.
# The module can be found on GitHub (automatic import later)
import inputter

# figureProfile class works with graphical user interfaces that allow plots
# to be added and changed.
class figureProfile:
    # initializer
    def __init__(self, data):
        self.data = data
        self.forget_canvas = False
        self.forget_choices = False
        self.horiz = False
        
    # function to change out the data set
    def data_edit(self, data):
        self.data = data
    
    # function to change or keep the choice menu
    def choice_menu_set(self, choices, choice_quote, same):
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
            choice_menu.pack()
            self.choice_menu = choice_menu
    
    # function to add the canvas
    def canvas_set(self, plot_type):
        if self.forget_canvas == True:
            pass
        else:
            flip_menu = tk.Button(frame, text= "Flip Axis", 
                              command = lambda : self.flip()) 
            flip_menu.pack() 
            self.forget_canvas = True
        try:
            figs_saved.current_canvas_widget.destroy()
        except:
            pass
        self.initial_img = Figure(figsize=(5, 4), dpi = 100) 
        self.ax = self.initial_img.add_subplot(111) 
        self.canvas = FigureCanvasTkAgg(self.initial_img, master= frame) 
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side= tk.TOP, fill= tk.BOTH, expand= 1)
        self.current_canvas_widget = self.canvas.get_tk_widget()
    
    
    # function to flip the orientation of the image
    def flip(self):
        if self.horiz == False:
            self.horiz = True
        else:
            self.horiz = False
        self.basic_plot(self.plot_type)
            
    
    # function to plot onto the GUI
    def basic_plot(self, plot_type):
        self.canvas_set(plot_type)
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
                        orientation = "horizontal", color = 'g') 
            else: 
                self.ax.hist(hist_bins[:-1], hist_bins, weights= hist_counts, 
                        color = 'g')
            choices = ["Original", "Cumulative Distribution", "Animated", "SVG"]
            self.choice_menu_set(choices, "Select a type of histogram", same)
        elif self.plot_type == "Bar Graph":
            if self.horiz:
                self.ax.barh(asker_object.current_column, max(asker_object.current_column))
            else:
                self.ax.bar(asker_object.current_column, max(asker_object.current_column))
            choices = ["Original", "Labeled", "Stacked", "Grouped", "Hat", 
                       "Bar of Pie", "Nested Pie", "Polar Axis"]
            self.choice_menu_try(choices, "Select a type of bar graph", same)


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
      str([x for x in asker_object.data.columns]))
asker_object.basic_read(str_statement = "Please select the column you" +
                        " seek to visualize data from.", readtype = "column")


# Plot types
plot_types = ["Histogram", "Bar Graph"]
# While-loop base case
not_finished = True
# figureProfile Object
figs_saved = figureProfile(asker_object.current_column)



while not_finished:
    frame = tk.Tk()
    frame.geometry("900x400")
    plot_choice = tk.StringVar(frame)
    plot_choice.set("Plot Type")
    plot_menu = tk.OptionMenu(frame, plot_choice, *plot_types,
                              command= lambda x : figs_saved.basic_plot(x))
    plot_menu.pack()
    frame.title("Data Visualization Interface")
    frame.mainloop()
    not_finished = asker_object.basic_ask(
        "Are you finished selecting visuals?")



# Reclaiming previous directory
os.chdir(prev_wd)



# Made with the help of various API reference pages such as those of
# Matplotlib, Pandas, Numpy, and Tkinter

