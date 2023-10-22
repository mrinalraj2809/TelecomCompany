from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://y5tgeaux3lr0l278v729:pscale_pw_IdrfOa2xqxJ6g64TSoaC5UAutcC4beGLDZ0sUpLOJCf@aws.connect.psdb.cloud/telecomcompany?charset=utf8mb4"

engine = create_engine(
     db_connection_string,
     connect_args={
          "ssl": {
             "ssl_ca": "/etc/ssl/cert.pem"
     }
})
