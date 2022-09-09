# Library Imports
import numpy
import pathlib
import tkinter
import matplotlib.pyplot
from tkinter import messagebox, filedialog

# Source Code Import
import object_detection_train

 
# Create Window
window = tkinter.Tk()
window.title("Sensors CDT Team Challenge 2022")

# Load CDT and Cyanovision Logos
sensors_cdt_logo = tkinter.PhotoImage(file = "sensors_cdt_logo.png")
cyanovision_logo = tkinter.PhotoImage(file = "cyanovision_logo.png")
window.geometry("%dx%d" % (cyanovision_logo.width(), cyanovision_logo.height()))

# Create Canvas
canvas = tkinter.Canvas(width = cyanovision_logo.width(), height = cyanovision_logo.height())
canvas.pack(side = "bottom", fill = "both", expand = "yes")

# Add CDT and Cyanovision Logos
canvas.create_image(0, 0, anchor = "nw", image = cyanovision_logo)
canvas.create_image(0, 0, anchor = "nw", image = sensors_cdt_logo)

tkinter.Label(canvas, width = 22, font = ("Arial", 24), fg = "midnightblue",
              text = "Choose Desired Mode", justify = "center").pack(anchor = "w", padx = (200), pady = (260, 20))


# Object Detection Model Training
def train_object_detection_button():
    messagebox.showinfo("Message", "Please select directory including the images of your dataset and the processed CSV titled 'dataset.csv' in the same folder")

    # Get Directory
    directory_path = tkinter.filedialog.askdirectory()
    dataset_directory = pathlib.Path(directory_path)

    if (directory_path != 0):
        epochs = tkinter.IntVar()
        train_object_detection.pack_forget()

        # Fewer Epochs Option
        tkinter.Label(canvas, width = 23, font = ("Arial", 18), fg = "midnightblue", justify = "center",
                      text = "Faster but Less Accurate").pack(anchor = "w", padx = (230), pady = (10, 0))

        tkinter.Radiobutton(canvas, width = 30, font = ("Arial"), indicatoron = 0, variable = epochs,
                            value = 20, text = "20 Epochs").pack(anchor = "w", padx = (230), pady = (5, 10))

        # More Epochs Option
        tkinter.Label(canvas, width = 23, font = ("Arial", 18), fg = "midnightblue", justify = "center",
                      text = "Slower but More Accurate").pack(anchor = "w", padx = (230), pady = (10, 0))

        tkinter.Radiobutton(canvas, width = 30, font = ("Arial"), indicatoron = 0, variable = epochs,
                            value = 40, text = "40 Epochs").pack(anchor = "w", padx = (230), pady = (5, 10))

        # Begin Training Option
        tkinter.Button(canvas, width = 60, height = 5, font = ("Arial", 16), text = "Run Model Training",
                       command = lambda: run_object_detection_train(epochs.get(), dataset_directory)).pack(anchor = "w", padx = (75), pady = (40))


# Method Invoking Object Detection Model Training
def run_object_detection_train(epochs, dataset_directory):
    train_object_detection.pack_forget()

    print("========== Invoking Object Detection Model Training with", epochs, "Epochs ==========")
    messagebox.showinfo("Message", "Please check the terminal output...")

    window.withdraw()
    window.destroy()

    # Invoke training
    object_detection_train.main(epochs, dataset_directory)


# Button Invoking Object Detection Model Training
train_object_detection = tkinter.Button(canvas, width = 60, height = 5, font = ("Arial", 16),
                                        text = "Train Object Detection Model",
                                        command = lambda: train_object_detection_button())
train_object_detection.pack(anchor = "w", padx = (75), pady = (50))


window.mainloop()
