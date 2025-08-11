import os
from config import LIMIT_PER_FILE

def get_file_content(working_directory:str, file_path:str) -> str:
    try:
        full_path = os.path.join(working_directory, file_path)
        abs_path = os.path.abspath(full_path)
        
        if working_directory not in abs_path:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        if os.path.isfile(abs_path) == False:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(abs_path, 'r') as f:
            content = f.read(LIMIT_PER_FILE)
            if len(content) < len(f.read()):
                content += f'\n[...File "{file_path}" truncated at 10000 characters]'
        return content    
    except Exception as e:
        return f"Error: {e}"