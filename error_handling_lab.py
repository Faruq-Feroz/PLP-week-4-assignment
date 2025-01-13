# error_handling_lab.py

def error_handling_lab():
    """
    Prompts the user for a filename and handles errors if it doesn’t exist or can’t be read.
    """
    filename = input("Enter the filename to check: ")
    try:
        with open(filename, 'r') as file:
            print("File opened successfully!")
            print("First 100 characters of the file:")
            print(file.read(100))  
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: You do not have permission to access this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    error_handling_lab()
