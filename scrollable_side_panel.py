
from tkinter import *


class ScrollableSidePanel(Frame):

    def __init__(self, option_panel, **kw):
        self.option_panel = option_panel
        self.canvas = Canvas(self.option_panel, borderwidth=0.5, width=250)
        super().__init__(master=self.canvas, width=225, **kw)

        self.scrollbar = Scrollbar(self.option_panel, orient=VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=RIGHT, fill=BOTH)
        self.canvas.pack(side=RIGHT, fill=Y, expand=True)
        self.canvas.create_window((1, 2), window=self, anchor="ne", tags="self.frame")
        self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(int(-(event.delta / 120)), "units"))

        self.bind("<Configure>", lambda *args: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
