from sentence_transformers import SentenceTransformer

_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text: str) -> list[float]:
    return _model.encode(text, convert_to_numpy=True).tolist()

if __name__ == "__main__":
    print(embed_text("Travel to Bali"))
