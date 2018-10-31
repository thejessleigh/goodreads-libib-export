FROM python:2.7
COPY goodreads_export.csv /
COPY converter.py /
CMD ["python", "./converter.py"]
