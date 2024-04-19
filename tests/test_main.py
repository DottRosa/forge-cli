"""
Tests the Forge CLI
"""

from unittest import mock
import pytest
from forge.main import read_config, get_config_path


def test_get_config_path():
    """Test the get_config_path function to ensure it returns the correct path."""
    with mock.patch("os.path.realpath", return_value="/path/to/script.json"):
        with mock.patch("os.path.dirname", return_value="/path/to"):
            config_path = get_config_path()
            assert config_path == "/path/to/default_config.json"


def test_read_config_file_exists():
    """Test read_config when the .forge.json file already exists."""
    with mock.patch("builtins.open", mock.mock_open(read_data='{"key": "value"}')):
        with mock.patch("json.load", return_value={"key": "value"}):
            assert read_config() == {"key": "value"}


def test_read_config_file_not_exists_user_creates():
    """Test read_config when .forge.json does not exist and the user chooses to create it."""
    with mock.patch("builtins.open", mock.mock_open()) as mocked_file:
        mocked_file.side_effect = [FileNotFoundError(), mock.DEFAULT, mock.DEFAULT]
        with mock.patch("json.load", return_value={"default_key": "default_value"}):
            with mock.patch("builtins.input", return_value="y"):
                with mock.patch(
                    "forge.main.get_config_path",
                    return_value="/path/to/default_config.json",
                ):
                    assert read_config() is None
                    mocked_file.assert_called_with(
                        ".forge.json", mode="w", encoding="utf-8"
                    )


def test_read_config_file_not_exists_user_declines():
    """Test read_config when .forge.json does not exist and the user chooses not to create it."""
    with mock.patch("builtins.open", mock.mock_open()) as mocked_file:
        mocked_file.side_effect = FileNotFoundError()
        with mock.patch("builtins.input", return_value="n"):
            assert read_config() is None
            mocked_file.assert_called_with(".forge.json", mode="r", encoding="utf-8")


# Run the tests
if __name__ == "__main__":
    pytest.main()
