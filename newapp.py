import tkinter as tk
from tkinter import ttk


class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('400x400')
        self.root.title('App')
        self.mainframe = tk.Frame(self.root, background='White')
        self.mainframe.pack(fill='both', expand=True,)


        #
        self.text = ttk.Label(self.mainframe, text='Hello World', background='White', font=('Brass Mono', 30))
        self.text.grid(row=0, column=0)

        #Text_Box
        self.text_field = ttk.Entry(self.mainframe,)
        self.text_field.grid(row=1, column=0, pady=10, sticky='NWES')

        set_text_button = ttk.Button(self.mainframe, text='Set Text',command=self.set_text)
        set_text_button.grid(row=1, column=1, pady=10)


        color_options = ['Red','Black','Green','Blue']
        self.color_box = ttk.Combobox(self.mainframe, values=color_options)
        self.color_box.grid(row=2, column=0,sticky='NWES',pady=10)

        set_color_button = ttk.Button(self.mainframe, text='Color Selection',command=self.set_color)
        set_color_button.grid(row=2, column=1, pady=10)


        self.reverse_text = ttk.Button(self.mainframe, text='Reverse Text', command=self.reverse)
        self.reverse_text.grid(row=3, column=0, sticky='NWES', pady=10)
        self.root.mainloop()
        return
    
    def set_text(self):
        newtext = self.text_field.get()
        self.text.config(text=newtext)


    def set_color(self):
        newcolor = self.color_box.get()
        self.text.config(foreground=newcolor)

    def reverse(self):
        newtext = self.text.cget('text')
        reversed = newtext[::-1]
        self.text.config(text=reversed)

if __name__ == '__main__':
    App()
