import sys

REQUIRED_PYTHON = "{{ cookiecutter.python_version }}"

def main():
    installed_python = str(sys.version_info.major) + '.' + str(sys.version_info.minor)
    if REQUIRED_PYTHON != installed_python:
        raise "This project requires Python {}. Found: Python {}".format(REQUIRED_PYTHON, installed_python)
    else:
        print(">>> Development environment passes all tests!")


if __name__ == '__main__':
    main()
