import yaml
from pathlib import Path


class ConfigLoader:
    _config = None

    @classmethod
    def load(cls):
        if cls._config is None:
            config_path = Path(__file__).parent.parent / "config.yml"

            with open(config_path, "r", encoding="utf-8") as file:
                cls._config = yaml.safe_load(file)

        return cls._config