# ☁️ localCloudLab – LocalStack + Azurite + Docker Compose

**localCloudLab** es un entorno de laboratorio unificado que permite simular servicios de **AWS** y **Azure** de forma completamente local, sin depender de cuentas reales, suscripciones ni tarjetas de crédito.

Ideal para quienes desean **aprender, practicar o automatizar entornos cloud** con total libertad y sin riesgos.

---

## 🚀 Características principales

- ☁️ Servicios de AWS simulados mediante **LocalStack**  
- ☁️ Servicios de Azure simulados mediante **Azurite**  
- 🐳 Despliegue rápido con **Docker Compose**  
- 🧑‍💻 Compatible con **Python**, `boto3`, `awslocal`, `azure-storage-blob`, etc.  
- ⚙️ Permite prácticas de automatización, integración y DevOps sin costos  

---

## ⚙️ Inicio rápido

1. **Cloná el repositorio:**
   ```bash
   git clone https://github.com/gpachello/localCloudLab.git
   cd localCloudLab

2. **Levantá el entorno:**
   ```bash
   docker compose up -d

3. **Verificá el estado:**
   ```bash
   docker compose ps

Deberías ver los servicios localstack, azurite y app ejecutándose:
   ```bash
   NAME         IMAGE                                     COMMAND                  SERVICE      CREATED          STATUS                    PORTS
   azurite      mcr.microsoft.com/azure-storage/azurite   "docker-entrypoint.s…"   azurite      44 seconds ago   Up 39 seconds             0.0.0.0:10000-10002->10000-10002/tcp
   cloud-app    localcloudlab-app                         "/usr/local/bin/entr…"   app          41 seconds ago   Up 36 seconds             0.0.0.0:2200->22/tcp
   localstack   localstack/localstack:latest              "docker-entrypoint.sh"   localstack   44 seconds ago   Up 38 seconds (healthy)   127.0.0.1:4510-4559->4510-4559/tcp, 127.0.0.1:4566->4566/tcp, 5678/tcp
