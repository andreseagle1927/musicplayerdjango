FROM python:3.10

ENV PYTHONUNBUFFERED = 1

WORKDIR /code

COPY requi.txt .

RUN pip install -r requi.txt

COPY . .

EXPOSE 8000

CMD ["python","manage.py", "runserver"]



