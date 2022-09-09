# Cyanovision Repository ReadMe

This ReadMe file is intended to help users of the Cyanovision toolkit to explore this repository in order to be able to run inference on new images using an already-trained object detection model, to be able to train a new object detection model using their own dataset, and to be able to access the Genesis dataset that was collected, labelled and processed in this project for use in further research.

# Folders in the Repository

## Genesis Dataset

This folder includes the dataset that was captured, labelled, and processed in this project. It features 204 images for training, 15 images for validation, and 25 images for testing. Additionally, it includes a "dataset.csv" file that contains all the information for the labelled algae and cyanobacteria in those images. This dataset can be used for training machine learning models and for further research.

## LabelBox Data Exporting Code

This folder includes the Google Colab notebook that was used to export the labelled microscopy images from the LabelBox online toolkit that was used for labelling them.

## Object Detection Inference on New Images

This folder includes the visualization code that can be used to view the algae and cyanobacteria that are detected on new image samples by a TFLite object detection model. At its current version, it is set to use the object detection model that was trained using the Genesis dataset (see above) and to visualize the algae and cyanobacteria detected on the test part of this dataset, but it can be adapted to use a different model or visualize different images by simply changing the references in the respective cells of the Google Colab notebook.

## Object Detection Training Code

This folder includes the Google Colab notebooks that can be used to train an object detection model with the TensorFlow Lite Model Maker using a labelled microscopy dataset. These are the notebooks used to train the TFLite model that was built in this project, and they can be adapted to train a model on a new dataset by changing the path to the dataset's directory in the respective cell in the Google Colab notebook.

## Cyanovision Object Detection Training UI

This folder includes the Python code of the desktop software that can be used on the user's personal computer offline to train a model through a user-friendly interface. The software can be launched by typing "python3 cyanovision_ui.py" on the terminal, and then a friendly interface will pop up and guide the user to select a directory including their processed dataset to train a model. The first time someone uses this, the following packages (dependencies) will need to be installed through pip3: numpy, PIL, tensorflow, tkinter, tflite-model-maker==0.3.2, pycocotools, tflite-support, matplotlib, and pathlib. Additionally, the libusb package will need to be installed using brew.

# Trained Object Detection Model

This folder includes two object detection models that were trained in this project. These were trained using the Genesis dataset (see above), and achieved an average AP50 precision of 0.68 and 0.7 approximately. They are both in a TFLite format to ensure they are lightweight for running inference on the constrained Edge TPU accelerator.
