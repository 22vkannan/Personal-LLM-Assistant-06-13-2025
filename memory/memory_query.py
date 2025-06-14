def retrieve_memory(query):
    vec = model.encode([query])[0]
    return collection.query(query_embeddings=[vec], n_results=3)['documents']
