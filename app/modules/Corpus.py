from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import jaccard_score
from sklearn.metrics.pairwise import cosine_distances
import numpy as np
import time

class Corpus:
    def __init__(self, data_frame):
        self.count_vectorizer=CountVectorizer(binary=True)
        self.tfidf_vectorizer = TfidfVectorizer()
        self.df = data_frame
        self.bag_of_words_matrix = self.create_bag_of_words()
        self.tfidf_matrix = self.create_tf_idf()                
        self.best_titles_jaccard=None
        self.best_titles_cosine=None
        self.sorted_indices_jacc=None
        self.sorted_indices_cos=None
        self.jaccard_similarities=None
        self.cosine_distances=None
        
        
    def calcular_similitud_jaccard(self, query, count_vectorizer):
        # Transformar la consulta a Bag of Words (BoW)
        query_bow = count_vectorizer.transform([query])
        
        # Calcular similitud Jaccard para cada documento en bag_of_words_matrix
        jaccard_similarities = []
        for idx in range(self.bag_of_words_matrix.shape[0]):
            similarity = jaccard_score(
                self.bag_of_words_matrix[idx].toarray()[0],
                query_bow.toarray()[0]
            )
            self.jaccard_similarities.append(similarity)
        
        # Obtener índices ordenados por similitud descendente
        sorted_indices = np.argsort(jaccard_similarities)[::-1]
        
    def create_bag_of_words(self):
        bow_matrix = self.count_vectorizer.fit_transform(self.df['stemmed_text'])
        bow_feature_names = self.count_vectorizer.get_feature_names_out()
        return bow_matrix

    def create_tf_idf(self):
        tfidf_matrix = self.tfidf_vectorizer.fit_transform(self.df['stemmed_text']) 
        tfidf_feature_names = self.tfidf_vectorizer.get_feature_names_out()
        return tfidf_matrix
    
    def jaccard(self,query):
        print("procesando jaccard.....")
        start=time.time()
        query_bow = self.count_vectorizer.transform([query])
        jaccard_similarities = []
        self.jaccard_similarities=[]
        for idx in range(self.bag_of_words_matrix.shape[0]):
            similarity = jaccard_score(
                self.bag_of_words_matrix[idx].toarray()[0],
                query_bow.toarray()[0]
            )
            jaccard_similarities.append(similarity)
        
        sorted_indices = np.argsort(jaccard_similarities)[::-1]
        self.best_titles_jaccard=[]
        self.sorted_indices_jacc=sorted_indices
        self.jaccard_similarities=jaccard_similarities
        for idx in sorted_indices:
            if(jaccard_similarities[idx]>0.0):
                filename=self.df['filename'].iloc[idx]
                self.best_titles_jaccard.append(filename)
            else:
                break
        end=time.time()
        print("Finalizo jaccard, Time: ",end-start)
        
            
    def cosine(self,query):
        print("procesando cosine.....")
        start=time.time()
        query_tdid_vector = self.tfidf_vectorizer.transform([query])
        print(query_tdid_vector)
        cosine_distances = []
        for idx in range(self.tfidf_matrix.shape[0]):
            a=self.tfidf_matrix[idx].toarray().squeeze()
            b=query_tdid_vector.toarray().squeeze()
            if np.linalg.norm(a)*np.linalg.norm(b)>0.0:                
                cos_distantce=np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))
            else:
                cos_distantce=0.0
            cosine_distances.append(cos_distantce)
        
        sorted_indices2 = np.argsort(cosine_distances)[::-1]
        self.best_titles_cosine=[]
        self.sorted_indices_cos=sorted_indices2
        self.cosine_distances=cosine_distances
        for idx in sorted_indices2:
            if(cosine_distances[idx]>0.0):
                filename=self.df['filename'].iloc[idx]
                self.best_titles_cosine.append(filename)
            else:
                break
        end=time.time()
        print("finalizo cosine Time: ",end-start)
        
        
    