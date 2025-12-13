import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)
    abs_working = os.path.abspath(working_directory)
    abs_target = os.path.abspath(full_path)

    if not (abs_target == abs_working or abs_target.startswith(abs_working + os.sep)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_target):
        return f'Error: File "{file_path}" not found.'

    if not abs_target.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        cmd = ["python", file_path] + args
        completed = subprocess.run(cmd, cwd=working_directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30, text=True)
        out = completed.stdout or ""
        err = completed.stderr or ""
        if (out == "" and err == "") and (completed.returncode == 0):
            return "No output produced"
        else:
            if completed.returncode != 0:
                return f"STDOUT: {out}\nSTDERR: {err}\nProcess exited with code {completed.returncode}"
            return f"STDOUT: {out}\nSTDERR: {err}"
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute a Python file in the working directory with optional command-line arguments.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="Optional list of string arguments to pass to the Python file.",
            ),
        },
    ),
)
