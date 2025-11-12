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

Deberías ver los servicios localstack, azurite y app ejecutándose.
 
