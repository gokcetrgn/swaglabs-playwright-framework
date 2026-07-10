import yaml
from pathlib import Path


class DataLoader:

    @staticmethod
    def load(file_path):
        file = Path(file_path)

        with open(file, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)