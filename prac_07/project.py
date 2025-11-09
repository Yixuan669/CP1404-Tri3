from datetime import datetime, date

FILENAME = "projects.txt"

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

class Project:
    """Create a class for this project"""
    def __init__(self, name: str, start_date: date, priority: int, cost_estimate: float, completion_percentage: int):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def is_complete(self) -> bool:
        """Determine if this project is complete"""
        return self.completion_percentage == 100

    def __str__(self) -> str:
        """Return a string representation of this project"""
        date_str = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {date_str}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

def main():
    """Create and run the main function"""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    choice = ""
    while choice != "Q":
        print(MENU)
        choice = input(">>> ").strip().upper()
        if choice == "L":
            filename = input("Filename to load projects from: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "S":
            filename = input("Filename to save projects to: ")
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        elif choice == "Q":
            # 跳出循环，下面统一处理退出
            break
        else:
            print("Invalid choice")

    ask_save_before_quit(FILENAME, projects)
    print("Thank you for using custom-built project management software.")

def load_projects(filename: str) -> list[Project]:
    """Load projects from a file"""
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        for line in in_file:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            name = parts[0]
            start_date = parse_date(parts[1])
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects

def parse_date(date_string: str) -> date:
    """Turn a date string into a date"""
    date_string = date_string.strip()
    try:
        return datetime.strptime(date_string, "%d/%m/%Y").date()
    except ValueError:
        return datetime.strptime(date_string, "%d/%m/%y").date()

def save_projects(filename: str, projects: list[Project]) -> None:
    """Save projects to a file"""
    with open(filename, "w", encoding="utf-8") as out_file:
        for project in projects:
            date_str = project.start_date.strftime("%d/%m/%Y")
            line = (f"{project.name}\t{date_str}\t{project.priority}\t"
                    f"{project.cost_estimate:.2f}\t"
                    f"{project.completion_percentage}")
            print(line, file=out_file)