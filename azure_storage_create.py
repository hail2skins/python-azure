# Want to create a storage account and container in Azure and will protect env variables with python-decouple

# Azure imports for DefaultAzureCredential, StorageManagementClient, ResourceManagementClient
from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.resource import ResourceManagementClient

# Python decouple to protect environment variables
from decouple import config

# Acquire a credential object using DefaultAzureCredential
credential = DefaultAzureCredential()

# Retrieve a subscription_id from environment variables using python-decouple
subscription_id = config('AZURE_SANDBOX_SUBSCRIPTION_ID')

# Obtain the managggement object for resources
resource_client = ResourceManagementClient(credential=credential, subscription_id=subscription_id)

# Set the resource group name and location for the new storage account
RESOURCE_GROUP_NAME = config("RESOURCE_GROUP_NAME")
LOCATION = config("LOCATION")

# Obtain the management object for storage
storage_client = StorageManagementClient(credential=credential, subscription_id=subscription_id)

# Create the storage account
STORAGE_ACCOUNT_NAME = config("STORAGE_ACCOUNT_NAME")

# Check if the storage account name is available, if not, create a unique name
availability_result = storage_client.storage_accounts.check_name_availability({"name": STORAGE_ACCOUNT_NAME})

if not availability_result.name_available:
    print(f"Storage name {STORAGE_ACCOUNT_NAME} is already in use. Start again.")
    exit()
    
# The name is available so provision the account
poller = storage_client.storage_accounts.begin_create(RESOURCE_GROUP_NAME, STORAGE_ACCOUNT_NAME,
    {
        "location": LOCATION,
        "sku": {"name": "Standard_LRS"},
        "encryption": {"enabled": True},
    }
)

# Long-running operations return a poller object; calling poller.result() waits for completion
account_result = poller.result()
print(f"Created storage account {account_result.name} in resource group {RESOURCE_GROUP_NAME}")





