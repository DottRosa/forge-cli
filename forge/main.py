#!/usr/bin/env python3
import json


def read_config():
    """Read the configuration file .forge.json."""
    with open(".forge.json", "r") as file:
        config = json.load(file)
    return config


def main():
    # Load configuration file
    read_config()


if __name__ == "__main__":
    main()
