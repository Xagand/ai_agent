import os

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