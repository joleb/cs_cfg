import openai
import os

# Set your OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to fetch new key binds from the ChatGPT API
def fetch_new_key_binds():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You are a script that generates cringe-worthy vegan-themed key bindings for CS:GO."
                },
                {
                    "role": "user",
                    "content": "Create 10 new vegan-themed key bindings for F2 to F11."
                }
            ]
        )

        # Extract the response text
        new_binds_text = response['choices'][0]['message']['content']
        # Split the binds by new lines to get them as a list
        new_binds = [line for line in new_binds_text.split('\n') if line.startswith('bind')]

        return new_binds

    except Exception as e:
        print(f"Error fetching key binds from ChatGPT: {e}")
        return []

# Function to write key binds to a file
def write_to_file(new_binds):
    try:
        # Path to the file
        file_path = "autoexec.cfg"

        # Write the key binds to the file
        with open(file_path, 'w') as file:
            file.write("// Updated Vegan Cringe Binds\n")
            file.writelines("\n".join(new_binds))
            file.write("\n")

        print("File updated successfully!")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Main function
def main():
    new_binds = fetch_new_key_binds()
    if new_binds:
        write_to_file(new_binds)
    else:
        print("Failed to fetch new key binds. Exiting.")

# Run the main function
if __name__ == "__main__":
    main()
