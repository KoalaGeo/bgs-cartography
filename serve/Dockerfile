# Static symbology host: nginx (non-root, port 8080) serving /symbology/v3/...
#
#   docker build -f serve/Dockerfile \
#     --build-arg BASE_URL=https://symbology.example.org/symbology/v3 -t bgs-symbology .
#   docker run --rm -p 8080:8080 bgs-symbology      # -> http://localhost:8080/symbology/v3/
#
# BASE_URL is the public URL of the v3 folder; GeoServer SLDs and index.json point at it.

FROM python:3.12-alpine AS build
RUN apk add --no-cache bash
WORKDIR /src
COPY . .
ARG BASE_URL=http://localhost:8080/symbology/v3
RUN python3 scripts/make_web_styles.py . --base-url "$BASE_URL" \
 && scripts/assemble_site.sh /out

FROM nginxinc/nginx-unprivileged:1.27-alpine
COPY serve/nginx/default.conf /etc/nginx/conf.d/default.conf
COPY serve/nginx/symbology-headers.conf /etc/nginx/snippets/symbology-headers.conf
COPY --from=build /out/ /usr/share/nginx/html/symbology/
EXPOSE 8080
HEALTHCHECK CMD wget -qO- http://127.0.0.1:8080/healthz || exit 1
