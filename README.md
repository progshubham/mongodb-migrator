
# MongoDB Data and Index Migration Script

This script migrates data and indexes from a source MongoDB database to a destination MongoDB database.





## Usage

Install the dependencies from requirements.txt:

```bash
  pip3 install -r requirements.txt
```

Modify the script with the correct MongoDB connection details for the source and destination databases:

```bash
src_client = MongoClient('mongodb://src_username:src_password@src_host:src_port/?authSource=src_auth_db')
dst_client = MongoClient('mongodb://dst_username:dst_password@dst_host:dst_port/?authSource=dst_auth_db')

src_db = src_client['src_db']
dst_db = dst_client['dst_db']

```
    
Run the script:

```bash
  python3 mongo_migrator.py
```


## Requirements

This script requires Python 3 and the following Python packages:

* pymongo


## Why to use this script:

* The script can be used to quickly migrate data and indexes from a source MongoDB instance to a destination MongoDB instance.
* The user needs to specify the credentials and details for both the source and destination MongoDB instances, along with the names of the source and destination databases.
* Once the necessary information is specified, the script will automatically copy over all the data and indexes from the source database to the destination database.

## Advantages:

* Saves time: The script is designed to automate the migration process, which saves a lot of time and effort that would otherwise be required to migrate data and indexes manually.
* Preserves data integrity: The script copies over all the indexes and data from the source database to the destination database, which ensures that the data is transferred accurately and without any loss.
* Easy to use: The script is straightforward to use and can be modified to suit the user's specific needs.
* Customizable: The script is written in Python, which is a highly customizable and flexible programming language. Users can modify the script to add new features or customize it to suit their specific requirements.

If you find mongodb-migrator helpful, please consider starring the project on GitHub. It helps to boost the project's visibility and encourages the maintainers to continue improving it. Thank you!


