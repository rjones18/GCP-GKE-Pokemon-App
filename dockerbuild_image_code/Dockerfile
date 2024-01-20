FROM rjones21/pythonbaseimage:latest
# COPY requirements.txt .
# RUN pip install -r requirements.txt
WORKDIR /myapp
COPY main.py /myapp/main.py
COPY templates/ /myapp/app/
COPY static/ /myapp/app/
CMD ["python", "/myapp/main.py"]

