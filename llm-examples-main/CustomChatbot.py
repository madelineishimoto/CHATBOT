import tkinter as tk

root=tk.Tk()

def create_window():
    
    width, height = 500, 400
    root.geometry('%dx%d+0+0' % (width, height))
    
def maximise_window():
  
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry('%dx%d+0+0' % (screen_width, screen_height))
    

def center_window():

    width, height = 500, 400
    screen_width = root.winfo_screenwidth()
    screen_height= root.winfo_screenheight()
    x_cord = int((screen_width/2) - (width/2))
    y_cord = int((screen_height/2) - (height/2))
    root.geometry("{}x{}+{}+{}" .format(width, height, x_cord, y_cord))
    

class Theme:
    def __init__(self, primary_color, background_color, secondary_background_color, text_color, font):
        self.primary_color = primary_color
        self.background_color = background_color
        self.secondary_background_color = secondary_background_color
        self.text_color = text_color
        self.font = font


theme = Theme(primary_color="#F63360",
              background_color="#FFFF33",
              secondary_background_color="#FFFDD0",
              text_color="#111227",
              font="Inter")

