# Lab 1 - Reading Data from Different File Types

In Lab 1, I learned how to read and process data from various file formats using LangChain's document loaders. I explored how to extract text from `.txt` files using `TextLoader`, load PDF documents using `PyPDFLoader`, handle Markdown files with `UnstructuredMarkdownLoader`, and scrape content from web pages using `WebBaseLoader`. This lab helped me understand how to prepare different types of documents for further processing in AI applications.

## 📘 Lab: Loading arXiv Research Papers & Extracting Text

In this lab, we worked on loading research papers from arXiv and extracting their text content for further processing.

### ✅ What We Did:

1. **Loading Data from arXiv**
   - Used the **`ArxivLoader`** class from the **LangChain** library to directly load research papers from arXiv by specifying paper IDs or search queries.
   - This loader simplifies fetching metadata and PDF content from arXiv.

2. **PDF Text Extraction using `pypdfium2`**
   - Utilized the **`pypdfium2`** Python library to open and extract text from downloaded PDF files.
   - This helped in handling multi-page PDFs and preserving formatting where possible.

3. **Data Preparation**
   - After extraction, the raw text was cleaned and structured to be ready for text splitting or NLP tasks.

---

This lab demonstrated an end-to-end pipeline for fetching academic research content from arXiv and converting it into machine-readable text using Python libraries.

##  Lab 3: Text Splitting Techniques using LangChain

In this lab, we explored various text splitting techniques provided by the LangChain library to process long text documents into manageable chunks suitable for language model inputs.

### ✅ Topics Covered:

1. **Installing Required Libraries**  
   Installed LangChain and its dependencies  .

2. **Text Splitters**  
   Explored different types of text splitters in LangChain, such as:
   - CharacterTextSplitter
   - RecursiveCharacterTextSplitter
   - TokenTextSplitter
   - MarkdownHeaderTextSplitter
   - HTMLHeaderTextSplitter
   - PythonCodeTextSplitter

3. **Key Parameters**  
   Understood how `chunk_size` and `chunk_overlap` control the splitting behavior.

4. **Prepare the Document**  
   Downloaded and loaded a sample file (`companypolicies.txt`) for testing.

5. **Split by Character**  
   Split text using fixed-length character chunks.

6. **Recursively Split by Character**  
   Applied recursive splitting that respects natural language boundaries (sentences, words).

7. **Split Code**  
   Tested code-aware splitting using PythonCodeTextSplitter.

8. **Markdown Header Text Splitter**  
   Used headers in Markdown files to logically chunk content.

9. **Split by HTML**  
   Parsed and split HTML content based on tag structure.

---

This lab helped understand how to efficiently prepare and structure text for LLM-based applications using LangChain's flexible splitting utilities.
