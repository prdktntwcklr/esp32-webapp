"""
Tests the functions.py module.
"""

from app.main.functions import esp_get_info

from unittest.mock import patch


@patch("esptool.main")
def test_empty_filename(mock_esptool_main):
    mock_esptool_main.return_value = None
    _ = esp_get_info("")
    mock_esptool_main.assert_not_called()


@patch("esptool.main")
def test_with_filename(mock_esptool_main):
    mock_esptool_main.return_value = None
    _ = esp_get_info("sample.bin")
    mock_esptool_main.assert_called_once_with(["image_info", "--version", "2",
                                               "sample.bin"])


@patch("esptool.main", side_effect=Exception("Failed to parse binary"))
def test_exception_thrown(mock_esptool_main):
    result = esp_get_info("faulty.bin")
    assert result == "Failed to parse binary"
    mock_esptool_main.assert_called_once_with(["image_info", "--version", "2",
                                               "faulty.bin"])


def esptool_main_success(cmd):
    """
    Mocks the esptool.main function to print a success output.
    """
    _ = cmd  # unused argument
    print("Mock ESP-IDF v4.7.0")


@patch("esptool.main", side_effect=esptool_main_success)
def test_esp_get_info_success(mock_esptool_main):
    """
    Tests the function when esptool.main successfully returns info.
    """
    result = esp_get_info("dummy.bin")
    assert "Mock ESP-IDF v4.7.0" in result
    mock_esptool_main.assert_called_once_with(["image_info", "--version", "2",
                                               "dummy.bin"])
