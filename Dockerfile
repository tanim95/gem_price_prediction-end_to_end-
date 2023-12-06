FROM python:3.8

WORKDIR /app

COPY . .

RUN python -m venv venom
          
RUN source venom/bin/activate

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD [ "python", "application.py" ]
