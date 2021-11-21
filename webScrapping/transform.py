import pandas as pd

def to_juta(str):
    data = str.replace("miliar", "")
    data = data.replace("$", "")
    juta = float(data)*1000
    juta = f"${juta} juta"
    return juta
 
def Transform(data):
#  empty data frame
 df=pd.DataFrame(columns=['nama','nomor_urut','kekayaan_bersih_usd','perusahaan','usia','kebangsaan','sumber_kekayaan','tahun'])
 df_orangkaya = data[1]
 for index,row in df_orangkaya.iterrows():
     nomor_urut = str(index+1)
     tahun='2018'
     kekayaan=to_juta(row['Kekayaan bersih (USD)'])
     df=df.append({'nama':row['Nama'],'nomor_urut':nomor_urut,'kekayaan_bersih_usd':kekayaan,'perusahaan':row['Sumber kekayaan'],'usia':row['Usia'],'kebangsaan':row['Kebangsaan'],'sumber_kekayaan':row['Sumber kekayaan'],'tahun':tahun},ignore_index=True)

 return df