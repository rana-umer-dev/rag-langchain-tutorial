
# Load Data form Research Paper
from langchain_community.document_loaders import ArxivLoader

loader = ArxivLoader(query="2103.00020", load_max_docs=1)
docs = loader.load()

print(docs[0].page_content[:500])  # prints abstract or summary
