from reference.index_table import REFERENCE_TABLE, GROUPS
from reference.index_table import INDEX_GROUPS_Numerator

import numpy as np
from itertools import chain


def cal_pixels(pred, index_type):
    numerator_types = INDEX_GROUPS_Numerator[index_type]
    numerator_subtypes = list(
        chain.from_iterable([GROUPS[i] for i in numerator_types]))
    numerator_indices = [REFERENCE_TABLE[i] for i in numerator_subtypes]
    target_numerator_pixels = len(pred[np.isin(pred, numerator_indices)])
    return target_numerator_pixels


def cal_normal_index(pred, index_type):
    # 空间边界指数 spatial boundary index
    # boundary pixels / total pixels
    if index_type not in [
            'SBI', 'SLI', 'SVI', 'TFI', 'PSI', 'SI', 'GVI', 'SAI'
    ]:
        raise TypeError('index type error')
    target_numerator_pixels = cal_pixels(pred, index_type)
    return round(target_numerator_pixels / len(pred.flatten()), 2)


def cal_EPI(pred):
    # 围合感知指数 enclosure perception index
    EPI_Numerator_pixels = cal_pixels(pred, 'EPI')
    EPI_Denominator_pixels = cal_pixels(pred, "EPI_D")
    try:
        res = round(EPI_Numerator_pixels / EPI_Denominator_pixels, 2)
    except Exception:
        res = 999
    return res


def cal_AI(pred):
    # 通行性指数 accessibility index
    AI_Numerator_pixels = cal_pixels(pred, 'AI')
    AI_Denominator_pixels = cal_pixels(pred, "AI_D")
    try:
        res = round(AI_Numerator_pixels / AI_Denominator_pixels, 2)
    except Exception:
        res = 999
    return res
