from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import MathpixPDFLoader
from langchain_community.document_loaders.csv_loader import CSVLoader

"""load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')"""

class document_loaders:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_pdf_using_pypdf(self):
        try:
            loader = PyPDFLoader(self.file_path)
            pages = loader.load()
            return  pages
        
        except Exception as e:
            print(f"Error: {e}")    
    
    def load_pdf_using_pymupdf(self):
        try:
            loader = PyMuPDFLoader(self.file_path)
            data = loader.load()
            return data
        
        except Exception as e:
            print(f"Error: {e}")
    def load_pdf_using_unstructured(self):
        try:
            loader=UnstructuredPDFLoader(self.file_path)
            data=loader.load()
            return data
        except Exception as e:
            print(f"Error: {e}")

    def load_pdf_using_mathpix(self):
        try:
            loader=MathpixPDFLoader(self.file_path)
            data=loader.load()
            return data
        except Exception as e:
            print(f"Error: {e}")
    def load_csv(self):
        try:
            loader=CSVLoader(file_path=self.file_path)
            data=loader.load()
            return data
        except Exception as e:
            print(f"Eroor : {e}")



dl = document_loaders(r"D:\NLP_Mentorship\Notebooks\documents\sensors-22-08281-v3.pdf")
#d2=document_loaders(pdf_url)
pypdf_results = dl.load_pdf_using_pypdf()
pymupdf_results = dl.load_pdf_using_pymupdf()
unstructured_result=dl.load_pdf_using_unstructured()
mathpix_result=dl.load_pdf_using_mathpix()
CSVLoader_result=dl.load_csv()
print(CSVLoader_result)
print(pypdf_results)
print(pymupdf_results)

