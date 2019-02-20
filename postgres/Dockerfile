FROM library/postgres
ENV POSTGRES_USER docker
ENV POSTGRES_PASSWORD super_strong_password
ENV POSTGRES_DB psko_app

COPY init.sql /docker-entrypoint-initdb.d/