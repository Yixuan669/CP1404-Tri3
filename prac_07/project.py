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