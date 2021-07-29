################################# Python Imported Libraries ######################################
import tkinter as tk
from tkinter import ttk

################################# TKinter Executible Code ######################################
class DistanceConverter(tk.Tk):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    self.title("John's Distance Converter")
    self.geometry('314x160')
    self.resizable(True,True)
    self.frames = dict()

    container = ttk.Frame(self)
    container.grid(sticky='EW')

    # Apply Styling to the container Frame Widget
    style = ttk.Style(container)
    style.theme_use('classic')

    # Create Dictionary of Frame KVP
    for FrameClass in (MetresToFeet,FeetToMetres):
      frame = FrameClass(container,self)
      self.frames[FrameClass] = frame
      frame.grid(row=0,column=0,sticky="NSEW")

    self.show_frame(MetresToFeet)

# Decide Which Frame to Display First
  def show_frame(self,container):
    frame = self.frames[container]
    self.bind("<Return>",frame.calculate)
    self.bind("<KP_Enter>",frame.calculate)
    frame.tkraise()

# Meters to Feet Class
class MetresToFeet(ttk.Frame):
  def __init__(self, container,controller,**kwargs):
    super().__init__(container,**kwargs)
    self.feet_value = tk.StringVar()
    self.metres_value = tk.StringVar()

    # Label Widgets
    metres_label = ttk.Label(self,text='Metres:')
    metres_label.grid(row=1,column=1,sticky='W',ipadx=5)
    feet_label = ttk.Label(self,text='Feet:')
    feet_label.grid(row=2,column=1,sticky='W',ipadx=5)
    feet_display = ttk.Label(self,textvariable=self.feet_value)
    feet_display.grid(row=2,column=2,sticky='WE')

    # Entry Widget
    metres_input = ttk.Entry(self,width=10,textvariable=self.metres_value)
    metres_input.grid(row=1,column=2,sticky='WE')
    metres_input.focus()

    # Button Widgets
    calculate_button = ttk.Button(self,text='Calculate:',command=self.calculate)
    calculate_button.grid(row=3,column=0,columnspan=2,sticky='WE')
    switch_page_button = ttk.Button(self,text='Switch Feet to Metres Calc',command=lambda: controller.show_frame(FeetToMetres))
    switch_page_button.grid(row=4,column=0,columnspan=2,sticky='WE')

    for child in self.winfo_children():
        child.grid_configure(padx=5,pady=5)

  def calculate(self,*args):
    try:
      value = float(self.metres_value.get())
      self.feet_value.set('%.2f' % (value * 3.28084))
    except ValueError:
      pass

# Feet to Metres Class
class FeetToMetres(ttk.Frame):
  def __init__(self,container,controller,**kwargs):
    super().__init__(container,**kwargs)
    self.feet_value = tk.StringVar()
    self.metres_value = tk.StringVar()

    # Label Widgets
    feet_label = ttk.Label(self,text='Feet:')
    feet_label.grid(row=1,column=1,sticky='W',ipadx=5)
    metres_label = ttk.Label(self,text='Metres:')
    metres_label.grid(row=2,column=1,sticky='W',ipadx=5)
    metres_display = ttk.Label(self,textvariable=self.metres_value)
    metres_display.grid(row=2,column=2,sticky='WE')

    # Entry Widgets
    feet_input = ttk.Entry(self,width=10,textvariable=self.feet_value)
    feet_input.grid(row=1,column=2,sticky='WE')
    feet_input.focus()

    # Button Widgets
    calculate_button = ttk.Button(self,text='Calculate:',command=self.calculate)
    calculate_button.grid(row=3,column=0,columnspan=2,sticky='WE')
    switch_page_button = ttk.Button(self,text='Switch Metres to Feet Calc',command=lambda: controller.show_frame(MetresToFeet))
    switch_page_button.grid(row=4,column=0,columnspan=2,sticky='WE')

    for child in self.winfo_children():
        child.grid_configure(padx=5,pady=5)

  def calculate(self,*args):
    try:
      value = float(self.feet_value.get())
      self.metres_value.set('%.2f' % (value * 3.28084))
    except ValueError:
      pass

################################# Python Executible Code ######################################
root = DistanceConverter()
root.mainloop()