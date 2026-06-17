from src.services.daily_problem_service import get_daily_problems
from src.database.schema import init_db

from src.config import INPUT_FILE_PATH as file_path, OUTPUT_FILE_PATH as output_file_path

def main():
    init_db()
    get_daily_problems(file_path, output_file_path)
            
if __name__ == "__main__":
    main()