import PIL.Image


def image_to_pil(img_path):
    pil_image = PIL.Image.open(img_path).convert("RGB")
    return pil_image
