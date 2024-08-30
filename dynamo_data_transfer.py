import json
import boto3
import os
import tqdm
import requests

# dynamo_client = boto3.resource('dynamodb', region_name = 'ap-south-1')

# created_table = dynamo_client.Table('product_table')

# status = created_table.table_status
# print(status)

def get_data():
    with open(r'matrimony_data.json', 'r') as file_to_pass:
        data_file = json.load(file_to_pass)
        return data_file
    
def pass_data(json_file):
    dynamo_client = boto3.resource('dynamodb', region_name = 'ap-south-1')

    created_table = dynamo_client.Table('product_table')
    
    for record in tqdm.tqdm(json_file):
        # record["user_name"] = (record["user_name"])
        # record["product_id"] = str(record["product_id"])
        # record["user_contact"] = str(record["user_contact"])
        # record["user_gender"] = (record["user_gender"])
        # record["email_id"] = str(record["email_id"])
        # record["birth_date"] = (record["birth_date"])
        # record["user_location"] = (record["user_location"])
        # record["user_job"] = (record["user_job"])
        # record["user_education"] = (record["user_education"])
        # record["user_height"] = str(record["user_height"])
        # record["user_nakshatra"] = (record["user_nakshatra"])
        # record["user_rashi"] = (record["user_rashi"])
        # record["bhari_father"] = (record["bhari_father"])
        # record["bhari_mother"] = (record["bhari_mother"])
        
        
        # To avoid the KeyError, or if any value is empty, So we use .get()
        record["user_name"] = (record.get("user_name", ""))
        record["product_id"] = str(record.get("product_id", ""))
        record["user_contact"] = str(record.get("user_contact", ""))
        record["user_gender"] = (record.get("user_gender", ""))
        record["email_id"] = str(record.get("email_id", ""))
        record["birth_date"] = (record.get("birth_date", ""))
        record["user_location"] = (record.get("user_location", ""))
        record["user_job"] = (record.get("user_job", ""))
        record["user_education"] = (record.get("user_education", ""))
        record["user_height"] = str(record.get("user_height", ""))
        record["user_nakshatra"] = (record.get("user_nakshatra", ""))
        record["user_rashi"] = (record.get("user_rashi", ""))
        record["bhari_father"] = (record.get("bhari_father", ""))
        record["bhari_mother"] = (record.get("bhari_mother", ""))
        created_table.put_item(Item = record)
        print("Succesfully transfered")

files = get_data()
pass_data(files)
