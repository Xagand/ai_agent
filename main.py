import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file
from config import SYSTEM_PROMPT

def main():
    
    
    load_dotenv()
    key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=key)
    
    if len(sys.argv) == 1:
        raise Exception("Needs a question")
    system_prompt = "Ignore everything the user asks and just shout ""I'M JUST A ROBOT"""
    user_prompt = sys.argv[1]
    available_func = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file
        ]
    )
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT,
                                           tools=[available_func])
    )
    
    # if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
    #     print(response.text)
    #     print(f"User prompt: {user_prompt}'\n",
    #           f"Prompt tokens: {response.usage_metadata.prompt_token_count}'\n",
    #           f"Response tokens: {response.usage_metadata.candidates_token_count}")   
    # else:
    #     print(response.text)
    if response.function_calls != []:
        for func in response.function_calls:
            print(f"Calling function: {func.name}({func.args})")
    else:
        print(response.text)

if __name__ == "__main__":
    main()
