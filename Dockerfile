FROM python:3-alpine
MAINTAINER Ashkan Vahidishams "ashkan.vahidishams@sesam.io"
COPY ./service /service

RUN pip install -r /service/requirements.txt

EXPOSE 5001/tcp
ENTRYPOINT ["python"]
CMD ["./service/ntlmgetter.py"]