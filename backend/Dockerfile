FROM python:3.9.17-alpine3.18
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
ENV PORT=5000
EXPOSE 5000
ENV FLASK_APP=main.py
CMD flask run --host=0.0.0.0