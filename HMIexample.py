import tkinter as tk
from tkinter import BOTTOM, RIGHT, LEFT, ttk
from tkinter.messagebox import showinfo
import math
from tkinter import Tk, Text
from turtle import right
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv
import random
import time
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import style
import matplotlib.animation as animation

#############################################################
root = tk.Tk()
root.geometry("400x300")
root.resizable(False, False)
root.title('"HMI"Example')

##############################################################
def EMERGENCY_SHUTOFF():
    print("TRIP")

 
def send_log():
    print("LOG SEND")

def turn_on():
    print("POWER ON")

TRIP = ttk.Button( text="TRIP", command=EMERGENCY_SHUTOFF)
TRIP.place(x=25, y=250)


send_log = ttk.Button( text="Send Log to Server", command=send_log)
send_log.place(x=150, y=250)

turn_on = ttk.Button( text="POWER ON?", command=turn_on)
turn_on.place(x=300, y=250)

#plot = ttk.Button( text="Plot", command=animate)
#plot.place(x=165, y=225)

root.mainloop()
#############################################