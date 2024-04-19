"""
Tests the Forge CLI
"""

import json

from unittest.mock import mock_open, patch
from forge.main import read_config


def test_read_config_success():
    """Tests the reading the configuration file"""

    mock_data = {
        "actions": [
            {"name": "Build project"},
            {"name": "Run tests"},
            {"name": "Clean project"},
        ]
    }
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
        with patch("json.load", return_value=mock_data):
            config = read_config()

            assert config == mock_data
            assert config["actions"][1]["name"] == "Run tests"
