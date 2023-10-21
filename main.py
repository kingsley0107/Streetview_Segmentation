from utils.reader import image_to_pil
from utils.transform import img_to_tensor
from NetWork.model import predict
from reference.index_formula import cal_normal_index, cal_AI, cal_EPI

path = r'./images/8pcguVQpxRMikWptAhcM8w.jpg'
pil_image = image_to_pil(path)
singleton_batch, output_size = img_to_tensor(pil_image)
result = predict(singleton_batch, output_size)
print(f"GreenView Index:{cal_normal_index(result, 'GVI')}")
print(f"SpatialBoundary Index:{cal_normal_index(result, 'SBI')}")
print(f"Accessibility Index:{cal_AI(result)}")
print(f"EnclosurePerception Index:{cal_EPI(result)}")
