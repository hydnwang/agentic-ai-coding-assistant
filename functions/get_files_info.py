import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{target_dir}" is not a directory'
    
    res = []
    for i in os.listdir(path=target_dir):
        file_abs = os.path.join(target_dir,i)
        file_size = os.path.getsize(file_abs)
        is_dir = os.path.isdir(file_abs)
        res.append(f"- {i + ":":<15} file_size={str(file_size) + ",":<10} is_dir={is_dir}")
    return "\n".join(res)


if __name__ == "__main__":
    res = get_files_info("calculator", ".")
    print("".join(res))