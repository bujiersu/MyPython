import torch

print("CUDA =",torch.cuda.is_available()) # 查看CUDA是否可用
print("CUDA数量 = ", torch.cuda.device_count()) # 查看可用的CUDA数量
print("CUDA版本 = ", torch.version.cuda) # 查看CUDA的版本号
print("cuDNN版本 = ", torch.backends.cudnn.version())

print("torch版本 = ",torch.__version__)

print("GPU = ", torch.cuda.is_available()) # 测试GPU是否可用
print("GPU数量 = ", torch.cuda.device_count()) # 测试GPU数量
print("GPU信息 = ", torch.cuda.get_device_properties(0)) # 测试第一块显卡的具体信息
