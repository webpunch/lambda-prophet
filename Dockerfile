FROM python:3.8-buster

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /var/task/venv/lib/python3.8/site-packages

COPY . .
