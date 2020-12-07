FROM python:3
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . /simple_site
WORKDIR /simple_site

EXPOSE 8080
ENTRYPOINT ["python3", "run.py"]
