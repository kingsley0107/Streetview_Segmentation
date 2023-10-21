from reference.object_dict import names, colors
from mit_semseg.utils import colorEncode
import numpy
import PIL.Image


def visualize_result(img, pred, index=None):
    # filter prediction class if requested
    if index is not None:
        pred = pred.copy()
        pred[pred != index] = -1
        print(f"{names[index+1]}:")

    # colorize prediction
    pred_color = colorEncode(pred, colors).astype(numpy.uint8)

    # aggregate images and save
    im_vis = numpy.concatenate((img, pred_color), axis=1)
    PIL.Image.fromarray(im_vis)
