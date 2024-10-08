from azure.cosmos import CosmosClient,PartitionKey
import random
from faker import Faker
from datetime import datetime,timedelta
import time
import pyodbc
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Initialize Faker
fake=Faker()

#Azure Key Vault url
key_vault_url='**********************************'

#Connecting to AzureKeyVault
credential = DefaultAzureCredential()
key_vault_client = SecretClient(vault_url=key_vault_url, credential=credential)

#Fetch Secret from AzureKeyVault
cosmos_url=key_vault_client.get_secret("cosmosdb-endpoint-url").value
cosmos_key=key_vault_client.get_secret("cosmosdb-key").value


# Initialize Cosmos DB Client
cosmos_client= CosmosClient(cosmos_url, credential=cosmos_key)

# Database and Container setup
database_name = 'AirBnb'
container_name = 'bookings'

database = cosmos_client.create_database_if_not_exists(id=database_name)
container= database.create_container_if_not_exists(
    id = container_name,
    partition_key=PartitionKey(path="/booking_id"),
    offer_throughput=400
)

# Function to generate and insert booking data into Cosmos DB record by record
def generate_and_insert_booking_data(num_records,customer_ids):
    for _ in range(num_records):
        record ={
            'id' : fake.uuid4(), # Cosmos DB requires a unique 'id' field
            'booking_id' : fake.uuid4(),
            'property_id' : fake.uuid4(),
            'customer_id' : random.choice(customer_ids),
            'owner_id' : fake.uuid4(),
            'check_in_date' : fake.date_this_year().strftime('%Y-%m-%d'),
            'check_out_date' : (fake.date_this_year() + timedelta(days=random.randint(1,14))).strftime('%Y-%m-%d'),
            'booking_date' : fake.date_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            'amount' : round(random.uniform(50,1000),2),
            'currency' : random.choice(['USD','EUR','GBP','CAD']),
            'property_location' : {
                'city' : fake.city(),
                'country' : fake.country()
            },
            'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Insert each record individually into the Cosmos DB container
        container.create_item(body=record)
        print(f"Inserted record: {record}")
        
        # Sleep for a short time to simulate real-time data insertion
        time.sleep(5)
        
customer_ids=list(range(1,100)) ## Dimension customer in ADLS has customer_ids b/w 1 to 100, so trying to generate same ids
generate_and_insert_booking_data(4,customer_ids)