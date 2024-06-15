from typing import Dict
import pandas as pd
from fastapi import FastAPI, HTTPException
from modules.query_processor import process_query_jaccard

app = FastAPI()
df_bow=pd.read_csv('Back_of_words_version2.1.csv', index_col=0)

@app.post("/query")
def pross_quer(data: Dict[str, str]):
    query= data.get("query")
    best_titles_jacard,best_titles_coss=process_query_jaccard(query,df_bow)
    #print("this is the query: ", query)
    #print("this is the results: ", best_titles_jacard)
    return {"best_titles_jaccard": best_titles_jacard,
            "best_titles_cos": best_titles_coss}