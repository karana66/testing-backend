FROM tensorflow/tensorflow:latest

WORKDIR /app/backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update \
    && apt-get install postgresql postgresql-contrib -y \
    && apt-get install ffmpeg libsm6 libxext6  -y \
    && apt-get install netcat -y

# install requirements
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /app/backend/entrypoint.sh
RUN chmod +x /app/backend/entrypoint.sh

COPY . .

ENTRYPOINT ["/app/backend/entrypoint.sh"]