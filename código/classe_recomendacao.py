import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class SistemaRecomendacao:
    def __init__(self, file_path):
        """
        Inicializa o sistema de recomendação.
        
        Args:
        - file_path (str): Caminho para o arquivo CSV com os dados.
        """
        self.data = pd.read_csv(file_path)
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(self.data['about_product'])
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)
        
    def recomendar(self, product_id, top_n=5):
        """
        Retorna os top_n produtos mais similares ao produto fornecido como uma lista de dicionários.

        Args:
        - product_id (str): ID do produto para o qual se deseja recomendações.
        - top_n (int): Número de recomendações a retornar.

        Returns:
        - List[Dict]: Lista de dicionários contendo `product_id`, `product_name`, `category` e `similarity_score`.
        """
        indices = self.data.index[self.data['product_id'] == product_id].tolist()
        if not indices:
            return []
        
        idx = indices[0]
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
        
        product_indices = [i[0] for i in sim_scores]
        similarity_scores = [i[1] for i in sim_scores]
        
        recommended = self.data.iloc[product_indices][['product_id', 'product_name', 'category']].copy()
        recommended['similarity_score'] = similarity_scores
        
        # Convertendo para uma lista de dicionários
        return recommended.to_dict(orient='records')
    
    def listar_produtos(self):
        """
        Retorna todos os produtos disponíveis como uma lista de tuplas (product_id, product_name).
        
        Returns:
        - List[Tuple[str, str]]: Lista de tuplas contendo `product_id` e `product_name`.
        """
        return list(self.data[['product_id', 'product_name']].drop_duplicates().itertuples(index=False, name=None))

