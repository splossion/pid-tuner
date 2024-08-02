import customtkinter as ctk
from k_slider import kSlider
from frame import myFrame
from plot import realTimePlotApp

app = ctk.CTk()
app.geometry("750x750")

# MANUAL TUNING

manual_tuning_frame = myFrame(app, 0, 0)
plot_frame = myFrame(app, 0, 1)
plot = realTimePlotApp(plot_frame)

kp = kSlider(manual_tuning_frame, "Kp", 0, 0)
ki = kSlider(manual_tuning_frame, "Ki", 2, 0)
ki = kSlider(manual_tuning_frame, "Kd", 4, 0)



app.mainloop()