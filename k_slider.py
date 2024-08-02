import customtkinter as ctk

class kSlider:
    def __init__(self, root, name="K", row=0, column=0) -> None:
        self.root = root
        self.row = row
        self.column = column
        self.name = name
        self.value = 0
        self.is_enable = True
        self.create_slider()
        self.create_label()
    
    def create_slider(self):
        self.__slider = ctk.CTkSlider(master=self.root, from_=0, to=500, command=self.update_label)
        self.__slider.set(self.__slider.cget("from_"))
        self.__slider.grid(row=self.row, column=self.column)
    
    def create_label(self):
        self.__label = ctk.CTkLabel(master=self.root, text=f"{self.name}: 0")
        self.__label.grid(row=self.row+1, column=self.column)
        
    def update_label(self, val):
        self.__label.configure(text=f"{self.name}: {val}")
        self.value = val
        
    def __repr__(self) -> str:
        return f"{self.name}: {self.value}"
    


"""    
def update_label(label, val):
    name = label.cget("text").split()[0]
    label.configure(text=f"{name} {round(val, 4)}")

def create_slider_label(master, name, row, column, update_func):
    slider = ctk.CTkSlider(master=master, from_=0, to=500, command=lambda val: update_func(val))
    slider.set(slider.cget("from_"))
    label = ctk.CTkLabel(master=master, text=f"{name}: 0")
    slider.grid(row=row, column=column)
    label.grid(row=row + 1, column=column)
    return slider, label

# Create sliders and labels
kp_slider, kp_label = create_slider_label(manual_tuning_frame, "Kp", 0, 0, lambda val: update_label(kp_label, val))
ki_slider, ki_label = create_slider_label(manual_tuning_frame, "Ki", 2, 0, lambda val: update_label(ki_label, val))
kd_slider, kd_label = create_slider_label(manual_tuning_frame, "Kd", 4, 0, lambda val: update_label(kd_label, val))
"""