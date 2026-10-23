import tools as tl
from prompts import system_agent_prompt
from langchain_groq import ChatGroq
from tools import collecting_info #first tool we have created
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain.messages import HumanMessage  #take a human message 
from objects import Answer

llm=ChatGroq(model="openai/gpt-oss-120b",temperature=0)

agent=create_agent(
    model=llm,
    tools=[collecting_info],
    system_prompt=system_agent_prompt,
    response_format=ToolStrategy(Answer)
)


def ask(question)->dict:
    """ Answer the user's question about the pdf"""
    tl.last_retrieved_context=[]

    result=agent.invoke(
        {"messages":[HumanMessage(content=question)]}
    )

    structured_resposne=result["structured_response"]


    return {
        "answer":structured_resposne.answer,
        "context":structured_resposne.context
    }


print(ask("what is the diet of penguins"))






