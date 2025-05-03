"""
Module providing general functions for the web application.
"""

# pylint: disable=broad-exception-caught

import esptool
import io
from contextlib import redirect_stdout


def esp_get_info(file_path: str) -> str:
    """
    returns info from esp32 binary (.bin) file

    NOTE: esptool.main does not include an API to simply return its output
    we therefore need to redirect standard output

    REF: https://blog.golioth.io/tag/esptool-py/
    REF: https://stackoverflow.com/a/16571630/922013
    """
    if not file_path:
        return ""

    with redirect_stdout(io.StringIO()) as f:
        cmd = ["image_info", "--version", "2", file_path]

        try:
            esptool.main(cmd)
        except Exception as e:
            return str(e)

    return f.getvalue()
