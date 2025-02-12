import os

class PathConfig:
    """
    Configuration class to manage all file and directory paths.
    """
    def __init__(self):
        self.yolo_model_path = os.getenv("YOLO_MODEL_PATH", "models/yolov8.pt")
        self.image_upload_dir = os.getenv("IMAGE_UPLOAD_DIR", "uploads/")
        self.log_file = os.getenv("LOG_FILE", "logs/app.log")

class Config:
    """
    Main configuration class that initializes all path-related settings.
    """
    def __init__(self):
        self.paths = PathConfig()
        
config = Config()
