#!/bin/env python
import math

try:
    import matplotlib
    matplotlib.use('TkAgg')
    from matplotlib import pyplot
    from matplotlib import style
except ImportError:
    raise ImportError("Visualizer requires module Matplotlib")

try:
    import tkinter
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
except ImportError:
    raise ImportError("Visualizer requires module tkinter")

import app_style
from parabola import Parabola
from plotter import Plotter
from main_window import MainWindow


class Visualizer:

    def __init__(self):
        pyplot.style.use(app_style.plot.style)
        self.tk_root = tkinter.Tk()

        self.tk_root.wm_title("Trajectory Visualization")

        self.figure = pyplot.figure()

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.tk_root)
        self.canvas.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=0.95)

        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.tk_root)

        self.canvas.show()
        self.toolbar.update()

        pyplot.subplots_adjust(left=0.045, right=1-0.045, top=0.95, bottom=0.06, wspace=0.15)

        self.plotter = None

        # Sets up the ui
        self.ui_handler = MainWindow(self)

        self.plotter = Plotter(self)

        self.ui_handler.update_projectile_inputs(self.plotter.parabola, True)
        self.ui_handler.update_plane_inputs(self.plotter.plane)
        self.ui_handler.update_spiral_inputs(self.plotter.spiral)
        self.ui_handler.grav_acceleration_change(None, 9.81)

        #pyplot.xlim([-10, 10])
        #pyplot.ylim([-10, 10])

        tkinter.mainloop()


if __name__ == '__main__':
    vis = Visualizer()
