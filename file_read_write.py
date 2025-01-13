# file_read_write.py

def file_read_write():
    """
    Reads a file and writes a modified version to a new file.
    """
    try:
        input_file = input("Enter the name of the file to read: ")
        with open(input_file, 'r') as file:
            data = file.read()

        modified_data = data.upper() 
        output_file = "modified_" + input_file
        with open(output_file, 'w') as file:
            file.write(modified_data)

        print(f"Modified content has been written to '{output_file}'.")
    except FileNotFoundError:
        print("The file does not exist. Please check the filename and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    file_read_write()
