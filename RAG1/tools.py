#invoking tools for the agent

from indexing import vector_store
from langchain.tools import tool

last_retrieved_context=[]


@tool
def collecting_info(query:str)->str:
    """
    search the pdf which is the knowledge base for relevant information 
    for the user's question 
    """
    global last_retrieved_context
    docs=vector_store.similarity_search(query,k=3)
    #indexed 10 chunks --> give me the best 3 paragraphs that we believe will give the  best answer to respiond to the agent



    #basically to check if how our agent behaves with more information and less information 

    #save the Real retrieved chunks

    last_retrieved_context=[doc.page_content for doc in docs] #3 pargraphs as an array, 3 paragraphs with spaces between them 

    return "\n\n".join(last_retrieved_context)





