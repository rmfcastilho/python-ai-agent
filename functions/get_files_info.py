import os

def get_files_info(working_directory, directory=None):
    # if directory is None:
    #     return "No directory provided."

    if not os.path.isdir(directory):
        return f"Error: '{directory}' is not a directory"

    abs_working = os.path.abspath(working_directory)
    abs_target = os.path.abspath(directory)

    if not abs_target.startswith(abs_working + os.sep):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    entries = []

    for entry in os.listdir(directory):
        full_path = os.path.join(directory, entry)
        file_size = os.path.getsize(full_path)
        is_dir = os.path.isdir(full_path)
        entries.append(f"- {entry}: file_size={file_size} bytes, is_dir={is_dir}")

    return "\n".join(entries)
