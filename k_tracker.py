from k_slider import kSlider
from k_entry import entryBox

class kTracker:
    def __init__(self, name, slider_frame, manual_frame, row, column) -> None:
        self.value = 0
        self.name = name
        self.k_slider = kSlider(slider_frame, self.name, row, column)
        self.k_entrybox = entryBox(manual_frame, self.name, row, column)
