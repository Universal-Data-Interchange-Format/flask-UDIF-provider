# Flask UDIF Provider

A Flask-based provider that serves users their own data in UDIF 
(Universal Data Interchange Format).

Originally built and deployed at Streamlytics, Inc. (2020). 
Open sourced under Apache 2.0.

---

## Part of the UDIF Ecosystem

- [UDIF Specification](https://github.com/Universal-Data-Interchange-Format/udif) 
— the core standard
- [UDIF Python](https://github.com/Universal-Data-Interchange-Format/udif-python) 
— Python readers and writers
- [UDIF Storage](https://github.com/Universal-Data-Interchange-Format/udif-storage) 
— storage API

**Inventor:** UDIF was invented by [Angela Benton](https://angelabenton.com).

---

### 1. Set Environment

    ENV=local
    FLASK_DEBUG=1
    FLASK_APP=app/wsgi.py
    PORT=5000

    POSTGRES_USER=
    POSTGRES_PASS=
    POSTGRES_HOST=proxy
    POSTGRES_PORT=5432
    POSTGRES_DB=
    MAX_OVERFLOW=1
    POOL_SIZE=1

    APPLY_SCHEMA=False
    PROJECT_NAME=

    BUCKET_NAME=udif_data_bkt_prod
    GRAPHQL_URL=
    WEBHOOK_URL=http://web:5000/udif/done

    REDIS=redis

### 2. Install docker and docker-compose

### 3. Run

    docker-compose up -d

### 4. Visiting flower

    flower port: 5555
    api port: 5000

### 5. API

    endpoint: 
    method: GET

    body :
    {
        "user_id": string,
        "username": string,
        "requested_datetime": string
    }

    bucket_name: udif_data_bkt_prod
    blob_name: < username >_< requested_datetime >

### 6. Computer Engine Instance

[GCE](https://console.cloud.google.com/compute/instancesDetail/zones/us-central1-a/instances/flask-udif-provider?project=clture-productions)

### 7. GCP Kubernetes Engine

[GCP K8s Engine](https://console.cloud.google.com/kubernetes/clusters/details/us-central1-c/udif-data-provider-prod/details?cloudshell=false&project=clture-production)
