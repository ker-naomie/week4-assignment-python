def read_and_modify_file():
    try:
        # Ask the user for the input file name
        input_filename = input("Enter the filename to read: ")

        # Open the file in read mode
        with open(input_filename, 'r') as file:
            content = file.read()

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Ask the user for the output file name
        output_filename = input("Enter the filename to save the modified content: ")

        # Write the modified content to the new file
        with open(output_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"File has been modified and saved as {output_filename}")

    except FileNotFoundError:
        print("Error: The file you entered does not exist.")
    except IOError:
        print("Error: There was an issue reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()