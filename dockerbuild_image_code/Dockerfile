FROM python:latest
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /myapp
COPY main.py /myapp/main.py
COPY templates/ /myapp/templates
COPY static/ /myapp/static
CMD ["python", "/myapp/main.py"]

