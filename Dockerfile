FROM python:3.9 as gunicorn-build
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app
WORKDIR /app
COPY demo_project/requirements.txt .
RUN pip install -r requirements.txt
COPY compose/gunicorn/entrypoint.sh /
RUN chmod +x "/entrypoint.sh"
COPY demo_project ./

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/usr/local/bin/gunicorn", "-b", "0.0.0.0:8000", "demo.wsgi:application"]
