FROM python:3.11-slim

WORKDIR /appdir

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY config.py .
COPY app/ app/
COPY tests/ tests/

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
