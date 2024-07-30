ARG PYTHON_VERSION=3.8.10
FROM python:${PYTHON_VERSION}-slim AS base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1


# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1


WORKDIR /app

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser
    # Download dependencies as a separate step to take advantage of Docker's caching.
    # Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
    # Leverage a bind mount to requirements.txt to avoid having to copy them into
    # into this layer.
    
    # Switch to the non-privileged user to run the application.
    
    
    # Copy the source code into the container.
    # COPY ./activity.sqlite .
    # COPY ./admin.sqlite .
    # COPY ./social_gamification.sqlite .
    # RUN chown appuser:appuser db_data/activity.sqlite
    # RUN chown appuser:appuser  db_data/admin.sqlite 
    # RUN chown appuser:appuser db_data/social_gamification.sqlite
    # RUN chmod 777 db_data/activity.sqlite
    # RUN chmod 777  db_data/admin.sqlite 
    # RUN chmod 777 db_data/social_gamification.sqlite
    # RUN  python -m venv .venv
    # RUN source ./.venv/bin/activate
# RUN python3 -m pip install --upgrade pip
    
# RUN python3 -m venv .venv
# RUN source ./.venv/bin/activate
# RUN  python3 -m pip install -t ./dist
RUN  --mount=type=cache,target=/root/.cache/pip \ 
--mount=type=bind,source=dist/adminproject-0.0.1-py3-none-any.whl,target=adminproject-0.0.1-py3-none-any.whl \
python3 -m pip install  adminproject-0.0.1-py3-none-any.whl waitress

RUN mkdir /usr/local/var && chown appuser:appuser /usr/local/var
# RUN flask --app my-admin build-test-admin-sg-ac-db
# RUN flask build-test-admin-sg-ac-db
# RUN pip install waitress
# RUN chmod 777 /usr/local/var
# 
USER appuser

COPY ./.env ./config.py ./
COPY ./db_data ./
# Expose the port that the application listens on.
EXPOSE 8080
# CMD [ "pwd" ]
# Run the application.
# CMD  pwd  && source ./.venv/bin/activate && python3 -m flask run --debug
# CMD  pwd  && flask --app  my_admin  run --debug
# CMD pip list
# CMD ls -la db_data
# CMD pip list && ls -la && flask --app admin-project build-test-admin-sg-ac-db && flask run --debug
CMD pip list &&  ls -la && flask --app adminproject build-test-admin-sg-ac-db && waitress-serve --call adminproject:create_app
# CMD chmod 777 /usr/local/var && ls -la && flask --app admin-project build-test-admin-sg-ac-db && flask run --debug
# CMD flask --app my-admin build-test-admin-sg-ac-db && waitress-serve --call 'my-admin:create_app'

# CMD  pwd  && python3 -m flask --app my_admin run --debug
# CMD pwd && python3 -m flask build-test-admin-sg-ac-db && flask run --debug
# CMD  python -m pip install -r requirments.txt && RUN flask build-test-admin-sg-ac-db && flask run --debug

