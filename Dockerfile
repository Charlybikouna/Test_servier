FROM python:3.7.1-stretch
ADD . /code
WORKDIR /code
RUN pip install --upgrade pip
RUN apt update
RUN pip install -r requirement.txt
RUN python -m nltk.downloader punkt
CMD ["python" , "pipeline.py"]



