import os
import subprocess

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