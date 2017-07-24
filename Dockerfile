FROM python:3.5-onbuild
MAINTAINER "Bravi Solutions<contato@bravi.com.br>"
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client
EXPOSE 5000
CMD ["python", "app.py",]
