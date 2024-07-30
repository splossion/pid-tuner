import customtkinter

class mainApp(customtkinter.CTk):
    def __init__(self, width = 100, height = 100):
        super().__init__()
        self.geometry(f"{width}x{height}")