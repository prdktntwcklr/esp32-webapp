# ESP32 Web App

## Using Docker to build the example application

From within `examples/hello_world`, run the following command from a Powershell prompt

```Powershell
docker run --rm -v ${PWD}:/project -w /project -e HOME=/tmp -e IDF_TARGET='esp32' espressif/idf:release-v5.3 idf.py build
```

You can also refer to the relevant [ESP-IDF documentation](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/tools/idf-docker-image.html)
for details.
