from tkinter import *

class Topics:
    def __init__(self):
        global root
        self.v = []
        self.root = Tk()
        self.root.title('Topic')
        self.root.geometry('450x450')

        self.labelTopic = Label(self.root, text="Nume topic ", font=("calibri", 20))
        self.labelTopic.grid(row=0, column=0)

        #creare caseta text
        self.entryTopic = Entry(self.root, width="30")
        self.entryTopic.grid(row=2, column=0)

        #buton adaugare topic
        self.buttonAdd = Button(self.root, text=" ADD", bg="black", fg="white", command=self.add)
        self.buttonAdd.grid(row=2, column=2)

        #buton delete
        button = Button(self.root, text=" DELETE", bg="black",fg="white", command=self.delete_topic)
        button.grid(row=2, column=3)

        #buton subscribe
        button = Button(self.root, text=" SUBCRIBE", bg="black",fg="white", command=self.subscribe_topic)
        button.grid(row=2, column=4)

        #bunton unsubscribe
        button = Button(self.root, text=" UNSUBSCRIBE", bg="black",fg="white", command=self.unsubscribe_topic)
        button.grid(row=2, column=5)

        self.root.mainloop()

    #adaugare topic
    def add(self):
        self.v.append(self.entryTopic.get())
        self.textbox= Listbox(self.root, height=10, width=30)
        self.textbox.grid(row=5, column=0)

        for i in self.v:
            self.textbox.insert(END, i+'\n')

    #stergere topic
    def delete_topic(self):
        sel = self.textbox.curselection()
        for index in sel[::-1]:
            self.textbox.delete(index)

    #subscribe la topic
    def subscribe_topic(self):
        sel = self.textbox.curselection()

    #unsubscribe la topic
    def unsubscribe_topic(self):
        sel = self.textbox.curselection()
