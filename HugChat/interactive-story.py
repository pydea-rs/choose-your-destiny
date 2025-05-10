from hugchat_interface import HugchatInterface
from decouple import config


def print_streaming_response(response_gen):
    full_text = ""
    for chunk in response_gen:
        if chunk and 'token' in chunk and (token := chunk['token']):
            print(token, end="", flush=True)
            full_text += token
    print()  # Ensure newline after stream ends
    return full_text


email: str = str(config('email', 'email'))
password: str = str(config('password', 'password'))

interface = HugchatInterface(email, password)
print("Initializing story...\n")

# Stream the first activation prompt
response = print_streaming_response(interface.activate(
    "Generate a random interactive story with random genre. Then inside the story, as story is going give the me choices, then i will input my choice and you should continue the story with my decisions. return ENDOFGAME when the story is completed.")
)

if interface.active_model:
    print(f"\n[Using model: {interface.active_model.displayName}]\n")

    while 'ENDOFGAME' not in response:
        user_input = input('> ')
        response = print_streaming_response(interface.prompt(user_input, stream=True))
