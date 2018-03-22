try:
    import matplotlib
    matplotlib.use('TkAgg')
    from matplotlib.figure import Figure
    from matplotlib import pyplot as plt
    from matplotlib import style
    from mpl_toolkits.mplot3d import axes3d
except ImportError:
    raise ImportError("Visualizer requires module Matplotlib")

try:
    from tkinter import *
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
except ImportError:
    raise ImportError("Visualizer requires module tkinter")

from projectile import *
from plotter import *
from scrollable_side_panel import *
import numpy as np
import itertools


class DetailsWindow(Toplevel):

    def __init__(self, root, **kw):
        super().__init__(**kw)
        self.protocol('WM_DELETE_WINDOW', self.iconify)
        self.title("Details Window")
        self.shown = False

        self.figure = plt.figure()

        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=0.95)
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self)
        self.canvas.show()
        self.toolbar.update()

        self.figure.subplots_adjust(left=0.045, right=1-0.045, top=0.95, bottom=0.06, wspace=0.15)

        self.side_panel = ScrollableSidePanel(self)

        self._row_counter = (x for x in itertools.count(start=0, step=1))
        
        self._test_plot()

        # GUI
        self.coord = StringVar(value="[x , y]")
        self.coord_label = Label(self.side_panel, font=("Helvetica", 15), textvariable=self.coord)
        self.coord_label.grid(row=self._next_row(), column=0, columnspan=2)
        self.top_spacer = Label(self.side_panel, text="\t\t\t", width=5)
        self.top_spacer.grid(row=self._next_row(), column=0)
        #self.object_selection_label = Label(self.side_panel)
        #self.object_selection_input = OptionMenu(self.side_panel)

    def _next_row(self):
        return next(self._row_counter)

    # DELETE AT SOME POINT
    def _test_plot(self):
        ax = self.figure.add_subplot(111)
        ax.format_coord = self.display_coords

        xs = np.arange(0, 10, 0.1)
        ys = np.sin(xs)

        ax.plot(xs, ys, label='ẋ')

        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles, labels, fontsize=15)

    def display_coords(self, x, y):
        if x < 0:
            pol_x = '-'
        else:
            pol_x = '+'
        if y < 0:
            pol_y = '-'
        else:
            pol_y = '+'
        self.coord.set("[{}{:2.3f} , {}{:2.3f}]".format(pol_x, abs(x), pol_y, abs(y)))
        return ''

    def toggle(self):
        if self.shown:
            self.iconify()
        else:
            self.deiconify()
        self.shown = not self.shown
