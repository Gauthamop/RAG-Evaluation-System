from langchain_core.vectorstores import InMemoryVectorStore
from langchain_groq import ChatGroq



system_agent_prompt="""
you are a question-answering asssistant for a PDF

use the collection_info tool to retrieve information from the pdf 
before answering questions its content.

Base your answers only based on the retrieved information, if the retrieved infromation does not contain the answer, say that the PDF does not provide 
enough information to answer this question
"""


