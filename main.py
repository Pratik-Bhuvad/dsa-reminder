from src.services.daily_problem_service import get_daily_problems
from src.database.schema import init_db

def main():
    init_db()
    
    file_path = 'data/problems.json'
    get_daily_problems(file_path)
    
            
if __name__ == "__main__":
    main()