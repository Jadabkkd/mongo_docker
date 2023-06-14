FROM python:3.7
COPY req.txt /Mongo_test/req.txt
WORKDIR /Mongo_test
RUN pip install -r req.txt
COPY . /Mongo_test
EXPOSE 8080
CMD [ "python","app.py" ]