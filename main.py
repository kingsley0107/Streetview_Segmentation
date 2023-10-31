from utils.reader import image_to_pil
from utils.transform import img_to_tensor
from NetWork.model import predict
from reference.index_formula import cal_normal_index, cal_AI, cal_EPI
import os
from tqdm import tqdm
from config.config import IMG_PATH, OUTPUT_FILE


class IndexCalculator:
    def __init__(self) -> None:
        self.indics_values = {
            "GSV_ID": [],
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
        path = rf'{IMG_PATH}\{pano_id}.jpg'
        pil_image = image_to_pil(path)
        singleton_batch, output_size = img_to_tensor(pil_image)
        result = predict(singleton_batch, output_size)
        self.indics_values['GSV_ID'].append(pano_id)
        for idx in ['SBI', 'SLI', 'SVI', 'TFI', 'PSI', 'SI', 'GVI', 'SAI']:
            try:
                self.indics_values[idx].append(cal_normal_index(result, idx))
            except Exception:
                self.indics_values[idx].append('error')
        try:
            self.indics_values['AI'].append(cal_AI(result))
        except Exception:
            self.indics_values['AI'].append('error')
        try:
            self.indics_values['EPI'].append(cal_EPI(result))
        except Exception:
            self.indics_values['EPI'].append('error')

    def release_all(self):
        import pandas as pd
        result = pd.DataFrame(self.indics_values)
        return result


if __name__ == '__main__':
    calculator = IndexCalculator()
    try:
        for image in tqdm(os.listdir(IMG_PATH)):
            if image.endswith('.jpg'):
                panoid = os.path.splitext(image)[0]
                calculator.gen_idx(panoid)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        res = calculator.release_all()
        res.to_csv(OUTPUT_FILE)
    print(res)
