# Running tutorial on https://learn.microsoft.com/en-us/azure/developer/python/get-started?tabs=cmd to learn how to use Azure SDK for Python
# Simply lists all the resource groups in the subscription
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# random to start working with Azure SDK for Python
import random

# To protect environmeent variables use python decouple
from decouple import config
# we need azure resources to work with Azure SDK for Python
# DefaultAzureCredential is a credential that looks for Azure Active Directory (AAD)
# ResourceManagementClient is a client for managing Azure resources
# StorageManagementClient is a client for managing Azure Storage resources
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# Acquire a credential object using DefaultAzureCredential
credential = DefaultAzureCredential()

# Retrieve a subscription_id from environment variables using python-decouple
subscription_id = config("AZURE_SANDBOX_SUBSCRIPTION_ID")

# Create a resource management client
resource_client = ResourceManagementClient(credential=credential, subscription_id=subscription_id)

# Retrieving a list of resource groups in the subscription
resource_groups = resource_client.resource_groups.list()

# Format the groups in a formatted output
column_width = 40

print("Resource Group".ljust(column_width) + "Location")
print("-" * (column_width * 2))

for group in resource_groups:
    print(f" {group.name.ljust(column_width)} {group.location}")





