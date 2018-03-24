try:
    import matplotlib
    matplotlib.use('TkAgg')
    from matplotlib.figure import Figure
    from matplotlib import pyplot as plt
    from mpl_toolkits.mplot3d import axes3d
except ImportError:
    raise ImportError("Visualizer requires module Matplotlib")

try:
    from tkinter import *
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
except ImportError:
    raise ImportError("Visualizer requires module tkinter")

import app_style as style
from detail_frames import *
from parabola import *
from plotter import *
from scrollable_side_panel import *
import numpy as np
import itertools


class DetailsWindow(Toplevel):

    def __init__(self, vis, **kw):
        super().__init__(**kw)
        self.vis = vis
        self.protocol('WM_DELETE_WINDOW', self.hide)
        self.title("Details Window")
        self.shown = False

        self._row_counter = (x for x in itertools.count(start=0, step=1))

        self.figure = plt.figure()

        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=0.95)
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self)
        self.canvas.show()
        self.toolbar.update()

        self.figure.subplots_adjust(left=style.plot.left,
                                    right=style.plot.right,
                                    top=style.plot.top,
                                    bottom=style.plot.bottom,
                                    wspace=style.plot.wspace)

        self.side_frame = Frame(self, width=style.panel.width)
        self.side_frame.pack(side=RIGHT, fill=BOTH)

        self.side_panel = ScrollableSidePanel(self.side_frame)

        # CREATE AXIS
        self.axis = self.figure.add_subplot(111)
        self.axis.format_coord = self.display_coords
        handles, labels = self.axis.get_legend_handles_labels()
        self.axis.legend(handles, labels, fontsize=style.plot.label_font_size)

        # GUI
        self.coord = StringVar(value="[x , y]")
        self.coord_label = Label(self.side_panel, font=style.panel.large_text, textvariable=self.coord)
        self.coord_label.grid(row=self._next_row(), column=0, columnspan=2, sticky=N)
        self.top_spacer = Label(self.side_panel, text="\t\t\t", width=5)
        self.top_spacer.grid(row=self._next_row(), column=0)

        # LOCK AXIS
        self.lock_axis = IntVar()
        self.lock_axis_input = Checkbutton(self.side_panel, text="Lock Axis", variable=self.lock_axis,
                                           command=lambda *args: self.redraw())
        self.lock_axis_input.grid(row=self._next_row(), column=0)

        # OBJECTS
        object_values = ['Parabolic Trajectory', 'Spiral Trajectory']
        self.object_selection_value = StringVar()
        self.object_selection_value.set(object_values[0])
        self.object_selection_value.trace('w', lambda *args: self.change_selected_object(self.object_selection_value.get()))
        self.object_selection_label = Label(self.side_panel, text="Selected Object: ")
        self.object_selection_input = OptionMenu(self.side_panel, self.object_selection_value,
                                                 'Parabolic Trajectory', 'Spiral Trajectory',
                                                 command=lambda *args: self.change_selected_object(self.object_selection_value.get()))
        obj_selection_row = self._next_row()
        self.object_selection_label.grid(row=obj_selection_row, column=0, sticky=E)
        self.object_selection_input.grid(row=obj_selection_row, column=1, sticky=W)

        self.parabola_frame = ParabolaDetailsFrame(self, self.axis, self.vis.plotter.parabola, master=self.side_panel)
        self.spiral_frame = SpiralDetailsFrame(self, self.axis, self.vis.plotter.spiral, master=self.side_panel)

        self.parabola_frame.grid(row=self._next_row(), column=0, sticky=E)
        self.spiral_frame.grid(row=self._next_row(), column=0, sticky=E)

        self.change_selected_object('Parabolic Trajectory')

    def change_selected_object(self, new_obj):
        self.axis.clear()
        if new_obj == 'Parabolic Trajectory':
            self.parabola_frame.grid()
            self.parabola_frame.on_focus()
            self.spiral_frame.grid_remove()
        elif new_obj == 'Spiral Trajectory':
            self.parabola_frame.grid_remove()
            self.spiral_frame.grid()
            self.spiral_frame.on_focus()

        self.axis.grid()
        self.canvas.draw()

    def redraw(self):
        if self.object_selection_value.get() == 'Parabolic Trajectory':
            self.parabola_frame.redraw()
        elif self.object_selection_value.get() == 'Spiral Trajectory':
            self.spiral_frame.redraw()
        elif self.object_selection_value.get() == 'Plane':
            pass
            #self.plane_frame.redraw()

    def _next_row(self):
        return next(self._row_counter)

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
            self.hide()
        else:
            self.show()

    def hide(self):
        self.shown = False
        self.iconify()

    def show(self):
        self.shown = True
        self.deiconify()
