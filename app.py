from vector_database import CassandraDatabase
import time
from controller import GameController
from decouple import config

open_ai_api_key = config('OPENAI_API_KEY')
token_json_path = config('TOKEN_JSON_PATH')
bundle_zip_path = config('BUNDLE_ZIP_PATH')
astra_db_keyspace = config('ASTRA_DB_KEYSPACE')
memory_key='tempkey'

print(open_ai_api_key, token_json_path, bundle_zip_path, astra_db_keyspace)
if __name__ == '__main__':
    database = CassandraDatabase(token=token_json_path, bundle=bundle_zip_path, astra_db_keyspace=astra_db_keyspace)
    result = database.connect(chat_id=memory_key)
    game = GameController(memory=database.chats_history, openai_api_key=open_ai_api_key)
    if result:
        game.telltale()
    print("\n\nBye!")
