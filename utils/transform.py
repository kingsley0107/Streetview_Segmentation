import torchvision
import PIL.Image
from functools import lru_cache


@lru_cache()
def transformer():
    pil_to_tensor = torchvision.transforms.Compose([
        torchvision.transforms.ToTensor(),
        torchvision.transforms.Normalize(
            mean=[0.485, 0.456, 0.406],  # These are RGB mean+std values
            std=[0.229, 0.224, 0.225])  # across a large photo dataset.
    ])
    return pil_to_tensor


def img_to_tensor(pil_image: PIL.Image):
    pil_to_tensor = transformer()
    img_data = pil_to_tensor(pil_image)
    singleton_batch = {'img_data': img_data[None]}
    output_size = img_data.shape[1:]
    return singleton_batch, output_size
