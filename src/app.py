from tkinter import Tk

from src.controllers.person import PersonController

if __name__ == '__main__':
    # Start Application
    mainwin = Tk()
    width = 650
    height = 450
    mainwin.geometry(f'{width}x{height}')
    mainwin.title('Contact Book')

    app = PersonController(mainwin)
    mainwin.mainloop()
