FROM python:3.8

ADD hello.py .

CMD ["python3", "hello.py"]
