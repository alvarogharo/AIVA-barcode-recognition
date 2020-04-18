FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD [ "python", "src/web_server.py" ]
EXPOSE 5000