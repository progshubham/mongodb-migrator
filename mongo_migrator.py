from pymongo import MongoClient
from pymongo.operations import InsertOne

# Define the source and destination MongoDB hosts
src_client = MongoClient('mongodb://src_username:src_password@src_host:src_port/?authSource=src_auth_db')
dst_client = MongoClient('mongodb://dst_username:dst_password@dst_host:dst_port/?authSource=dst_auth_db')

# Set the source and destination databases
src_db = src_client['src_db']
dst_db = dst_client['dst_db']

# Get a list of all the collections in the source database
collections = src_db.list_collection_names()

# Loop through each collection and migrate the data and indexes to the destination database
for collection_name in collections:
    src_collection = src_db[collection_name]
    dst_collection = dst_db[collection_name]

    # Check if the source collection is empty
    if src_collection.count_documents({}) == 0:
        print(f"{collection_name} is empty")

    # Create the destination collection if it doesn't exist
    if collection_name not in dst_db.list_collection_names():
        print(f"Creating collection {collection_name}")
        dst_db.create_collection(collection_name, capped=False)

    # Copy the data
    if src_collection.count_documents({}) >= 1:
        dst_collection.insert_many(src_collection.find())

    # Copy the indexes
    indexes = src_collection.index_information()
    for name, index in indexes.items():
        if name == '_id_':
            continue
        key = index['key']
        if 'kwargs' in index:
            kwargs = index['kwargs']
            dst_collection.create_index(key, name=name, **kwargs)
        else:
            dst_collection.create_index(key, name=name)

# Close the MongoDB connections
src_client.close()
dst_client.close()

print('Data and index migration complete.')