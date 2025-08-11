import os
from google import genai
from google.genai import types

def write_file(working_directory:str, file_path:str, content:str) -> str:
    
    try:
        full_path = os.path.join(working_directory, file_path)
        abs_path = os.path.abspath(full_path)
        print(abs_path)
        if working_directory not in abs_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.exists(abs_path) == False:
            os.makedirs(abs_path)
            print(os.path.exists(abs_path))
            with open(abs_path, "w") as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        else:
            with open(abs_path, "w") as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
          
    except Exception as e:
        return f"Error: {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwriting file by namy of file_path. If file not exsiting - create it and writing content",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File to ovewright or create new file with that name."),
            "content":  types.Schema(
                type=types.Type.STRING,
                description="Content that supposed to be use to ovewright the file"
           
            ),
        },
    ),
)        