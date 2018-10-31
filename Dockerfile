FROM python:2.7
ADD goodreads_export.csv /
ADD converter.py /
CMD ["python", "./converter.py"]
