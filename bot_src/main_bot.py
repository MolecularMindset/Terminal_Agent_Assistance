## imports 
import os 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain.tools import  tool
from langchain_community.tools import ShellTool
from langchain_experimental.utilities import PythonREPL
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor,create_react_agent,Tool # To load simple ReAct agent. Reason an act
from langchain import hub
import warnings
warnings. filterwarnings("ignore")
load_dotenv()

## Define model choose between OpenAI and Groq
model = 'OpenAI' ## or OpenAI

if model == 'OpenAI':
    # Load API KEYs
    #Defien OPENAI API
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    ## Load OpenAI chatbot
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.1)

elif model == 'Groq':
    ## Load Groq API key
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    ## Load Groq chatbot
    llm = ChatGroq(temperature=0.1, model_name="mixtral-8x7b-32768") #gemma-7b-it mixtral-8x7b-32768 or llama2-70b-4096

else:
    print(f'Model name ({model}) is not currently available.')


#### Define Tools ###
## Define custom tool using the function to get chatbot response
@tool
def chatbot_response(input):
    """Use Chatbot to answer questions that do not require any tools. Do not perform any action if this tool is used."""
    response = llm.invoke(input)
    return response.content

## Define other tools
## Shell tool
shell_tool = ShellTool()
python_repl = PythonREPL()

# You can create the tool to pass to an agent
repl_tool = Tool(
    name="python_repl",
    description="A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`.",
    func=python_repl.run,
)

# Define list of tools the LLM is going to use 
tools_list = [chatbot_response,shell_tool,repl_tool]

# Get the template prompt to use - you can modify this!
prompt = hub.pull("hwchase17/react")

## Construct the ReAct agent by defining the llm, tools and prompt template
shell_Agent = create_react_agent(llm=llm,tools=tools_list,prompt=prompt)

# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=shell_Agent, tools=tools_list, verbose=False)


# Define function to get Assistant response
def assistant_agent_response(input):

    # Run executor to get response 
    response = agent_executor.invoke({"input":str(input)})
    return response['output']