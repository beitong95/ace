import torch
from ace_network import Regressor

pt_model_path = "/home/bizon/beitong/ace/output/own/office2_240p.pt"
onnx_model_path = "model_output_tflite/model.onnx"
encoder_path = "/home/bizon/beitong/ace/ace_encoder_pretrained.pt"
encoder_state_dict = torch.load(encoder_path, map_location="cpu")
head_state_dict = torch.load(pt_model_path, map_location="cpu")
network = Regressor.create_from_split_state_dict(encoder_state_dict, head_state_dict).eval()
sample_input = torch.rand((1, 1, 240, 426))
torch.onnx.export(
    network,                  # PyTorch Model
    sample_input,                    # Input tensor
    onnx_model_path,        # Output file (eg. 'output_model.onnx')
    opset_version=12,       # Operator support version
    input_names=['input'],   # Input tensor name (arbitary)
    output_names=['output'] # Output tensor name (arbitary)
)