from datetime import datetime

from ..fetchers.json_fetcher import fetch_json_data
from ..storage.history_repository import (
    get_history,
    add_history,
    clear_history,
    get_history_by_date,
)
from ..selectors.problem_selector import select_todays_problem
from ..delivery.terminal_output import log_problem_to_terminal
from ..delivery.file_delivery import write_problem_to_file, format_problem_for_file
from ..delivery.email_delivery import send_email

from ..config import GMAIL_RECEIVER_EMAIL as receiver


def get_daily_problems(file_path, output_file_path):
    """
    Retrieves daily problems from a specified JSON file.

    Args:
        file_path (str): The path to the JSON file containing daily problems.
    Returns:
        list: A list of dictionaries representing daily problems.
    """
    available_problems = fetch_json_data(file_path)
    attempted_problem = {entry["problem_id"] for entry in get_history()}

    # Checking whether a problem has already been shown today
    today = datetime.now().date()
    existing_problem = get_history_by_date(today)

    if existing_problem:
        selected_problem = next(
            (
                problem
                for problem in available_problems
                if problem["id"] == existing_problem[0]["problem_id"]
            ),
            None,
        )
        
        problem_body = format_problem_for_file(selected_problem)

        log_problem_to_terminal(selected_problem)
        write_problem_to_file(problem_body, output_file_path)
        send_email(
            recipient=receiver,
            subject="Today's Daily Problem",
            body=problem_body
        )
        
        return None

    # Filter out problems that have already been attempted
    unattempted_problems = [
        problem
        for problem in available_problems
        if problem["id"] not in attempted_problem
    ]

    # If all problems have been attempted, reset the history
    if not unattempted_problems:
        clear_history()
        unattempted_problems = available_problems

    selected_problem = select_todays_problem(unattempted_problems)

    # Record the selected problem in the history with the current date
    add_history(selected_problem["id"], datetime.now())
    
    problem_body = format_problem_for_file(selected_problem)

    log_problem_to_terminal(selected_problem)
    write_problem_to_file(problem_body, output_file_path)
    send_email(
        recipient=receiver,
        subject="Today's Daily Problem",
        body=problem_body
    )

    return None
