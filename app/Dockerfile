FROM python:3.6
ADD . /psko-devops-demo
WORKDIR /psko-devops-demo
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]