import tkinter as tk
import pyttsx3

engine= pyttsx3.init()
class Widget():

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Read a file')
        # self.root.resizable(0,0)
        self.labe1 = tk.Label(self.root, text="Select a file to read")
        self.labe1.pack()
        self.entry=tk.Entry(self.root)
        self.entry.pack
        self.button = tk.Button(self.root, text='open a file', command = self.clicked)
        self.button.pack()

    def showWidget(self):
        self.root.mainloop()


    def clicked(self):
        

        with open('/home/shweta/Documents/python/rdfile.txt') as f:
            # lines = f.readlines.()
            lines = f.read().splitlines()
    

        engine.say(lines)
        engine.runAndWait()
        engine.runAndWait()



if __name__ == '__main__':
    widget = Widget()
    widget.showWidget()