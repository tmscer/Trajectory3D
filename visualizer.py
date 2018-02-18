#!/bin/env python
import math

try:
    import matplotlib
    matplotlib.use('TkAgg')
    from matplotlib.figure import Figure
    from matplotlib import pyplot
    from matplotlib import style
    from mpl_toolkits.mplot3d import axes3d
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
except ImportError:
    raise ImportError("Visualizer requires module Matplotlib")

try:
    import tkinter
except ImportError:
    raise ImportError("Visualizer requires module tkinter")

from projectile import *
from plotter import *
from user_interface_handler import *


class Visualizer:

    def __init__(self):
        self.tk_root = tkinter.Tk()

        self.tk_root.wm_title("Trajectory Vis")

        self.figure = pyplot.figure()

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.tk_root)
        self.canvas.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=0.95)

        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.tk_root)

        del self.toolbar.children['!frame']
        self.toolbar.children.clear()
        print(self.toolbar.children.keys())

        self.canvas.show()
        self.toolbar.update()

        pyplot.subplots_adjust(left=0.045, right=0.975, top=0.95, bottom=0.06, wspace=0.15)

        self.plotter = None

        # Sets up the ui
        self.ui_handler = UserInterfaceHandler(self)

        self.plotter = Plotter(self)

        self.ui_handler.update_inputs(self.plotter.proj, 0, False)

        tkinter.mainloop()


if __name__ == '__main__':
    vis = Visualizer()
