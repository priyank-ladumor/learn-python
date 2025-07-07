
# import pyttsx3

# engine = pyttsx3.init()
# engine.say("Hello my name is priyank")
# engine.runAndWait()


# import pyjokes

# joke = pyjokes.get_joke()
# print(joke) 



# Import the os module (used for interacting with the operating system)
import os

# Define a function to list and print directory contents
def list_directory(path):
    try:
        # ✅ Get a list of all entries (files and directories) in the given path
        entries = os.listdir(path)

        # 🖨️ Print the directory contents
        print(f"Contents of '{path}':")
        for name in entries:
            print(name)

    # ⚠️ Handle case: Directory not found
    except FileNotFoundError:
        print(f"Error: Directory '{path}' does not exist.")

    # ⚠️ Handle case: Permission denied
    except PermissionError:
        print(f"Error: Permission denied for '{path}'.")

    # ⚠️ Handle any other OS-related error
    except OSError as e:
        print(f"Error accessing '{path}': {e}")

# Main execution starts here
if __name__ == "__main__":
    # 📥 Ask the user to input a directory path
    folder = input("Enter the directory path: ")

    # 🚀 Call the function to list directory contents
    list_directory(folder)

