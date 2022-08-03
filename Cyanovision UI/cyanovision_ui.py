# Library Imports
import numpy
import pathlib
import tkinter
import matplotlib.pyplot
from tkinter import messagebox, filedialog

# Source Code Imports
#import classification_train
#import segmentation_train


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


# Classification Model Training
def train_classification_button():
    messagebox.showinfo("Message", "Please select directory including images with and without cyanobacteria in different folders")

    # Get Directory
    directory_path = tkinter.filedialog.askdirectory()
    dataset_directory = pathlib.Path(directory_path)

    if (directory_path != 0):
        epochs = tkinter.IntVar()
        train_segmentation.pack_forget()
        train_classification.pack_forget()

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
                       command = lambda: run_classification_train(epochs.get(), dataset_directory)).pack(anchor = "w", padx = (75), pady = (40))


# Method Invoking Classification Model Training
def run_classification_train(epochs, dataset_directory):
    train_classification.pack_forget()
    train_segmentation.pack_forget()

    print("========== Invoking Classification Model Training with", epochs, "Epochs ==========")
    messagebox.showinfo("Message", "Please check the terminal output...")

    window.withdraw()
    window.destroy()

    # Invoke training
    #classification_train.main(epochs, dataset_directory)


# Segmentation Model Training
def train_segmentation_button():
    messagebox.showinfo("Message", "Please select directory including original and segmented cyanobacteria images in different folders")

    # Get Directory
    directory_path = tkinter.filedialog.askdirectory()
    dataset_directory = pathlib.Path(directory_path)

    if (directory_path != 0):
        epochs = tkinter.IntVar()
        train_segmentation.pack_forget()
        train_classification.pack_forget()

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
                       command = lambda: run_segmentation_train(epochs.get(), dataset_directory)).pack(anchor = "w", padx = (75), pady = (40))


# Method Invoking Segmentation Model Training
def run_segmentation_train(epochs, dataset_directory):
    train_classification.pack_forget()
    train_segmentation.pack_forget()

    print("========== Invoking Segmentation Model Training with", epochs, "Epochs ==========")
    messagebox.showinfo("Message", "Please check the terminal output...")

    window.withdraw()
    window.destroy()

    # Invoke training
    #segmentation_train.main(epochs, dataset_directory)


# Button Invoking Classification Model Training
train_classification = tkinter.Button(canvas, width = 60, height = 5, font = ("Arial", 16),
                                      text = "Train Classification Model",
                                      command = lambda: train_classification_button())
train_classification.pack(anchor = "w", padx = (75), pady = (10, 10))

# Button Invoking Segmentation Model Training
train_segmentation = tkinter.Button(canvas, width = 60, height = 5, font = ("Arial", 16),
                                    text = "Train Segmentation Model",
                                    command = lambda: train_segmentation_button())
train_segmentation.pack(anchor = "w", padx = (75), pady = (10, 10))


window.mainloop()
