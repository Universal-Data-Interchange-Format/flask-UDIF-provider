# flask-UDIF-provider
This provider is for providing users with their data in UDIF


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
    GRAPHQL_URL=https://streamlytics-graphql-v3-tus3qiegjq-uc.a.run.app/graphql
    WEBHOOK_URL=http://web:5000/udif/done

### 2. Install docker and docker-compose

### 3. Run
    docker-compose up -d

### 4. Visiting flower
    flower port: 5555
    api port: 5000

### 5. API

    endpoint: http://34.68.254.175:5000/udif/create
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
    https://console.cloud.google.com/compute/instancesDetail/zones/us-central1-a/instances/flask-udif-provider?project=clture-productions