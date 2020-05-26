FROM python:3.8 AS builder

WORKDIR /workspaces
ADD . /workspaces

RUN pip install -r requirements.txt && pip install . && \
    cd src && \
    pyinstaller -F wsgi.py \
        --name app \
        --hidden-import=pkg_resources.py2_warn \
        --hidden-import=gunicorn.glogging \
        --hidden-import=gunicorn.workers.ggevent

FROM frolvlad/alpine-glibc
WORKDIR /workspaces
COPY --from=builder /workspaces/src/dist/app .
CMD ["./app"]