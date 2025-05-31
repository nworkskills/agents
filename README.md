# Agents: Chat-Based and Agentic AI Applications

This repository demonstrates the implementation of chat-based and agentic AI applications using LangChain, OpenAI's GPT-4o-mini, FastAPI, and Flask. It includes four Python scripts showcasing different approaches to building conversational and task-oriented AI systems. The project is designed to be a learning resource for developers, students, and businesses interested in modern AI development.

## Features
- **Agentic AI**: A LangChain-based agent with tool integration for tasks like mathematical calculations.
- **Chat APIs**: Two Flask-based APIs for direct chat interactions using LangChain and OpenAI's native API.
- **Web Integration**: A FastAPI endpoint to expose the agent as a scalable web service.
- **Open-Source**: Publicly available for exploration, modification, and contribution.

## Prerequisites
- Python 3.10+
- OpenAI API key
- Basic knowledge of Python, web frameworks, and AI concepts

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/nworkskills/agents
   cd agents
   ```

2. **Set Up Environment Variables**
   - Create a `.env` file in the project root:
     ```bash
     echo "OPENAI_API_KEY=your_openai_key_here" > .env
     ```
   - Replace `your_openai_key_here` with your actual OpenAI API key.

3. **Install Dependencies**
   - Create and activate a virtual environment (recommended):
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```
   - Install requirements:
     ```bash
     pip install -r requirements.txt
     ```
   - Note: The repository does not include a `requirements.txt` file by default. Create one with the following content:
     ```
     langchain
     langchain-community
     openai
     fastapi
     uvicorn
     flask
     pydantic
     python-dotenv
     numexpr
     ```

4. **Run the Applications**
   - For `api.py` (FastAPI agent):
     ```bash
     uvicorn api:app --host 0.0.0.0 --port 8000
     ```
   - For `chatopenai_api_langchain.py` (Flask with LangChain):
     ```bash
     python chatopenai_api_langchain.py
     ```
   - For `openai_chatcompletion.py` (Flask with OpenAI):
     ```bash
     python openai_chatcompletion.py
     ```

## Usage Examples

1. **Agent API (`api.py`)**
   - Start the FastAPI server and test the agent:
     ```bash
     curl -X POST http://localhost:8000/ask -H "Content-Type: application/json" -d '{"prompt": "What is 5 + 3?"}'
     ```
   - Expected response:
     ```json
     {"response": "8"}
     ```

2. **LangChain Chat API (`chatopenai_api_langchain.py`)**
   - Start the Flask server and test the chat endpoint:
     ```bash
     curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"message": "What’s the capital of France?"}'
     ```
   - Expected response:
     ```json
     {"response": "The capital of France is Paris."}
     ```

3. **OpenAI Chat API (`openai_chatcompletion.py`)**
   - Start the Flask server and test the chat endpoint:
     ```bash
     curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"message": "Tell me a joke"}'
     ```
   - Expected response:
     ```json
     {"response": "Why did the scarecrow become a motivational speaker? Because he was outstanding in his field!"}
     ```

## File Structure
```
agents/
├── agent.py                     # LangChain agent with tool integration
├── api.py                       # FastAPI server to expose the agent
├── chatopenai_api_langchain.py  # Flask API using LangChain for chat
├── openai_chatcompletion.py     # Flask API using OpenAI's ChatCompletion
├── .env                         # Environment file for API keys (create manually)
└── README.md                    # Project documentation
```

## File Descriptions

### `agent.py`
- **Purpose**: Implements a LangChain agent that uses GPT-4o-mini and a math tool to process user prompts.
- **Key Imports**:
  - `langchain.chat_models.ChatOpenAI`: Initializes the GPT-4o-mini model.
  - `langchain.agents.initialize_agent, load_tools`: Sets up the agent and loads tools like `llm-math`.
  - `langchain.agents.agent_types.AgentType`: Defines the agent type (`ZERO_SHOT_REACT_DESCRIPTION`).
  - `os`: Manages the OpenAI API key.
- **Execution**: Initializes the LLM, loads the math tool, and creates an agent that processes prompts via the `run_agent` function.
- **Learning Outcomes**: Understand LangChain agent setup, tool integration, and LLM configuration.
- **Benefits**: Provides a foundation for building task-specific agents, useful for automation or educational purposes.

### `api.py`
- **Purpose**: Exposes the agent from `agent.py` as a FastAPI web endpoint for scalable access.
- **Key Imports**:
  - `fastapi.FastAPI`: Creates the web server.
  - `pydantic.BaseModel`: Validates incoming JSON data.
  - `agent.run_agent`: Uses the agent’s logic.
  - `uvicorn`: Runs the FastAPI server.
- **Execution**: Defines a `/ask` POST endpoint that accepts a prompt, processes it with the agent, and returns the response. Runs on port 8000.
- **Learning Outcomes**: Learn to integrate AI agents with FastAPI and handle HTTP requests.
- **Benefits**: Enables deployment of AI services as APIs, ideal for production or prototyping.

### `chatopenai_api_langchain.py`
- **Purpose**: Implements a Flask-based chat API using LangChain’s `ChatOpenAI` for conversational responses.
- **Key Imports**:
  - `flask.Flask, request, jsonify`: Builds the web server and handles HTTP requests.
  - `langchain_community.chat_models.ChatOpenAI`: Interfaces with GPT-4o-mini.
  - `langchain.schema.HumanMessage`: Formats user input for the LLM.
  - `os`: Manages the API key.
- **Execution**: Defines a `/chat` POST endpoint that processes user messages and returns LLM responses. Runs on port 5000.
- **Learning Outcomes**: Learn to build chat APIs with Flask and LangChain, focusing on conversational AI.
- **Benefits**: Quick prototyping of chatbots, useful for learning or customer-facing applications.

### `openai_chatcompletion.py`
- **Purpose**: Implements a Flask-based chat API using OpenAI’s native ChatCompletion API for direct LLM interaction.
- **Key Imports**:
  - `flask.Flask, request, jsonify`: Manages the web server and HTTP responses.
  - `openai`: Accesses OpenAI’s ChatCompletion API.
  - `os`: Handles the API key.
- **Execution**: Defines a `/chat` POST endpoint that sends user messages to OpenAI’s API and returns responses. Runs on port 5000.
- **Learning Outcomes**: Understand direct LLM API usage without frameworks like LangChain.
- **Benefits**: Offers a lightweight approach to chat applications, ideal for simple integrations.

## What You’ll Learn
- **Agentic AI**: How to build and configure a LangChain agent with tools for task-specific processing.
- **Chat APIs**: Techniques for creating conversational APIs using Flask and FastAPI.
- **LLM Integration**: Using OpenAI’s GPT-4o-mini with LangChain and directly via the OpenAI API.
- **Web Development**: Building and deploying web services with modern Python frameworks.
- **Extensibility**: Structuring projects for easy modification and scaling.

## Benefits
- **Developers**: Gain practical experience with LangChain, FastAPI, and Flask, enhancing skills in AI and web development.
- **Students**: Build a portfolio with real-world AI projects, aligning with trends in conversational and agentic systems.
- **Businesses**: Prototype chatbots or task-oriented agents for customer support, automation, or internal tools.
- **Open-Source Enthusiasts**: Contribute to a public project, learning collaborative development.

## How to Enhance
- **Add Tools**: Extend `agent.py` with tools like web search or database queries from LangChain’s ecosystem.
- **Improve APIs**: Add authentication, conversation history, or multiple endpoints to `api.py`, `chatopenai_api_langchain.py`, or `openai_chatcompletion.py`.
- **Integrate Front-Ends**: Connect the APIs to web or mobile interfaces using frameworks like React or Flutter.
- **Alternative LLMs**: Swap GPT-4o-mini for open-source models (e.g., via Hugging Face) to reduce costs.
- **Deployment**: Use Docker or cloud platforms (e.g., AWS, Heroku) for production-ready deployment.
- **Explore RAG**: Check out the related `rag-agent-gpt-langchain` project at [https://github.com/nworkskills/rag-agent-gpt-langchain](https://github.com/nworkskills/rag-agent-gpt-langchain) for advanced Retrieval-Augmented Generation features.

## Contributing
Contributions are welcome! Please:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit changes (`git commit -m "Add YourFeature"`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

Report issues or suggest features via the [Issues](https://github.com/nworkskills/agents/issues) tab.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. (Note: Create a `LICENSE` file in the repository with the MIT License text or your preferred license.)