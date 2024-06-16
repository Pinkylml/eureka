import pandas as pd
result_jacc={}
def retrieval_relevant_docs(df,sorted_indices,jaccard_sim):
    print("Recuperando archivos")
    for idx in sorted_indices:
        if(jaccard_sim[idx]>0):
            filename=df['filename'].iloc[idx]
            texto = df['stemmed_text'].iloc[idx]
            result_jacc[filename]=texto
        else:
            break
    return result_jacc