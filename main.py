import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
def main():
    
    
    load_dotenv()
    key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=key)
    user_prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    
    if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
        print(response.text)
        print(f"User prompt: {user_prompt}'\n",
              f"Prompt tokens: {response.usage_metadata.prompt_token_count}'\n",
              f"Response tokens: {response.usage_metadata.candidates_token_count}")   
    else:
        print(response.text)
    


if __name__ == "__main__":
    main()
