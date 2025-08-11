import os
from google import genai
from google.genai import types

def get_files_info(working_directory:str, directory=".") -> str:
    try:
        full_path = os.path.join(working_directory, directory)
        abs_path = os.path.abspath(full_path)
        if directory == ".":
            result = f"Result for current directory:"
            
        else:
            result = f"Result for '{directory}' directory:"
            
        if working_directory not in abs_path:
            return f'{result}\nError: Cannot list "{directory}" as it is outside the permitted working directory'
        if os.path.isfile(abs_path) == True:
            return f'{result}\nError: "{directory}" is not a directory'
        
        content_lst = []

        for file_name in os.listdir(path=abs_path):
            file_path = abs_path + f"/{file_name}"
            content_lst.append(f"- {file_name}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}")
        content = "\n".join(content_lst)
        
        return f"{result}\n{content}"       
    except Exception as e:
        return f"Error: {e}"
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)    
# def main():
#      print(get_files_info("calculator", "."))
    
# if __name__ == "__main__":
#     main()    