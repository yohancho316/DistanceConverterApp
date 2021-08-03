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
    for FrameClass in (MetersToFeet,FeetToMeters):
      frame = FrameClass(container,self)
      self.frames[FrameClass] = frame
      frame.grid(row=0,column=0,sticky="NSEW")

    self.show_frame(MetersToFeet)

# Decide Which Frame to Display First
  def show_frame(self,container):
    frame = self.frames[container]
    self.bind("<Return>",frame.calculate)
    self.bind("<KP_Enter>",frame.calculate)
    frame.tkraise()

# Meters to Feet Class
class MetersToFeet(ttk.Frame):
  def __init__(self, container,controller,**kwargs):
    super().__init__(container,**kwargs)
    self.feet_value = tk.StringVar()
    self.meters_value = tk.StringVar()

    # Label Widgets
    meters_label = ttk.Label(self,text='Meters:')
    meters_label.grid(row=1,column=1,sticky='W',ipadx=5)
    feet_label = ttk.Label(self,text='Feet:')
    feet_label.grid(row=2,column=1,sticky='W',ipadx=5)
    feet_display = ttk.Label(self,textvariable=self.feet_value)
    feet_display.grid(row=2,column=2,sticky='WE')

    # Entry Widget
    meters_input = ttk.Entry(self,width=10,textvariable=self.meters_value)
    meters_input.grid(row=1,column=2,sticky='WE')
    meters_input.focus()

    # Button Widgets
    calculate_button = ttk.Button(self,text='Calculate:',command=self.calculate)
    calculate_button.grid(row=3,column=0,columnspan=2,sticky='WE')
    switch_page_button = ttk.Button(self,text='Switch Feet to Meters Calc',command=lambda: controller.show_frame(FeetToMeters))
    switch_page_button.grid(row=4,column=0,columnspan=2,sticky='WE')

    for child in self.winfo_children():
        child.grid_configure(padx=5,pady=5)

  def calculate(self,*args):
    try:
      value = float(self.meters_value.get())
      self.feet_value.set('%.2f' % (value * 3.28084))
    except ValueError:
      pass

# Feet to Meters Class
class FeetToMeters(ttk.Frame):
  def __init__(self,container,controller,**kwargs):
    super().__init__(container,**kwargs)
    self.feet_value = tk.StringVar()
    self.meters_value = tk.StringVar()

    # Label Widgets
    feet_label = ttk.Label(self,text='Feet:')
    feet_label.grid(row=1,column=1,sticky='W',ipadx=5)
    meters_label = ttk.Label(self,text='Meters:')
    meters_label.grid(row=2,column=1,sticky='W',ipadx=5)
    meters_display = ttk.Label(self,textvariable=self.meters_value)
    meters_display.grid(row=2,column=2,sticky='WE')

    # Entry Widgets
    feet_input = ttk.Entry(self,width=10,textvariable=self.feet_value)
    feet_input.grid(row=1,column=2,sticky='WE')
    feet_input.focus()

    # Button Widgets
    calculate_button = ttk.Button(self,text='Calculate:',command=self.calculate)
    calculate_button.grid(row=3,column=0,columnspan=2,sticky='WE')
    switch_page_button = ttk.Button(self,text='Switch Meters to Feet Calc',command=lambda: controller.show_frame(MetersToFeet))
    switch_page_button.grid(row=4,column=0,columnspan=2,sticky='WE')

    for child in self.winfo_children():
        child.grid_configure(padx=5,pady=5)

  def calculate(self,*args):
    try:
      value = float(self.feet_value.get())
      self.meters_value.set('%.2f' % (value * 3.28084))
    except ValueError:
      pass

################################# Python Executible Code ######################################
root = DistanceConverter()
root.mainloop()