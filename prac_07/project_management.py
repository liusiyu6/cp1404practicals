"""
Time estimate: 2.5 hours
Actual time: 4 hours
"""

from project import Project
import datetime

DEFAULT_FILENAME = "projects.txt"


def main():
    """Main menu-driven program for managing projects."""
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from {DEFAULT_FILENAME}")

    MENU = ("\n(L)oad projects\n(S)ave projects\n(D)isplay projects\n"
            "(F)ilter projects by date\n(A)dd new project\n(U)pdate project\n(Q)uit")

    choice = input(MENU + "\n>>> ").lower()
    while choice != "q":
        if choice == "l":
            filename = input("Filename to load from: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid choice.")
        choice = input(MENU + "\n>>> ").lower()

    save_choice = input(f"Would you like to save to {DEFAULT_FILENAME}? (Y/n): ").lower()
    if save_choice in ("", "y"):
        save_projects(DEFAULT_FILENAME, projects)
        print("Projects saved.")
    print("Thank you for using Pythonic Project Management.")


def load_projects(filename):
    """Load projects from a tab-delimited file."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # skip header line
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """Save all projects to a tab-delimited file."""
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                  f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """Display incomplete and complete projects separately, sorted by priority."""
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]
    incomplete.sort()
    complete.sort()

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects:")
    for project in complete:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Ask for a date and display projects starting after that date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered = [p for p in projects if p.start_date > filter_date]
    filtered.sort(key=lambda p: p.start_date)
    for project in filtered:
        print(f"  {project}")


def add_new_project(projects):
    """Add a new project to the list."""
    print("Let's add a new project:")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion))


def update_project(projects):
    """Update an existing project's completion or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(f"Selected project: {project}")
    new_completion = input("New percentage: ")
    new_priority = input("New priority: ")
    project.update(new_completion, new_priority)
    print("Project updated.")


if __name__ == "__main__":
    main()
