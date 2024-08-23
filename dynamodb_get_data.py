import boto3
import os
import requests
from boto3.dynamodb.conditions import Key

# Creating DynamoDb Client
aws_client = boto3.client('dynamodb', region_name="ap-south-1")

aws_service = boto3.resource('dynamodb', region_name="ap-south-1")
dynamodb_table = aws_service.Table('Student_database')
table_name = "Student_database"
status = dynamodb_table.table_status
print(status)

# Get a single Item:

get_data = aws_client.get_item(
    TableName = table_name,
    Key={
        'stud_Id':{'N': '4'},
        'stud_Name': { 'S': "Karan"},
    }
)
print(get_data['Item'])