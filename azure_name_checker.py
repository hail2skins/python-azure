from azure.mgmt.storage import StorageManagementClient
from azure.identity import DefaultAzureCredential

from decouple import config

subscription_id = config("AZURE_SANDBOX_SUBSCRIPTION_ID")

# Create a StorageManagementClient object
credential = DefaultAzureCredential()
client = StorageManagementClient(credential, subscription_id)

account_name = config("STORAGE_ACCOUNT_NAME")

# Check the availability of the storage account name)

availability = client.storage_accounts.check_name_availability({"name": account_name, "type": "Microsoft.Storage/storageAccounts"})

if availability.name_available:
    print(f"The name {account_name} is available.")
else:
    print(f"The name {account_name} is not available. Reason: {availability.reason}")