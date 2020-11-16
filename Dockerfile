FROM python

WORKDIR /app
RUN pip install flask-restful
COPY . /app
CMD python3 app.py