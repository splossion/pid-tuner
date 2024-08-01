import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x150")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callbck)
        self.button.pack()

    def button_callbck(self):
        print("button clicked")

app = App()
app.mainloop()