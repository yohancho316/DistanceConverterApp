################################# Python Imported Libraries ######################################
import tkinter as tk
from tkinter import ttk

################################# TKinter Executible Code ######################################
class DistanceConverter(tk.Tk):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    self.title("John's Distance Converter")
    self.geometry('190x110')
    self.resizable(True,True)
    self.frames = dict()

    container = ttk.Frame(self)
    container.grid(padx=60,pady=30,sticky='EW')

    metres_to_feet = MetresToFeet(container,self)
    metres_to_feet.grid(row=0,column=0,sticky='NSEW')

    feet_to_metres = FeetToMetres(container,self)
    feet_to_metres.grid(row=0,column=0,sticky='NSEW')

    # The Class itself Becomes Keys and its Objects are the Associated Values
    self.frames[FeetToMetres] = feet_to_metres
    self.frames[MetresToFeet] = metres_to_feet

    # Decide Which Frame to Display First
    self.show_frames(FeetToMetres)

    # self.bind("<Return>",frame.calculate)
    # self.bind('<KP_Enter>',frame.calculate)

  def show_frame(self,container):
    frame = self.frames[container]
    frame.tkraise()

# Meters to Feet Class
class MetresToFeet(ttk.Frame):
  def __init__(self, container,controller,**kwargs):
    super().__init__(container,**kwargs)
    self.feet_value = tk.StringVar()
    self.metres_value = tk.StringVar()

    # Label Widgets
    metres_label = ttk.Label(self,text='Metres:')
    metres_label.grid(column=1,row=1,sticky='W',ipadx=5)
    feet_label = ttk.Label(self,text='Feet:')
    feet_label.grid(column=1,row=2,sticky='W',ipadx=5)
    feet_display = ttk.Label(self,textvariable=self.feet_value)
    feet_display.grid(column=2,row=2,sticky='EW')

    # Entry Widget
    metres_input = ttk.Entry(self,width=10,textvariable=self.metres_value)
    metres_input.grid(column=2,row=1,sticky='EW')
    metres_input.focus()

    # Button Widgets
    calculate_button = ttk.Button(self,text='Calculate:',command=self.calculate)
    calculate_button.grid(column=1,row=3,columnspan=2,sticky='EW')
    switch_page_button = ttk.Button(self,text='Switch to Metres Calc',command=lambda: controller.show_frame(FeetToMetres))

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
    feet_label.grid(column=1,row=1,sticky='W',ipadx=5)
    metres_label = ttk.Label(self,text='Metres:')
    metres_label.grid(column=1,row=2,sticky='W',ipadx=5)
    metres_display = ttk.Label(self,textvariable=self.metres_value)
    metres_display.grid(column=2,row=2,sticky='EW')

    # Entry Widgets
    feet_input = ttk.Entry(self,width=10,textvariable=self.feet_value)
    feet_input.grid(column=2,row=1,sticky='EW')
    feet_input.focus()

    # Button Widgets
    calculate_button = ttk.Button(self,text='Calculate:',command=self.calculate)
    calculate_button.grid(column=1,row=3,columnspan=2,sticky='EW')
    switch_page_button = ttk.Button(self,text='Switch to Feet Calc',command=lambda: controller.show_frame(MetresToFeet))

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