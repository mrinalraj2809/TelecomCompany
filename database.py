from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://4nv2jvc6dx72256cg07d:pscale_pw_GGBIzRIR2sEAsPvdhWHrvH9CvNUkQODA1uqBOxoqceV@aws.connect.psdb.cloud/telecomcompany?charset=utf8mb4"

engine = create_engine(
     db_connection_string,
     connect_args={
          "ssl": {
             "ssl_ca": "/etc/ssl/cert.pem"
     }
})
