import pandas as pd
result = {
    "best_titles_jacc": {},
    "best_titles_coss": {},
}

def retrieval_relevant_docs(df,sorted_indices,jaccard_sim,sorted_indices_cos, cosine_distances):
    print("Recuperando archivos")
    for idx in sorted_indices:
        if(jaccard_sim[idx]>0):
            filename=df['filename'].iloc[idx]
            texto = df['original_text'].iloc[idx]
            result["best_titles_jacc"][filename]=texto
        else:
            break
        
    for idx in sorted_indices_cos:
        if(cosine_distances[idx]>0):
            filename=df['filename'].iloc[idx]
            texto = df['original_text'].iloc[idx]
            result["best_titles_coss"][filename]=texto
        else:
            break
    return result