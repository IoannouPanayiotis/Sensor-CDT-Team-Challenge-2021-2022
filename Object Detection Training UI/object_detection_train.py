# Required Packages (please install prior to running this code):
#   pip3 install tflite-model-maker==0.3.2
#   pip3 install -q pycocotools
#   pip3 install -q tflite-support
# If you encounter any errors, then also:
#   brew install libusb

def main(epochs, dataset_directory):
    # Library Imports
    from tflite_model_maker.config import ExportFormat
    from tflite_model_maker import object_detector
    from tflite_model_maker import model_spec
    import tensorflow as tf
    from PIL import Image
    import numpy as np
    import ssl
    import os

    ssl._create_default_https_context = ssl._create_unverified_context
    tf.get_logger().setLevel('ERROR')

    from absl import logging
    logging.set_verbosity(logging.ERROR)

    # Load Dataset
    os.chdir(dataset_directory)
    train_data, val_data, test_data = object_detector.DataLoader.from_csv("dataset.csv")

    # Create & train model
    spec = model_spec.get('efficientdet_lite2')
    # To make this run, we went to the source code of the model_maker API where these lines are defined:
    #     policy = tf.keras.mixed_precision.experimental.Policy(precision)
    #     tf.keras.mixed_precision.experimental.set_policy(policy)
    # and changed them to:
    #     policy = tf.keras.mixed_precision.Policy(precision)
    #     tf.keras.mixed_precision.set_global_policy(policy)
    # as the experimental version of Keras was removed depreciating the model_spec function.
    # Depending on your version of Keras, this may be required as well.

    spec.config.tflite_max_detections = 90
    spec.config.max_instances_per_image = 999

    model = object_detector.create(train_data, model_spec=spec, batch_size=4, train_whole_model=True, epochs=epochs, validation_data=val_data)

    model.evaluate(test_data)

    model.export(export_dir='.', tflite_filename='saved_object_detection_model.tflite')
