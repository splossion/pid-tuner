import customtkinter

class firstPage:
    def __init__(self, app) -> None:
        self.__app = app
        self.button = customtkinter.CTkButton(self.__app, text="my button", command=self.button_callbck)
        self.button.pack(padx=20, pady=20)

    def button_callbck(self):
        print("button clicked")