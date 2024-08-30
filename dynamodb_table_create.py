import boto3
<<<<<<< HEAD
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
=======
import os

def create_dynamo_table():
    dyn_table = boto3.resource('dynamodb')
    table_name = 'Student_database'

    params = {
        "TableName" : table_name,
        "KeySchema" : [
            {"AttributeName" : "stud_Id", "KeyType" : "HASH"},
            {"AttributeName" : "stud_Name", "KeyType" : "RANGE"}
        ],
        "AttributeDefinitions" : [
            {"AttributeName" : "stud_Id", "AttributeType" : "N" },
            {"AttributeName" : "stud_Name", "AttributeType" : "S"}
        ],
        "ProvisionedThroughput" : {"ReadCapacityUnits" : 10, "WriteCapacityUnits" : 10},
    }
    table_create = dyn_table.create_table(**params)
    print(f"Creating {table_name}....")
    table_create.wait_until_exists()
    return table_create

if __name__ == "__main__":
    call_table = create_dynamo_table()
    print("Successfully dynamobd table created.")
>>>>>>> master
