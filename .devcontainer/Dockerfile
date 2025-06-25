FROM ubuntu:plucky
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y apache2 python3-pip
COPY index.html /var/www/html/index.html
CMD ["/bin/bash"]