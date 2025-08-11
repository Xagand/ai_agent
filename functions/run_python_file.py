import os
import subprocess
from google import genai
from google.genai import types


def run_python_file(working_directory:str, file_path:str, args=[]) :
    try:
        full_path = os.path.join(working_directory, file_path)
        abs_path = os.path.abspath(full_path)
        
        if working_directory not in abs_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if os.path.exists(abs_path) == False:
            return f'Error: File "{file_path}" not found.'
        if abs_path.endswith('py') == False:
            return f'Error: "{file_path}" is not a Python file.'
        
        process = ["python3", abs_path]
        if args != []:
            process += args
            
        completed_process = subprocess.run(process,
                                        timeout=30,
                                        capture_output=True,
                                        text=True)
        
        result = f"""STDOUT: {completed_process.stdout}
STDERR: {completed_process.stderr}"""
        
        if completed_process.returncode != 0:
            result += f"\nProcess exited with code {completed_process.returncode}"
        print(result)   
        return result
    except Exception as e:
        return f"Error: executing Python file:{e}"    

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Running any python file. Timeout in 30 seconds.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Python file to run"),
            "args":  types.Schema(
                type=types.Type.STRING,
                description="List of additional args if required for running programm"
           
            ),
        },
    ),
)            