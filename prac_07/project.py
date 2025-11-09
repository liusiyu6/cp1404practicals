"""
Time estimate: 1.5 hours
Actual time: 2.5 hours
"""
import datetime


class Project:
    """Represent a project with relevant details."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project instance."""
        self.name = name
        if isinstance(start_date, str):
            self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        else:
            self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return string representation of the project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Compare projects by priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if the project is complete."""
        return self.completion_percentage == 100

    def update(self, new_completion=None, new_priority=None):
        """Update completion percentage and/or priority."""
        if new_completion != "":
            self.completion_percentage = int(new_completion)
        if new_priority != "":
            self.priority = int(new_priority)
