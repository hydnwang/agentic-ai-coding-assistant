import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="""
        Overwrites an existing file 
        or writes a new file if nonexistent (and creates necessary directories safely), 
        constrained to the working directory
    """,
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The contents to the file to write as a string",
            )
        },
    ),
)

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

    if not (os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir):
        return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(abs_file_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    abs_file_dir = os.path.dirname(abs_file_path)
    try:
        os.makedirs(abs_file_dir, exist_ok=True)
        
        with open(abs_file_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f'Error: {e}'
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'