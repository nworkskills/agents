from flask import Flask, request, jsonify
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os

app = Flask(__name__)

# Set your OpenAI API key here
os.environ["OPENAI_API_KEY"] = "your-api-key-here"  # Replace with your real API key

# Initialize ChatOpenAI instance (use gpt-3.5-turbo or gpt-4 if you have access)
chat = ChatOpenAI(model="gpt-4o-mini")

@app.route("/chat", methods=["POST"])
def chat_api():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    try:
        response = chat([HumanMessage(content=user_input)])
        return jsonify({"response": response.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

'''
curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d "{\"message\": \"What's the capital of France?\"}"
'''