from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://krifxfdh9vfyxfw8twa4:pscale_pw_NHGnZeETMeeaoA7cAtPvBPRWprL4XpPN7mJWVEhVhOi@aws.connect.psdb.cloud/telecomcompany?charset=utf8mb4"

engine = create_engine(
     db_connection_string,
     connect_args={
          "ssl": {
             "ssl_ca": "/etc/ssl/cert.pem"
     }
})
