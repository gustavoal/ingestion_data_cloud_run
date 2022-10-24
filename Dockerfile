FROM python:3.8-slim

WORkDIR ./app

COPY . /app

ARG PROJECT_ID
ENV projeto_id_gcp=$PROJECT_ID

EXPOSE 8101

RUN pip install -r requirements.txt

CMD python main.py