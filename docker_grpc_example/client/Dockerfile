FROM python:3

WORKDIR /usr/src/client

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# we must expose the port that will be running our flask app.
EXPOSE 5000

# we use python as an entrypoint (consider it an executable)
ENTRYPOINT [ "python" ]

CMD [ "./client.py" ]