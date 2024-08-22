import boto3
import requests
import os

def create_dyn_table():
    
    dynamo_table = boto3.resource("dynamodb")
    table_name = "Student_table"
    
    params = {
        "TableName" : table_name,
        "KeySchema" : [
            {
                'AttributeName' : 'userId',
                'KeyType' : 'HASH'
            },
            {
                'AttributeName' : 'userName',
                'KeyType' : 'RANGE'
            }
        ],
        "AttributeDefinitions": [
            {
                'AttributeName' : 'userEmail',
                'AttributeType' : 'S'
            },
            {
                'AttributeName' : 'userName',
                'AttributeType' : 'S'
            }
        ],
        "ProvisionedThroughput" :{
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
        
    }
    
    # table = dynamo_table.create_table(
    #     TableName=table_name,
    #     KeySchema = [
    #         {
    #             'AttributeName' : 'userId',
    #             'KeyType' : 'HASH'
    #         },
    #         {
    #             'AttributeName' : 'userName',
    #             'KeyType' : 'RANGE'
    #         }
    #     ],
    #     AttributeDefinitions=[
    #         {
    #             'AttributeName' : 'userEmail',
    #             'AttributeType' : 'S'
    #         },
    #         {
    #             'AttributeName' : 'userName',
    #             'AttributeType' : 'S'
    #         }
    #     ],
    #     ProvisionedThroughput={
    #         'ReadCapacityUnits': 1,
    #         'WriteCapacityUnits': 1
    #     }
    # )
    print(f"Creating {table_name}...")
    table = dynamo_table.create_table(**params)
    table.wait_until_exists()
    return table.table_status
    
    
    
if __name__ == "__main__":
    student_table = create_dyn_table()
    print("Table created.")