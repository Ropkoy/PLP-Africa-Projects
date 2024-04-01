def main():
    # Task 1: File Creation
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("2nd line with numbers: 12345\n")
            file.write("Another line here\n")
            print("File 'my_file.txt' created successfully and written with initial content.")
    except Exception as e:
        print("Error occurred while creating or writing to the file:", e)

    # Task 2: File Reading and Display
    try:
        with open("my_file.txt", "r") as file:
            file_contents = file.read()
            print("\nContents of 'my_file.txt':\n", file_contents)
    except FileNotFoundError:
        print("Error: File 'my_file.txt' not found.")
    except PermissionError:
        print("Error: Permission denied while reading the file.")
    except Exception as e:
        print("Error occurred while reading the file:", e)

    # Task 3: File Appending
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appended line 1\n")
            file.write("Line 2 appended\n")
            file.write("More appended content\n")
            print("\nAdditional content appended to 'my_file.txt' successfully.")
    except PermissionError:
        print("Error: Permission denied while appending to the file.")
    except Exception as e:
        print("Error occurred while appending to the file:", e)


if __name__ == "__main__":
    main()
