#to read the pdf and return multiple chunks or paragraphs technically

from pymupdf import open 
import re #regex expressions
from typing import List
from pathlib import Path


#function for paragraph extraction 

def extract_paragraphs(pdf_path:str|Path)-> List[str]:
    "this function basically takes the path of the pdf as an input and then gives output in the form of an array of paragraphs"

    doc=open(pdf_path)
    paragraphs=[] #final array of paragraphs extracted from the pdf

    for page in doc:
        #getting blocks from the pdf
        blocks=page.get_text("blocks")

        blocks=sorted(blocks,key=lambda b:(b[1],b[0]))
    

               #  blocks=[
                #0
                #1
                #2  
                #3
                #"text"    #hence block[4]
                #]  '''

        for block in blocks:
            text=block[4]


            #replace line breaks inside a paragraph with spaces , we can do this by a regex expression

            text=re.sub(r"\r+"," ",text).strip()

            if text:
                paragraphs.append(text) #new paragraph is appended to the paragraph , to provide us a list of paragraph arrays 



    return paragraphs

if __name__ == "__main__":
    pdf_path = Path(__file__).resolve().parent.parent / "pdfs" / "Penguins_ACL.pdf"
    print(extract_paragraphs(pdf_path))







