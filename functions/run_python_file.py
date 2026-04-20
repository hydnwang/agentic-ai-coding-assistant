import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the python file with Python3 interpreter, accepts additional CLI args as an optional array",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to run, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="A optional array of strings to be used as CLI args for the Python file",
                items=types.Schema(
                    type=types.Type.STRING,
                ),
            ),
        },
    ),
)

def run_python_file(working_directory, file_path, args=None):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

    if not (os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: "{file_path}" does not exists or is not a regular file'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'
    
    command = ["python", abs_file_path]
    if args:
        command.extend(args)
        # for arg in args:
        #     command.append(arg)
    try:
        res = subprocess.run(command, cwd=abs_working_dir, capture_output=True, text=True, timeout=30)
        if res.returncode != 0:
            return f'Process exited with code {res.returncode}'
        if not res.stdout and not res.stderr:
            return 'No output produced'
        
        output = f'STDOUT: {res.stdout}; \nSTDERR: {res.stderr}'
        return output
    except Exception as e:
        return f'Error: executing Python file: {e}'
    
    """
    1. Set the working directory properly.
    2. Capture output (i.e., stdout and stderr).
    3. Decode the output to strings, rather than bytes; this is done by setting text=True.
    4. Set a timeout of 30 seconds to prevent infinite execution.
    """

# if __name__ == "__main__":
#     run_python_file("calculator", "main.py", ["3 + 5"])