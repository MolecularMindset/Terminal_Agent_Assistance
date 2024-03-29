import sys

## Import assisntant response function
from main_bot import assistant_agent_response


# Function to generate a response to user input
def generate_response(user_input):
    # Your logic for generating a response goes here
    model_response = assistant_agent_response(user_input)
    return model_response

if __name__ == "__main__":
    # Get user input from command line
    user_input = sys.argv[1]
    # Generate response
    response = generate_response(user_input)
    
    # Print the response
    print(response)


