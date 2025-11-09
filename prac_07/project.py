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

def display_projects(projects: list[Project]) -> None:
    """Display complete and incomplete projects by format"""
    incomplete_projects = [p for p in projects if not p.is_complete()]
    complete_projects = [p for p in projects if p.is_complete()]

    incomplete_projects.sort(key=sort_by_priority_and_start)
    complete_projects.sort(key=sort_by_priority_and_start)

    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(f"  {project}")
    print("Completed projects: ")
    for project in complete_projects:
        print(f"  {project}")

def sort_by_priority_and_start(project: Project):
    """For sorting projects by priority"""
    return project.priority, project.start_date


def get_start_date(project: Project):
    """For sorting projects by date"""
    return project.start_date

def filter_projects_by_date(projects: list[Project]) -> None:
    """Filter projects by user input."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = parse_date(date_string)
    filtered = [p for p in projects if p.start_date >= filter_date]
    filtered.sort(key=get_start_date)
    for project in filtered:
        print(project)

def add_new_project(projects: list[Project]) -> None:
    """Add new projects to a file"""
    print("Let's add a new project")
    name = input("Name: ")
    date_string = input("Start date (dd/mm/yy): ")
    start_date = parse_date(date_string)
    priority = get_int("Priority: ")
    cost_text = input("Cost estimate: $")
    cost_estimate = float(cost_text)
    completion_percentage = get_int("Percent complete: ")
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)

def get_int(prompt: str) -> int:
    """Turn a string into an integer"""
    value_text = input(prompt)
    return int(value_text)

def update_project(projects: list[Project]) -> None:
    """Update single project percentage and priorities"""
    for index, project in enumerate(projects):
        print(f"{index} {project}")
    choice_text = input("Project choice: ")
    if not choice_text:
        return
    choice = int(choice_text)
    if choice < 0 or choice >= len(projects):
        return
    project = projects[choice]
    print(project)
    new_percentage_text = input("New Percentage: ")
    if new_percentage_text.strip():
        project.completion_percentage = int(new_percentage_text)
    new_priority_text = input("New Priority: ")
    if new_priority_text.strip():
        project.priority = int(new_priority_text)