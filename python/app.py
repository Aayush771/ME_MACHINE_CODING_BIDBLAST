from sys import argv
import traceback
from src.repositories import GreetingRepository
from src.services import GreetingService

# Initialize repositories
greetingRepository = GreetingRepository()

# Initialize services
greetingService = GreetingService(greetingRepository)

def main():

    # Test your code by ading commands in sample_input/sample_input_one.txt
    # Run run.sh script using "bash run.sh" in your terminal.
    if len(argv) == 2:
        inputFile = argv[1].split("=")[1]
        try:
            with open(inputFile, 'r') as file:
                lines = file.readlines()
                # Execute the commands
                run(lines)
        except FileNotFoundError:
            print(f"The file '{inputFile}' does not exist.")
        return
        
    # OR
    # Test your code by ading commands in this list
    inplace_commands = [
    "CREATE_GREETING,Hello World!",
    "CREATE_GREETING,Bye World!",
    "LIST_GREETING",
    "GET_GREETING,1"
    ]

    run(inplace_commands)


def run(commands):
    for line in commands:
        if line is None:
            break
        tokens = line.split(",")

        try:
            # Execute Services
            if tokens[0] == "CREATE_GREETING":
                create_greeting(tokens)
            elif tokens[0] == "LIST_GREETING":
                list_greeting(tokens)
            elif tokens[0] == "GET_GREETING":
                get_greeting(tokens)
            # Add more if statements below to support other commands
            else:
                raise Exception("Invalid Command")
        except Exception as e:
            print(e.__class__, '-', e)
            traceback.print_exc()

# CREATE_GREETING
def create_greeting(tokens):
    message = tokens[1]
    g = greetingService.create(message)
    print(g)

# LIST_GREETING
def list_greeting(tokens):
    gList = greetingService.getAllGreetings()
    print(gList)

# GET_GREETING
def get_greeting(tokens):
    id = int(tokens[1])
    g = greetingService.getGreeting(id)
    print(g)
      
if __name__ == "__main__":
    main()