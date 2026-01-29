from pathlib import Path

def get_image_path(file_name):
    folder = Path(__file__).resolve().parent
    return folder/'images'/file_name