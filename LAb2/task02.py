#This loader uses the pypdfium2 library to extract text from PDF files. It can sometimes handle files better than other loaders like PyPDFLoader or PDFMinerLoader.
#Good for extracting text from scanned PDFs or images inside PDFs.


from langchain_community.document_loaders import PyPDFium2Loader

loader = PyPDFium2Loader("sample.pdf")
pages = loader.load()

print(pages[0].page_content)
