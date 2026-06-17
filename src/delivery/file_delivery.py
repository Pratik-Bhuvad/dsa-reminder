

import os
from datetime import datetime

def format_problem_for_file(problem):
    """
    Formats the problem data into a string suitable for writing to a file.

    Args:
        problem (dict): The problem data to be formatted.
    Returns:
        str: A formatted string representing the problem data.
    """
    date = datetime.now().strftime("%d-%m-%Y")
    topics = problem.get("topics", "N/A")
    
    if isinstance(topics, list):
        topics = ", ".join(topics)
        
    return f"""Date: {date}

Title: {problem.get("title", "N/A")}

Topics: {topics}
Difficulty: {problem.get("difficulty", "N/A")}
    
Link: {problem.get("url", "N/A")}
===============================================

"""
    

def write_problem_to_file(problem, file_path):
    """
    Writes the problem data to a specified file.

    Args:
        problem (dict): The problem data to be written.
        file_path (str): The path to the file where the data will be written.
    """
    
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
    
    with open(file_path, 'a', encoding="utf-8") as file:
        file.write(problem)
            
                