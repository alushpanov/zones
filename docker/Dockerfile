FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y gdal-bin libgdal-dev
RUN apt-get install -y python3-gdal
RUN apt-get install -y binutils libproj-dev
RUN python3 -m pip install -r requirements.txt

RUN useradd -ms /bin/bash appuser
USER appuser

CMD ["/app/docker/entrypoint.sh"]