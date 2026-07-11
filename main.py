import pytest
from common.config_loader import ConfigLoader

config = ConfigLoader.load()

args = [
    "projects/Swaglabs/scenarios",
    "--alluredir=results/allure-results",
   "-n",
   "auto",
]

for browser in config["execution"]["browsers"]:
    args.append(f"--browser={browser}")

if __name__ == "__main__":
    pytest.main(args)