from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://wamdf02tnwplgc75v7sq:pscale_pw_FvZvNHQTRA6xZIYl7IqEo7jFmMuBj1Y7G3KtGhQc1hk@aws.connect.psdb.cloud/telecomcompany?charset=utf8mb4"

engine = create_engine(
     db_connection_string,
     connect_args={
          "ssl": {
             "ssl_ca": "/etc/ssl/cert.pem"
     }
})
