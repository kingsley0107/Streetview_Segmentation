from utils.reader import image_to_pil
from utils.transform import img_to_tensor
from NetWork.model import predict
from reference.index_formula import cal_normal_index
import os
from tqdm import tqdm
from config.config import IMG_PATH, OUTPUT_FILE
import pandas as pd

# from config.config import IMG_PATH, OUTPUT_FILE

# IMG_PATH = r'./data/2022_GSV'
# OUTPUT_FILE = r"./result.csv"


class IndexCalculator:
    def __init__(self) -> None:
        self.indics_values = {
            "GSV_ID": [],
            "Person": [],
            "Bike": [],
            "HeavyV": [],
            "LightV": [],
            "Facade": [],
            "WindowOpening": [],
            "Road": [],
            "Sidewalk": [],
            "StreetFurniture": [],
            "GreeneryTree": [],
            "GreeneryGrass": [],
            "Sky": [],
            "Nature": []
        }
        self.ori = pd.DataFrame()

    def gen_idx(self, pano_id):
        path = rf'{IMG_PATH}/{pano_id}.jpg'
        pil_image = image_to_pil(path)
        singleton_batch, output_size = img_to_tensor(pil_image)
        result = predict(singleton_batch, output_size)
        self.indics_values['GSV_ID'].append(pano_id)
        for idx in [
                'Person', 'Bike', 'HeavyV', 'LightV', 'Facade',
                'WindowOpening', 'Road', 'Sidewalk', 'StreetFurniture',
                'GreeneryTree', 'GreeneryGrass', 'Sky', 'Nature'
        ]:
            try:
                self.indics_values[idx].append(cal_normal_index(result, idx))
            except Exception:
                self.indics_values[idx].append('error')
        # try:
        #     self.indics_values['AI'].append(cal_AI(result))
        # except Exception:
        #     self.indics_values['AI'].append('error')
        # try:
        #     self.indics_values['EPI'].append(cal_EPI(result))
        # except Exception:
        #     self.indics_values['EPI'].append('error')

    def release_all(self):
        import pandas as pd
        result = pd.concat([self.ori, pd.DataFrame(self.indics_values)])
        return result


if __name__ == '__main__':
    calculator = IndexCalculator()
    path = r'./result.csv'
    if os.path.exists(path):
        ori_pd = pd.read_csv(path)[[
            "GSV_ID", 'Person', 'Bike', 'HeavyV', 'LightV', 'Facade',
            'WindowOpening', 'Road', 'Sidewalk', 'StreetFurniture',
            'GreeneryTree', 'GreeneryGrass', 'Sky', 'Nature'
        ]]
        calculator.ori = ori_pd
        seg_res = pd.read_csv(path)['GSV_ID'].unique()
        existed_id = set(seg_res)
        flag = 1
    else:
        flag = 0
    try:
        for image in tqdm(os.listdir(IMG_PATH)):
            if image.endswith('.jpg'):
                panoid = os.path.splitext(image)[0]
                if flag == 1 and panoid not in existed_id:
                    try:
                        calculator.gen_idx(panoid)
                    except Exception:
                        continue
                elif flag == 1 and panoid in existed_id:
                    print(f'{panoid} have been caled!')
                    pass
                elif flag == 0:
                    try:
                        calculator.gen_idx(panoid)
                    except Exception:
                        continue
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        res = calculator.release_all()
        res.to_csv(OUTPUT_FILE)
    print(res)
