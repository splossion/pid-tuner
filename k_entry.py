import customtkinter as ctk

class entryBox:
    def __init__(self, root, name="K", row=0, column=0) -> None:
        self.root = root
        self.row = row
        self.column = column
        self.name = name
        self.is_enable = True
        self.__create_label()
        self.__create_entry_box()
    
    def __create_label(self):
        self.__label = ctk.CTkLabel(self.root, text=self.name, fg_color="transparent")
        self.__label.grid(row=self.row, column=self.column, padx=20, pady=10)
        
    def __create_entry_box(self):
        self.__entry = ctk.CTkEntry(self.root, placeholder_text=self.name)
        self.__entry.grid(row=self.row+1, column=self.column, padx=20, pady=20)
        
        