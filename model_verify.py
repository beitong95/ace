import onnx
import numpy as np

# Load the ONNX model
model = onnx.load("/home/bizon/beitong/ace/model_output_tflite/model.onnx")

# Check that the IR is well formed
onnx.checker.check_model(model)

# Print a Human readable representation of the graph
onnx.helper.printable_graph(model.graph)

import onnxruntime as ort

ort_session = ort.InferenceSession("/home/bizon/beitong/ace/model_output_tflite/model.onnx")

outputs = ort_session.run(
    None,
    {'input': np.random.randn(1, 1, 240, 426).astype(np.float32)}
)

print(outputs)