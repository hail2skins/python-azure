import asyncio
from azure.storage.blob.aio import BlobServiceClient
from azure.identity.aio import DefaultAzureCredential
from decouple import config
import time

async def count_containers_in_account(account_name, credential):
    async with BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=credential) as client:
        container_count = 0
        async for container in client.list_containers():
            container_count += 1
        print(f"Total containers in {account_name}: {container_count}")
        return container_count

async def main():
    start_time = time.time()

    # Acquire a credential object using DefaultAzureCredential
    credential = DefaultAzureCredential()

    # Retrieve storage account names from environment variables and split into a list
    storage_account_names = config("STORAGE_ACCOUNT_NAMES").split(',')

    # Gather all tasks
    tasks = [count_containers_in_account(name, credential) for name in storage_account_names]
    container_counts = await asyncio.gather(*tasks)

    total_containers = sum(container_counts)
    print(f"Total containers across all storage accounts: {total_containers}")

    # Calculate the total execution time
    execution_time = time.time() - start_time
    print(f"Total execution time: {execution_time} seconds")

# Run the main coroutine
asyncio.run(main())