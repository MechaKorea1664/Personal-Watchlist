from tkinter import *
from tkinter.font import BOLD


def home(t_mst,t_font):
    frame = Frame(t_mst,relief=GROOVE,height=100,width=100)
    Label(frame,text='Welcome Home!',font=t_font,justify=LEFT)
    return frame

def sidebar(t_col,t_row,t_mst):
    pass