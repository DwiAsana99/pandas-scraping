import os
import pandas as pd

from sqlalchemy import create_engine

def Load(data,nama_tabel):
    path_config = os.getcwd()
    with open(path_config + '\config\config.conf','r') as file:
        conf = file.readlines()
    db = {}
    for line in conf:
        line = line.replace('\n','').split('=')
        if len(line) == 2:
            db[line[0]] = line[1]
      # Connection DB
    conn_string = f"postgresql+psycopg2://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}"
    engine = create_engine(conn_string)
    
    data.to_sql(name=nama_tabel, con=engine, if_exists='replace', index=False)
    print('Data success export Database !')     