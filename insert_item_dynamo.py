#To add single item:-
import boto3

#Call the service
dynamodb = boto3.resource('dynamodb')

#define table
table_name = 'Student_attendance'

#call the table with name
table = dynamodb.Table(table_name)

#Put an item to the table with attributes
table.put_item(
    Item = [
        {
        'Student name':'Swarab Raul',
        'Reg no':155, #Reg no is defined as N, so nno double quotes
        'Attended': 'Y',
        'Date': '2024-08-04',
        },
        ]
    
)

#To add multiple items:-
import boto3

#Call the service
dynamodb = boto3.resource('dynamodb')

#define table
table_name = 'Student_attendance'

#call the table with name
table = dynamodb.Table(table_name)

#Put an item to the table with attributes

Items = [
    {
    'Student name':'Swarab Raul',
    'Reg no':155, #Reg no is defined as N, so nno double quotes
    'Attended': 'Y',
    'Date': '2024-08-04',
    },
    {
    'Student name': 'Rabindranath',
    'Reg no': 156,         
    'Attended': 'Y',
    'Date': '2024-08-04',
    },
    {
    'Student name': 'Manjunath',
    'Reg no': 159,        
    'Attended': 'Y',
    'Date': '2024-08-04',
    }
    ]
#Insert each items
for item in Items:
    table.put_item(Item=item)
    
