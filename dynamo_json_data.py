import json
import boto3
import os
from pprint import pprint
import tqdm


def aws_res():
    aws_resource = boto3.resource('dynamodb',region_name='ap-south-1')
    # call table
    dynamo_table = aws_resource.Table('Student_database')
    # get_status = dynamo_table.table_status
    # print(get_status)
    return dynamo_table

def call_json():
    with open(r'dummy_data.json','r') as file:
        data_sheet = json.load(file)
        # pprint(data_sheet,sort_dicts=False)
        return data_sheet

# If data is correct:   
def transfer_data(json_sheet,dynamodb_sheet):
    for details in tqdm.tqdm(json_sheet):
        try:
            dynamodb_sheet.put_item(Item = details)
            print("Data transfer successful")
        except Exception as e:
            print(f"Failed data transfer : {e}")
    
# if data has some empty of missmatch_data type.
def transfer_data(json_sheet,dynamodb_sheet):
    for details in tqdm.tqdm(json_sheet):
        try:
            # Ensure stud_Id is not empty and is a valid integer
            stud_Id = details.get("stud_Id", None)
            if stud_Id is None  or not isinstance(stud_Id, int):
                print(f"invalid student data; {details}")
                break
            
            # Ensure stud_Name is a string
            # details["stud_Name"] = str(details.get("stud_Name", ""))
            stud_Name = details.get("stud_Name", None)
            if len(stud_Name.strip( )) == 0 or not isinstance(stud_Name, str):
                print(f"Invalid data: {details}")
                break
            
            # Handle missing personal_detail by assigning an empty dictionary if missing
            details["personal_detail"] = details.get("personal_detail", {})
            
            # Insert the item into DynamoDB
            dynamodb_sheet.put_item(Item = details)
            print("Data transfer Success.")
        except Exception as e:
            print(f"Data transfer failed: {e}")
            break



if __name__ == "__main__":
    get_json = call_json()
    get_dynamo_table = aws_res()
    data_transfer = transfer_data(get_json,get_dynamo_table)
    
        