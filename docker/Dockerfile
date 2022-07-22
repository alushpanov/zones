FROM python:3.9
# alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y gdal-bin libgdal-dev
RUN apt-get install -y python3-gdal
RUN apt-get install -y binutils libproj-dev
RUN python3 -m pip install -r requirements.txt

COPY . /app
WORKDIR /app

#RUN \
#  apk --update add && \
#  apk add postgresql-libs && \
#  python3 -m pip install -r requirements.txt --no-cache-dir && \
#  addgroup -S appgroup && \
#  adduser -S appuser -G appgroup && \
#  chown appuser:appgroup /app

#COPY --chown=appuser:appgroup . .

#USER appuser
#CMD ["/app/docker/entrypoint.sh"]