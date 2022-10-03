FROM python:3

WORKDIR /usr/src/server

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# we expose the listening port.
EXPOSE 8888

CMD [ "python", "./server.py" ]