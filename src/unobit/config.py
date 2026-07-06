from pathlib import Path
import yaml


class Config:

    def __init__(self, filename: str = "config/config.yaml"):

        self.filename = Path(filename)

        if not self.filename.exists():
            self.filename = Path("config/config.example.yaml")

        with open(self.filename, encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    def get(self, *keys):

        value = self.data

        for key in keys:
            value = value[key]

        return value