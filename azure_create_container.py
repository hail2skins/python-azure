# Want to create a container in Azure and will protect env variables with python-decouple

# Azure imports for DefaultAzureCredential, StorageManagementClient, ResourceManagementClient
from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.storage.blob import BlobServiceClient

# Python decouple to protect environment variables
from decouple import config

# Acquire a credential object using DefaultAzureCredential
credential = DefaultAzureCredential()

# Retrieve a subscription_id from environment variables using python-decouple
#subscription_id = config('AZURE_SANDBOX_SUBSCRIPTION_ID') # Sandbox subscription
subscription_id = config('DSNONPROD_SUBSCRIPTION_ID') # DSNONPROD subscription

# Obtain the managggement object for resources
resource_client = ResourceManagementClient(credential=credential, subscription_id=subscription_id)

# Set the resource group name and location for the new storage account
RESOURCE_GROUP_NAME = config("RESOURCE_GROUP_NAME")
LOCATION = config("LOCATION")

# Obtain the management object for storage
storage_client = StorageManagementClient(credential=credential, subscription_id=subscription_id)

# Create the storage account
STORAGE_ACCOUNT_NAME = config("STORAGE_ACCOUNT_NAME")

# Define container name
CONTAINER_NAME = config("CONTAINER_NAME")

# # Creating 10 containers
# for i in range(10):
#     unique_container_name = f"{CONTAINER_NAME}{i+1}"
#     container = storage_client.blob_containers.create(
#         RESOURCE_GROUP_NAME,
#         STORAGE_ACCOUNT_NAME,
#         unique_container_name,
#         {}
#     )
#     print(f"Created container {unique_container_name} in storage account {STORAGE_ACCOUNT_NAME} in resource group {RESOURCE_GROUP_NAME}")
    
# # Now I want to remove every container in the resource group
# for container in storage_client.blob_containers.list(RESOURCE_GROUP_NAME, STORAGE_ACCOUNT_NAME):
#     storage_client.blob_containers.delete(RESOURCE_GROUP_NAME, STORAGE_ACCOUNT_NAME, container.name)
#     print(f"Deleted container {container.name} in storage account {STORAGE_ACCOUNT_NAME} in resource group {RESOURCE_GROUP_NAME}")

# Initialize BlobServiceClient with DefaultAzureCredential
blob_service_client = BlobServiceClient(account_url=f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net", credential=credential)

# Now I want to access every container in the resource group and access a list of blobs in each container
# For now we just want a count of the blobs in each container
# Iterate through each container in the storage account
for container in storage_client.blob_containers.list(RESOURCE_GROUP_NAME, STORAGE_ACCOUNT_NAME):
    container_client = blob_service_client.get_container_client(container.name)
    blobs = list(container_client.list_blobs())
    print(f"Container {container.name} in storage account {STORAGE_ACCOUNT_NAME} in resource group {RESOURCE_GROUP_NAME} has {len(blobs)} blobs")








