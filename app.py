from webScrapping import scraper, transform,load
import pandas as pd

if __name__=="__main__":
    # extract
    link="https://id.wikipedia.org/wiki/Daftar_miliarder_Forbes"
    data = scraper.Scraper(link)
    
    # transform
    df=transform.Transform(data)
    
    #load
    load.Load(df, ' dwiasana_orang_terkaya_forbes')
