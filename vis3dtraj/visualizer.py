#!/bin/env python

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

from vis3dtraj import app_style
from vis3dtraj.plot_manager import Plotter
from vis3dtraj.gui.main_window import MainWindow


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

        pyplot.subplots_adjust(**app_style.plot.subplot_kwargs)

        self.plot_mngr = None

        # Sets up the ui
        self.ui_handler = MainWindow(self)
        self.plot_mngr = Plotter(self)

        self.ui_handler.update_projectile_inputs(self.plot_mngr.parabola, True)
        self.ui_handler.update_plane_inputs(self.plot_mngr.plane)
        self.ui_handler.update_spiral_inputs(self.plot_mngr.spiral)
        self.ui_handler.grav_acceleration_change(None, 9.81)

        tkinter.mainloop()


def run():
    return Visualizer()


if __name__ == '__main__':
    vis = run()
