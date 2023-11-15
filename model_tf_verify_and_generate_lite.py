import tensorflow as tf
import numpy as np
model = tf.saved_model.load('/home/bizon/beitong/ace/model_output_tflite/model.tf')
model.trainable = False

input_tensor = tf.random.uniform([1,1,240,426])
out = model(**{'input': input_tensor})

print(out)

# Convert the model

tflite_model_path = 'model_output_tflite/model_lite.tflite'

converter = tf.lite.TFLiteConverter.from_saved_model('/home/bizon/beitong/ace/model_output_tflite/model.tf')
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# scene = 'datasets/office2'
# image_height=240
# testset = CamLocDataset(
#     scene / "test",
#     mode=0,  # Default for ACE, we don't need scene coordinates/RGB-D.
#     image_height=image_height,
# )
# testset_loader = DataLoader(testset, shuffle=False, num_workers=4)

def representative_dataset_gen():
    for _ in range(10):
        # get sample input data as numpy array 
        input = np.random.rand(1, 1, 240, 426).astype(np.float32)
        yield [input]

converter.representative_dataset = representative_dataset_gen
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type = tf.uint8
converter.inference_output_type = tf.uint8
tflite_model = converter.convert()


# Save the model
with open(tflite_model_path, 'wb') as f:
    f.write(tflite_model)

import numpy as np
import tensorflow as tf

# Load the TFLite model and allocate tensors
interpreter = tf.lite.Interpreter(model_path=tflite_model_path)
interpreter.allocate_tensors()

# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Test the model on random input data
input_shape = input_details[0]['shape']
input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)

interpreter.invoke()

# get_tensor() returns a copy of the tensor data
# use tensor() in order to get a pointer to the tensor
output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data)
print(type(output_data))


