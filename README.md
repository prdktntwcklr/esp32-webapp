# ESP32 Web App

This is a simple web application to display information about ESP32 binaries.
Users can upload a binary file and receive information such as the project
name, compile time, and ESP-IDF version directly from within their web browser.

The binary analyzer uses the official [espressif/esptool](https://github.com/espressif/esptool)
utility that runs integrated into a Python backend built with Flask.

## Screenshot

The screenshot below shows the output from a successfully analyzed binary.

![Binary Info Success](docs/esp_webapp_success.png)

## Project structure

- `app` - web application built with Flask
- `examples/hello_world` – simple example application for ESP32 that can be
analyzed
- `tests` - collection of unit and integration tests

## Using Docker to build the example application for ESP32

To avoid having to install the complete `ESP-IDF` toolchain on your machine, you
can use a pre-built `Docker` image that includes all required dependencies.

Run the following command from a terminal to build the binaries for the `hello_world`
application:

```bash
docker compose run --rm idf-build
```

Refer to the [relevant parts of the ESP-IDF documentation](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/tools/idf-docker-image.html)
for details on how to use the ESP-IDF Docker image.

## Running the project locally

You can run this project locally on your machine using Docker.

First, build the Docker image from the project directory:

```bash
docker build -t flask-app .
```

This command will create an image called flask-app using the Dockerfile in the
top-level directory of this repo.

Once the image is built, run the Flask app in a Docker container:

```bash
docker run --rm -p 5000:5000 flask-app
```

This will start the Flask app inside the container, and map port `5000` in the
container to port `5000` on your host machine. You should see the following logs
appearing in your terminal:

```text
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
```

You can then access the application in your web browser at the above URL:

```text
http://127.0.0.1:5000/
```

## Tests

Once the image is built (see above), run the tests inside the container:

```bash
docker run --rm flask-app pytest -v
```

## CI/CD Pipeline

Both the build of the example application and the tests run automatically as
part of a CI/CD pipeline on every pull request. See [`.github/workflows/main.yml`](.github/workflows/main.yml)
for details.
