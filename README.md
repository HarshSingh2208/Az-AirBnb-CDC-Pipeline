# 🚀 AirBnB CDC Ingestion Pipeline

## 📋 Overview

This repository contains the AirBnB Change Data Capture (CDC) Ingestion Pipeline, built using Azure Data Factory (ADF) to handle real-time data ingestion, transformation, and processing. The pipeline integrates with Azure services like Cosmos DB, Azure Synapse Analytics, and Azure Data Lake Storage (ADLS) to enable robust, scalable data workflows.

The initial step of the pipeline involves generating mock booking data using a Python script. This mock data is then ingested into Cosmos DB, and the pipeline processes the data at regular intervals to ensure it is available for analytics and reporting.

## 🛠️ Project Structure

### AirBnB CDC Ingestion Pipeline
- **Technology Stack**: Azure Data Lake Storage (ADLS), Cosmos DB, Azure Synapse Analytics, Azure Data Factory (ADF), Python , Azure KeyVault , Logic Apps
- **Functionality**:
  - **🎉 Mock Data Generation** (Initial Step):
    - A Python script generates and inserts synthetic booking data into Cosmos DB for testing and development purposes.
    - The data is generated using the `Faker` library and is securely inserted into Cosmos DB by retrieving credentials from Azure Key Vault.
  - **🔄 Data Processing**:
    - Ingests data from Cosmos DB and ADLS, performing necessary transformations.
    - Transforms the data and loads it into Azure Synapse Analytics for downstream analytics.
  - **🔧 Data Transformation**:
    - Key transformations are performed, including customer dimension loading and booking fact transformations, ensuring the data is ready for analytics.
  - **⏰ Pipeline Trigger**:
    - The pipeline is triggered every **1 hour** to process and transform the real-time data arriving in Cosmos DB.
  - **📧 Success and Failure Notifications**:
    - Email notifications are sent upon successful execution or failure of the pipeline to ensure timely action.

## 📋 Requirements

- Azure Data Factory
- Azure Data Lake Storage (ADLS)
- Cosmos DB
- Azure Synapse Analytics
- Python 3.x
- Azure SDK for Python (`azure-cosmos`, `azure-identity`, `azure-keyvault-secrets`)
- `Faker` library for generating mock data

## 🛠️ Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/airbnb-cdc-pipeline.git
cd airbnb-cdc-pipeline
```

### 2. Running the Mock Data Generation Script
Install the required Python dependencies:
```bash
pip install azure-cosmos faker azure-identity azure-keyvault-secrets
```

To generate mock data and insert it into Cosmos DB:
```bash
python mock-data-in-cosmosDB.py
```

### 3. Deploying the AirBnB CDC Pipeline
- Import the ARM template `ARMTemplateForFactory.json` in Azure Data Factory to create the pipeline resources.
- Update the necessary parameters such as Cosmos DB credentials, ADLS path, and Synapse Analytics connections.
- Ensure that the pipeline is configured to trigger every **1 hour** for periodic data processing.

## 📊 Usage

### Pipeline Steps
1. **🎉 Mock Data Generation**: Generates and inserts synthetic booking data into Cosmos DB using the Python script.
2. **🔄 LoadCustomerDim Pipeline**: Processes and loads customer data from ADLS to Synapse.
3. **🔄 LoadBookingFact Pipeline**: Transforms booking data from Cosmos DB and stores it in a fact table in Synapse.
4. **📁 Error Handling**: Any bad records encountered during processing are captured and stored separately for auditing purposes.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.
