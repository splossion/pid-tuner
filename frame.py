import customtkinter as ctk

class myFrame(ctk.CTkFrame):
    def __init__(self, root, row=0, column=0, **kwargs):
        super().__init__(master=root, **kwargs)
        self.configure(width = 200, height = 200)
        self.__root = root
        self.__row = row
        self.__column = column
        self.grid(row=self.__row, column=self.__column)
    
    def deactivate(self):
        self.grid_forget()
    
    def activate(self):
        self.grid(row=self.__row, column=self.__column)
