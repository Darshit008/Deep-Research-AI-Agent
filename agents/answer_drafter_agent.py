# # agents/answer_drafter_agent.py

# import google.generativeai as genai

# # Configure Gemini with your API key


# agents/answer_drafter_agent.py

# agents/answer_drafter_agent.py

from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load .env file
load_dotenv()

# Now get the GEMINI_API_KEY from the environment variable correctly
genai.configure(api_key=os.environ["GEMINI_API_KEY"])  # Ensure GEMINI_API_KEY is the key in .env

def draft_answer(data, query):
    # Extract actual content from list of dictionaries
    content_list = [item["content"] if isinstance(item, dict) and "content" in item else str(item) for item in data]
    combined_content = "\n".join(content_list)

    prompt = f"""Using the following research data, answer the query: {query}

    Research Data:
    {combined_content}

    Answer:"""

    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

    response = model.generate_content(prompt)
    
    return response.text


