import random
import time

from hugchat_agent import HugchatAgent
from decouple import config


email: str = str(config('email', 'email'))
password: str = str(config('password', 'password'))

interface = HugchatAgent(email, password)
query_result = interface.activate("I want you to generate a random interactive story with random genre. Then inside the stpry, as story is going give the me choices, then i will input my choice and you should continue the story with my decisions. return ENDOFGAME when the story is completed.")
print(query_result)

if interface.active_model:

    print(interface.active_model.displayName)

    while query_result != 'ENDOFGAME':
        time.sleep(1)
        prompt = input('> ')
        query_result = interface.prompt(prompt)
        print(query_result)
