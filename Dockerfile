FROM python:3.9

WORKDIR /docker_square

COPY . .
CMD ["python", "square.py"]