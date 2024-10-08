#!/usr/bin/python3
"""
create.py

Used with command line to create a new project in subdirectory
"""
import os
import sys
import hashlib
import datetime


def create_project(project_name: str) -> str:
    """
    Create a new project in subdirectory

    Parameter
    ---------
    project_name: str
        Name of the project

    Returns
    -------
    str
        path to the project directory
    """
    # folder is named as: $BASE_DIR/$(YYMMDDXX)-$(project_name)
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # replace all non-alphanumeric characters with underscore
    project_name = "".join([c if c.isalnum() else "_" for c in project_name])
    date_str = datetime.datetime.now().strftime("%y%m%d")
    random_str = hashlib.md5(project_name.encode()).hexdigest()[:2]
    project_dir = os.path.join(base_dir, f"{date_str}{random_str}-{project_name}")
    print(f"Creating project in {project_dir}")
    os.mkdir(project_dir)
    return project_dir


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 create.py <project_name>")
        sys.exit(1)
    project_dir = create_project(sys.argv[1])
    print(f"Project created in {project_dir}")
