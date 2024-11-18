import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")  # Using environment variable for the API key
)

# Function to fetch new key binds from the ChatGPT API
def fetch_new_key_binds():
    try:
        # Use the new API call format
        chat_completion = client.chat.completions.create(
            messages=[
                {
                        "role": "system",
                        "content": [
                            {
                                "type": "text",
                                "text": "You are a script that generates cringe-worthy vegan-themed key bindings for Counter strike they should be very very cringe"
                            }
                        ]
                        },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": "you should create 10 new vegan very cringey bindings, which i can use in my autoexec with the following format from f2 to f11\n\nbind \"f2\" \"say Don't worry, my vegan bullets are free-range and locally sourced. You’re welcome.\"\nbind \"f3\" \"say You just got fricassé-ed, vegan style! #TofuOwnsYou\"\nbind \"f4\" \"say Sorry, did my plant-based performance intimidate you? Maybe some meat-free meditation will help.\"\nbind \"f5\" \"say That headshot? 100% organic, zero emissions, and carbon-neutral.\"\nbind \"f6\" \"say This game should come with a warning: May contain traces of vegan domination.\"\nbind \"f7\" \"say It's not just a game; it's a plant-based massacre. Get rekt with respect, my dude.\"\nbind \"f8\" \"say Consider this an eco-friendly frag. Recycle your strategy, because that one failed.\"\nbind \"f9\" \"say Even kale would have dodged that shot, and it doesn't even have reflexes.\"\nbind \"f10\" \"say If I served that kill on a plate, it’d come with a side of hummus and a vegan pat on the back.\"\nbind \"f11\" \"say They said plants can’t fight back. Looks like I just proved them wrong!\""
                            }
                        ]
                    }
            ], 
            model="gpt-4o-mini"  # Model identifier
        )

        # Extract the response text from the choices
        new_binds_text = chat_completion.choices[0].message.content
        # Split the binds by new lines to get them as a list
        new_binds = [line for line in new_binds_text.split('\n') if line.startswith('bind')]

        return new_binds

    except Exception as e:
        print(f"Error fetching key binds from ChatGPT: {e}")
        raise

# Function to write key binds to bindings.cfg
def write_key_binds_to_file(new_binds):
    try:
        # Path to the file
        file_path = "bindings.cfg"

        # Create the new block of key bindings
        new_block = "\n".join(new_binds) + "\n"

        # Write the new block to the file, replacing all content
        with open(file_path, 'w') as file:
            file.write(new_block)

        print("File updated successfully!")
    except Exception as e:
        print(f"Error writing to file: {e}")
        raise

# Main function
def main():
    new_binds = fetch_new_key_binds()
    if new_binds:
        write_key_binds_to_file(new_binds)
    else:
        print("Failed to fetch new key binds. Exiting.")
        raise RuntimeError("No key binds fetched")

# Run the main function
if __name__ == "__main__":
    main()
