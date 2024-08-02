import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
import random

class realTimePlotApp:
    def __init__(self, root):
        self.root = root
        
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title("Real-Time Data")
        
        self.x_data = []
        self.y_data = []
        self.line, = self.ax.plot(self.x_data, self.y_data, 'r-')  # Line object

        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.ani = animation.FuncAnimation(self.fig, self.update_plot, interval=1000)

    def update_plot(self, i):
        if len(self.x_data) > 100:
            self.x_data.pop(0)
            self.y_data.pop(0)
        self.x_data.append(i)
        self.y_data.append(random.randint(0, 10))

        # Update the data of the line object
        self.line.set_xdata(self.x_data)
        self.line.set_ydata(self.y_data)

        # Rescale the axes
        self.ax.relim()
        self.ax.autoscale_view()

        # Redraw the canvas
        self.canvas.draw()