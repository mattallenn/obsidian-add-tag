import os

def append_to_files(directory, content):
    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        # Check if the path is a file
        if os.path.isfile(filepath):
            # Open the file in append mode
            with open(filepath, 'a') as file:
                # Append content to the file
                file.write("\n")
                file.write(content)
                print(f"Appended to {filename}")
            # Close the file
            file.close()

# Get user input
directory_path = input("Enter the directory path: ")
content_to_append = input("Enter the content to append: ")

# Validate the directory path
if not os.path.exists(directory_path):
    print("Directory does not exist")
    exit()

# Validate the content
if not content_to_append:
    print("Content cannot be empty")
    exit()

# Call the function with the directory path and content
append_to_files(directory_path, content_to_append)
