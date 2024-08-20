def esp_get_info(file_path: str) -> str:
    '''
    returns info from esp32 binary (.bin) file

    NOTE: esptool.main does not include an API to simply return its output
    we therefore need to redirect standard output
    reference: https://blog.golioth.io/tag/esptool-py/
    reference: https://stackoverflow.com/a/16571630/922013
    '''

    import io
    from contextlib import redirect_stdout

    with redirect_stdout(io.StringIO()) as f:
        import esptool
        cmd = ["image_info", "--version", "2", file_path]

        try:
            esptool.main(cmd)
        except Exception as e:
            return str(e)

    return f.getvalue()
