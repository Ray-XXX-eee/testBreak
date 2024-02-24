import os
from py_sel import create_python_selenium_project
from j_sel import create_java_selenium_project
from js_sel import create_js_webdriverio_project


def main():
    # Get user input for the project type
    project_type = input("What type of project do you want to create? ")

    # Specify the directory where the project will be created
    project_directory = (
        "C:\\Users\\Rayha\\Desktop\\Projects\\playground\\coding-instruct-model\\op"
    )

    # Execute the project creation functions based on the project type
    if project_type.lower() == "python":
        create_python_selenium_project("\\op\\python\\py_sel+")
    elif project_type.lower() == "java":
        create_java_selenium_project(project_directory)
    elif project_type.lower() == "javascript":
        create_js_webdriverio_project(project_directory)
    else:
        print("Unsupported project type. Please choose Python, Java, or JavaScript.")


if __name__ == "__main__":
    main()
