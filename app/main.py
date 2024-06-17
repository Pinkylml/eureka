from typing import Dict
from typing import Union
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .modules.load_data import load_data_to_dataframe
from .modules.Corpus import Corpus
from .modules.retrieval_relevant_docs import retrieval_relevant_docs
from .modules.evaluation import evaluate

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
all_files=df['filename'].tolist()
corpur=Corpus(df)

@app.get("/{query}")
async def read_item(query: str):
        corpur.jaccard(query=query)
        corpur.cosine(query=query)
        recall=evaluate(query,all_files,corpur.best_titles_jaccard)
        print("Recall jacc: ", recall)
        result=retrieval_relevant_docs(
            df,
            corpur.sorted_indices_jacc,
            corpur.jaccard_similarities,
            corpur.sorted_indices_cos,
            corpur.cosine_distances
            )
        
        del corpur.sorted_indices_jacc,corpur.jaccard_similarities,corpur.sorted_indices_cos,corpur.cosine_distances
        return result