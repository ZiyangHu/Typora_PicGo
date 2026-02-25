import numpy as np

class config_predict:
    """
    the config of prediction setting.
    """
    network = 'GCN' 
    num_nodes = 6250
    model_path = "logs/loss_2025_05_23_15_57_58/best_model.pth"
    output_folder = "predict/output/integral"
