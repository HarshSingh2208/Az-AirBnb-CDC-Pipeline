# Az-AirBnb-CDC-Pipeline
AirBnB CDC Ingestion Pipeline & Mock Data Generator

Overview
This repository contains two key components for managing data ingestion and testing processes related to AirBnB's Change Data Capture (CDC) pipeline. The project integrates with Azure services such as Cosmos DB, Azure Synapse Analytics, and Azure Data Factory (ADF). It includes:

AirBnB CDC Ingestion Pipeline: Built using Azure Data Factory to handle real-time data ingestion, transformation, and processing from multiple data sources.
Mock Data Generator: A Python script designed to generate synthetic booking data for testing the ingestion pipeline by inserting records into Cosmos DB.
Project Structure
1. AirBnB CDC Ingestion Pipeline
Functionality:

Ingests data from multiple sources, including ADLS and Cosmos DB.
Performs data transformations and loads data into Azure Synapse for further analysis.
Sends success and failure email notifications based on the pipeline execution outcome.
Trigger: The pipeline is triggered every 1 hour to ensure timely processing of real-time data coming into Cosmos DB. This ensures that even though data arrives in real-time, it is processed and transformed at regular intervals.
2. Mock Data Generator for Cosmos DB
Functionality:

Generates and inserts synthetic booking data into Cosmos DB.
Utilizes the Faker library to create realistic mock data such as booking IDs, customer IDs, property IDs, etc.
Integrates with Azure Key Vault to securely retrieve Cosmos DB credentials.
Requirements
AirBnB CDC Ingestion Pipeline:
Mock Data Generator:
Setup
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-repo/airbnb-cdc-pipeline.git
cd airbnb-cdc-pipeline
2. Running the Mock Data Generator
Install the required Python dependencies:

bash
Copy code
pip install azure-cosmos faker azure-identity azure-keyvault-secrets
To run the script, simply execute:

bash
Copy code
python mock-data-in-cosmosDB.py
3. Deploying the AirBnB CDC Pipeline
Import the ARM template ARMTemplateForFactory.json in Azure Data Factory to create the pipeline resources.
Update the necessary parameters such as Cosmos DB credentials, ADLS path, and Synapse Analytics connections.
Ensure that the pipeline is configured to trigger every 1 hour.
Usage
Mock Data Generator
The mock data generator script allows you to generate and insert synthetic booking data into the Cosmos DB container for testing. The script fetches sensitive credentials (Cosmos DB endpoint and key) from Azure Key Vault, ensuring secure access. You can specify the number of records to generate and the customer IDs for the bookings.

AirBnB CDC Pipeline
The AirBnB CDC pipeline manages the real-time ingestion, transformation, and processing of customer and booking data. While data arrives in real-time in Cosmos DB, the pipeline processes it every 1 hour to ensure batch transformation and loading into Azure Synapse Analytics.

License
This project is licensed under the MIT License.

Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.

This enhanced README adds visual elements (badges/icons) for different tools and services, making the content more engaging. Let me know if you'd like to adjust anything!
