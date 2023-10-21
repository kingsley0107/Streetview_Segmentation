from mit_semseg.models import ModelBuilder, SegmentationModule
import torch
from functools import lru_cache


@lru_cache()
def build_network():
    # Network Builders
    net_encoder = ModelBuilder.build_encoder(
        arch='resnet50dilated',
        fc_dim=2048,
        weights='ckpt/ade20k-resnet50dilated-ppm_deepsup/encoder_epoch_20.pth')
    net_decoder = ModelBuilder.build_decoder(
        arch='ppm_deepsup',
        fc_dim=2048,
        num_class=150,
        weights='ckpt/ade20k-resnet50dilated-ppm_deepsup/decoder_epoch_20.pth',
        use_softmax=True)
    return net_encoder, net_decoder


@lru_cache()
def build_model():
    net_encoder, net_decoder = build_network()
    crit = torch.nn.NLLLoss(ignore_index=-1)
    segmentation_module = SegmentationModule(net_encoder, net_decoder, crit)
    segmentation_module.eval()
    return segmentation_module


def predict(singleton_batch, output_size):
    model = build_model()
    with torch.no_grad():
        scores = model(singleton_batch, segSize=output_size)
    _, pred = torch.max(scores, dim=1)
    pred = pred.cpu()[0].numpy()
    return pred
