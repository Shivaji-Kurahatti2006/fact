FROM python:3.14-slim
WORKDIR docker_fact
COPY . .
RUN pip install pytest
CMD ["pytest"]