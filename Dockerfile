FROM python:2.7
ARG export_file
COPY $export_file /
COPY converter.py /
CMD ["python", "./converter.py"]
