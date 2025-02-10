#!/usr/bin/env python3

import yaml
import requests
import os
from datetime import datetime

# Load the YAML file
config_path = os.path.join(
    os.path.dirname(__file__), os.path.join("dependencies", "config.yaml")
)
if os.path.exists(config_path):
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
else:
    raise FileNotFoundError(f"Configuration file not found: {config_path}")

# Extract dependencies from the YAML file
dependencies = config["dependencies"]

for dependency in dependencies:
    response = requests.get(dependency["page"])
    if response.status_code == 200:
        response_text = "\n".join(response.text.split("\n")[1:])
        os.makedirs(os.path.dirname(dependency["path"]), exist_ok=True)
        with open(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)), dependency["path"]
            ),
            "w",
        ) as file:
            current_datetime = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
            file.write(
                f"+++\ntitle = '{dependency['title']}'\ndate = '{current_datetime}'\n+++\n\n{response_text}"
            )
    else:
        print(f"Failed to download {dependency['page']}")
