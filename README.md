# ESP32 Web App

This is a simple web application to display information about ESP32 binaries. Users can upload a binary file and receive information such as the project name, compile time, and ESP-IDF version directly from within their browser.

## Using Docker to build the example application for ESP32

From within `examples/hello_world`, run the following command from a Powershell prompt

```Powershell
docker run --rm -v ${PWD}:/project -w /project -e HOME=/tmp -e IDF_TARGET='esp32' espressif/idf:release-v5.3 idf.py build
```

You can also refer to the relevant [ESP-IDF documentation](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/tools/idf-docker-image.html)
for details.

## Running the project locally

You can run this project locally on your machine. From within a [virtual environment](https://docs.python.org/3/library/venv.html),
install the required dependencies:

```Powershell
pip install -r requirements.txt
```

And start the development server by typing:

```Powershell
flask run
```

You can then visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to try out the application.

## Running tests

The application is covered by a set of unit and integration tests. To run the tests, execute the following command from within your Python virtual environment:

```Powershell
pytest -v
```

These tests also run automatically as part of a CI/CD pipeline when creating a new pull request.
