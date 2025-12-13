from functions.get_file_content import get_file_content

def main():
    print("Result for 'calculator/main.py' is:")
    print(get_file_content("calculator", "main.py"))

    print("Result for calculator/pkg/calculator.py is:")
    print(get_file_content("calculator", "pkg/calculator.py"))

    print("Result for 'calculator/bin/cat' is:")
    print(get_file_content("calculator", "/bin/cat"))

    print("Result for 'calculator/pkg/does_not_exist.py' is:")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    main()
