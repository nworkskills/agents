from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, load_tools
from langchain.agents.agent_types import AgentType
import os

os.environ["OPENAI_API_KEY"] = "your_openai_key_here"


llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
tools = load_tools(["llm-math"], llm=llm)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def run_agent(prompt):
    return agent.run(prompt)