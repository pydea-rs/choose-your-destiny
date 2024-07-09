from astrapy import DataAPIClient
import os
# Initialize the client
client = DataAPIClient(os.getenv('DATAPI_TOKEN'))
db = client.get_database_by_api_endpoint(
  "https://c27c5eb4-0d01-43b2-a340-cc855e813c87-us-east1.apps.astra.datastax.com",
    namespace="default_keyspace",
)
      
print(f"Connected to Astra DB: {db.list_collection_names()}")