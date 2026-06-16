

def log_problem_to_terminal(problem):
    """
    Logs the details of the selected problem to the terminal.

    Args:
        problem (dict): A dictionary containing the details of the selected problem.
    """
    print("Problem of the Day:")
    print('=' * 20)
    print(f"Today's Problem: {problem['title']}")
    print(f"Topics: {', '.join(problem['topics'])}")
    print(f"Difficulty: {problem['difficulty']}")
    print(f"Link: {problem['url']}")
    print('=' * 20)