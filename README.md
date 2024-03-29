# **Terminal_Agent_Assistance**

Welcome to Terminal_Agent_Assistance, an innovative Large Language Model (LLM) chatbot framework designed to enhance your terminal experience. This project utilizes cutting-edge technologies from LangChain, OpenAI, and Groq to provide a seamless interface for file management, data analysis, and more. With Terminal_Agent_Assistance, users can interact with their terminal through natural language commands, making complex tasks simpler and more intuitive.

## **Features**

- **Advanced LLM Integration**: Harnessing the power of OpenAI's models for natural language understanding.

- **LangChain for Workflow Automation**: Utilizing LangChain to create complex workflows and automate tasks within the terminal.

- **Groq API Acceleration**: Leveraging Groq's hardware solutions for unparalleled performance and efficiency in processing tasks.

- **Comprehensive Tutorial**: Includes a detailed Jupyter notebook tutorial on building simple to advanced agents, showcasing the integration of these technologies.

<br>

## **Getting Started**

### **1. Prerequisites**

To get started with Terminal_Agent_Assistance, ensure you have Python and the following dependencies installed:

```pip install --upgrade --quiet  langchain langchain-openai langchain-experimental langchainhub python-dotenv langchain-groq```

### **2. Installation**

#### 2.1 Clone the Repository:
```git clone https://github.com/MolecularMindset/Terminal_Agent_Assistance.git```


#### 2.2 Navigate to the Directory:
```cd Terminal_Agent_Assistance```

#### 2.3 Add API keys to .env file:
- Create a copy of the .env_sample file and call it .env
- Copy your OpenAI and Groq API keys in the defined spaces


#### 2.4 Make the main script a executable
```chmod +x bot_src/launch_bot.sh```

#### 2.5 Add executable to PATH
- Open your shell profile file (.bashrc, .zshrc, etc.) in a text editor. For most users, this will be ~/.bashrc or ~/.zshrc.

- Add the following line at the end of the file, replacing /path/to with the actual path to the bot_src directory:

```export PATH=$PATH:/path/to/bot_src```

- Save the file and reload your shell configuration:

```source ~/.bashrc```

- Or replace .bashrc with your profile file

**Now, you can run launch_bot.sh from anywhere in the terminal.**

<br>
<br>

## Directory Structure 
```
Terminal_Agent_Assistance/
├── bot_src/
│   ├── launch_bot.sh         - Script to run the chatbot globally.
│   ├── bot_response.py       - Script to call response that the agent give
│   └── main_bot.py            - Langchain workflow for chat and agent using Groq and OpenAI
│
├── tutorial/
│   └── Tutorial_notebook.ipynb - Jupyter notebook tutorial for Terminal_Agent_Assistance components
│
├── .env_sample               - File to store enviorement variables sunch as API keys
├── .gitignore
│
└── README.md                 - Project documentation.
```

<br>


## Tutorial

Explore the tutorial/Tutorial_notebook.ipynb Jupyter notebook for a comprehensive guide on building both basic and advanced chatbots and agents. This tutorial emphasizes the integration of LangChain, OpenAI, and Groq technologies, providing a solid foundation for developing powerful terminal-based applications.

<br>

## Contributing

We welcome contributions to Terminal_Agent_Assistance! Feel free to submit pull requests, open issues, or suggest features to help us improve.

<br>

### License

This project is licensed under the MIT License - see the LICENSE file for more details.
