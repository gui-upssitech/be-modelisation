from tkinter import *

class SettingsWidget:

    def __init__(self):
        self.counter = 0
        self.btn_desc = StringVar()
        self.btn_desc.set("Counter: 0")

    def draw(self, parent):
        root = Frame(parent)

        btn = Button(root, textvariable=self.btn_desc, command=self.__on_click)
        btn.pack(padx=10, pady=10)

        root.pack(fill=BOTH, expand=True)
        parent.add(root, text="Paramètres")

    def __on_click(self):
        self.counter += 1
        self.btn_desc.set(f"Counter: {self.counter}")