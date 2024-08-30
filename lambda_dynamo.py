import boto3

# Call the service
dynamodb = boto3.resource('dynamodb')

# Define table
table_name = 'Student_attendance'

# Create DynamoDB table
table = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {
            'AttributeName': 'Student name',
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': 'Reg no',
            'KeyType': 'RANGE'  # Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Student name',
            'AttributeType': 'S'  # String type
        },
        {
            'AttributeName': 'Reg no',
            'AttributeType': 'N'  # Numeric type
        }
        # Do not include other attributes here unless they are part of the KeySchema
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 8,
        'WriteCapacityUnits': 8
    }
)

# Wait until the table exists
table.wait_until_exists()

# Print out details
print("Table Status: ", table.table_status)