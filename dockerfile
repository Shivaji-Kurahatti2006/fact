FROM python:3.14-slim
WORKDIR docker_fact
COPY . .
CMD ["python","fact.py"]