from utils.reader import image_to_pil
from utils.transform import img_to_tensor
from NetWork.model import predict
from reference.index_formula import cal_normal_index, cal_AI, cal_EPI
import os
from tqdm import tqdm


class IndexCalculator:
    def __init__(self) -> None:
        self.indics_values = {
            "SBI": [],
            "SLI": [],
            "SVI": [],
            "TFI": [],
            "PSI": [],
            "SI": [],
            "GVI": [],
            "SAI": [],
            "AI": [],
            "EPI": []
        }

    def gen_idx(self, pano_id):
        path = rf'C:\Users\20191\Desktop\streetview_images_crawler_Google\2022_GSV\{pano_id}.jpg'
        pil_image = image_to_pil(path)
        singleton_batch, output_size = img_to_tensor(pil_image)
        result = predict(singleton_batch, output_size)
        for idx in ['SBI', 'SLI', 'SVI', 'TFI', 'PSI', 'SI', 'GVI', 'SAI']:
            self.indics_values[idx].append(cal_normal_index(result, idx))
        self.indics_values['AI'].append(cal_AI(result))
        self.indics_values['EPI'].append(cal_EPI(result))

    def release_all(self):
        import pandas as pd
        result = pd.DataFrame(self.indics_values)
        return result


if __name__ == '__main__':
    calculator = IndexCalculator()
    for image in tqdm(
            os.listdir(
                r'C:\Users\20191\Desktop\streetview_images_crawler_Google\2022_GSV'
            )):
        if image.endswith('.jpg'):
            panoid = os.path.splitext(image)[0]
            calculator.gen_idx(panoid)
    res = calculator.release_all()
    print(res)
