from typing import Dict
from typing import Union
import pandas as pd
from fastapi import FastAPI, HTTPException
from modules.query_processor import process_query_jaccard
from modules.load_data import load_data_to_dataframe
from fastapi.middleware.cors import CORSMiddleware
from modules.Corpus import Corpus
from modules.retrieval_relevant_docs import retrieval_relevant_docs

app = FastAPI()
#df_bow=pd.read_csv('Back_of_words_version2.1.csv', index_col=0)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
"""@app.post("/query")
def pross_quer(data: Dict[str, str]):
    query= data.get("query")
    best_titles_jacard,best_titles_coss=process_query_jaccard(query,df_bow)
    #print("this is the query: ", query)
    #print("this is the results: ", best_titles_jacard)
    return {"best_titles_jaccard": best_titles_jacard,
            "best_titles_cos": best_titles_coss}"""
df=load_data_to_dataframe()
corpur=Corpus(df)

@app.get("/{query}")
async def read_item(query: str):
        corpur.jaccard(query=query)
        result=retrieval_relevant_docs(df,corpur.sorted_indices_jacc,corpur.jaccard_similarities)
        return result