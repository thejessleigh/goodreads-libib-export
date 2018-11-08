FROM python:3.7
ARG export_file=goodreads.csv
COPY $export_file goodreads_export.csv
COPY converter.py /
CMD ["python", "./converter.py"]
