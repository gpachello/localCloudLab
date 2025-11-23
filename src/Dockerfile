FROM python:3.11-slim

# Instalación de sshd + sudo
RUN apt-get update && \
    apt-get install -y --no-install-recommends openssh-server sudo && \
    rm -rf /var/lib/apt/lists/*

# Crear usuario
RUN useradd -m -d /home/test -s /bin/bash -u 1000 test && \
    echo 'test:test' | chpasswd && \
    adduser test sudo

# Asegurar que sshd escuche en 0.0.0.0
RUN mkdir -p /var/run/sshd && \
    echo "ListenAddress 0.0.0.0" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
    echo "Banner /app/banner" >> /etc/ssh/sshd_config

EXPOSE 22

WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la app
COPY . .

# Copiar entrypoint
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
