import boto3

#call the service
dynamodb = boto3.resource('dynamodb')

#Define table
table_name = 'Student_attendence'

#Create DynamoDB table.
table = dynamodb.create_table(
    TableName = table_name,
    KeySchema = [
        {
            'AttributeName': 'Student name',
            'KeyType':'HASH' #Partition key
        },
        {
            'AttributeName': 'Reg no',
            'KeyType':'RANGE' #Sort key
        }
    ],
    AttributeDefinition=[
        {
            'AttributeName': 'Student name',
            'AttributeType': 'S' #String type
        },
        {
            'AttributeName': 'Reg no',
            'AttributeType': 'N' #Numeric type
        },
        {
            'AttributeName': 'Total Attended',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'Percentage',
            'KeyType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 8,
        'WriteCapacityUnits': 8
    }
)

#Wait until the table exists.
table.wait_until_exists()

#print out details
print("Table Status: ", table.table_status)

