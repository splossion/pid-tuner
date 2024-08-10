import customtkinter as ctk

class myFrame(ctk.CTkFrame):
    def __init__(self, root, row=0, column=0, rowspan=1, columnspan=1, **kwargs):
        super().__init__(master=root, **kwargs)
        self.configure(width = 200, height = 200)
        self.__root = root
        self.__row = row
        self.__column = column
        self.__rowspan = rowspan
        self.__columnspan = columnspan
        self.grid(row=self.__row, column=self.__column, padx=20, pady=10, rowspan = self.__rowspan, columnspan = self.__columnspan)
    
    def deactivate(self):
        self.grid_forget()
    
    def activate(self):
        self.grid(row=self.__row, column=self.__column, rowspan = self.__rowspan, columnspan = self.__columnspan)
