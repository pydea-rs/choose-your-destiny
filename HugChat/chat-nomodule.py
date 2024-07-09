import random
import time

from hugchat import hugchat
from hugchat.login import Login
from decouple import config

email: str = str(config('email', 'email'))
password: str = str(config('password', 'password'))

cookie_path_dir = "./cookies/"
sign = Login(email, password)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

models = chatbot.get_available_llm_models()

for model in models:
    print(model.displayName)

model_index = random.randint(0, len(models))

chatbot.switch_llm(model_index)

print(chatbot.get_active_llm_index())

if chatbot.active_model:
    print(chatbot.active_model.displayName)

    # chatting
    query_result = chatbot.query("I want you to generate a random interactive story with random genre. Then inside the stpry, as story is going give the me choices, then i will input my choice and you should continue the story with my decisions. return ENDOFGAME when the story is completed.", web_search=False)
    print(query_result)
    # chatting
    print(chatbot.active_model.displayName)

    while query_result != 'ENDOFGAME':
        time.sleep(3)
        # chatbot.new_conversation(switch_to = True) # switch to the new conversation

        prompt = input('> ')
        query_result = chatbot.query(prompt, web_search=False)
        print(query_result)