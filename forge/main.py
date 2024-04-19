#!/usr/bin/env python3
"""main file of the Forge CLI"""

import json


def read_config():
    """Read the configuration file .forge.json."""
    with open(".forge.json", mode="r", encoding="utf-8") as file:
        config = json.load(file)
    return config


def main():
    """Main function of the CLI"""
    # Read the configuration file
    read_config()


if __name__ == "__main__":
    main()
