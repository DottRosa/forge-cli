#!/usr/bin/env python3
"""main file of the Forge CLI"""

import json
import os


def get_config_path():
    """
    Calculate the real path of the config file as the symbolic link does not know where to find it
    """
    # Original path
    script_path = os.path.realpath(__file__)
    # Calculate the path
    script_dir = os.path.dirname(script_path)
    config_path = os.path.join(script_dir, "default_config.json")

    return config_path


def read_config():
    """Read the configuration file .forge.json."""
    config_path = ".forge.json"

    try:
        with open(config_path, mode="r", encoding="utf-8") as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        response = input(
            "Seems that you don't have the configuration file. Do you want to create it? (y/n): "
        )
        if response.lower() == "y":
            # internal configuration file path
            internal_config_path = get_config_path()
            print(internal_config_path)
            # reading the internal configuration file
            with open(internal_config_path, mode="r", encoding="utf-8") as default_file:
                default_config = json.load(default_file)

            with open(config_path, mode="w", encoding="utf-8") as new_file:
                json.dump(default_config, new_file, indent=4)

            print("File .forge.json successfully created")

        return None


def main():
    """Main function of the CLI"""
    # Read the configuration file
    read_config()


if __name__ == "__main__":
    main()
