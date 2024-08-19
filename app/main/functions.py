def get_esp_info(destination):
    '''
    returns info from esp32 binary (.bin) file

    NOTE: esptool.main does not include an API to simply return its output
    we therefore need to redirect standard output
    reference: https://blog.golioth.io/tag/esptool-py/
    reference: https://stackoverflow.com/a/16571630/922013

    TODO: why are line breaks not preserved here?
    '''

    import io
    from contextlib import redirect_stdout

    with redirect_stdout(io.StringIO()) as f:
        import esptool
        cmd = ["image_info", "--version", "2", str(destination)]
        esptool.main(cmd)

    return f.getvalue()
