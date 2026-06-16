import json

def fetch_json_data(file_path):
    """
    Fetches JSON data from a specified file path.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        list: A list of dictionaries containing the JSON data.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file at {file_path} is not a valid JSON file.")
        return []
    
