import customtkinter as ctk
from plot import realTimePlotApp
from frame import myFrame
from k_tracker import kTracker

app = ctk.CTk()
app.geometry("750x750")

slider_tuning_frame = myFrame(app, 0, 0)
manual_tuning_frame = myFrame(app, 1, 0)
kp = kTracker("Kp", slider_tuning_frame, manual_tuning_frame, 0, 0)
ki = kTracker("Ki", slider_tuning_frame, manual_tuning_frame, 2, 0)
kd = kTracker("Kd", slider_tuning_frame, manual_tuning_frame, 4, 0)

plot_frame = myFrame(app, 0, 1, 2, 2)
plot = realTimePlotApp(plot_frame)

app.mainloop()