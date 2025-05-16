from langchain_community.document_loaders import PyPDFium2Loader

loader = PyPDFium2Loader("sample.pdf")
pages = loader.load()

print(pages[0].page_content)
