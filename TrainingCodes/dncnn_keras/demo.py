import tensorflow as tf

# Print TensorFlow version
print("TensorFlow version:", tf.__version__)

# Check if GPU is available and being used
if tf.config.list_physical_devices('GPU'):
    print("TensorFlow is using GPU")
    print("GPU devices:", tf.config.list_physical_devices('GPU'))
else:
    print("No GPU available. TensorFlow is using CPU")
