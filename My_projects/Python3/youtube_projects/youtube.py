import tkinter as tk

class Application(object):
    """ Főosztály létrehozása. """
    def __init__(self, master = None):
        self.master = master
        self.frame = tk.Frame(self.master, width = 600, height = 400, bg = "white")
        self.frame.pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Youtube Downloader")
    root.geometry("1366x768")
    app = Application(master=root)
    root.mainloop()