import boto3
import os
import requests
from boto3.dynamodb.conditions import Attr
from botocore.exceptions import ClientError
from pprint import pprint

def into_table():
    dynamo_client = boto3.resource("dynamodb")
    data_table = dynamo_client.Table("product_table")
    return data_table

#'Key' parameter only accepts the primary key or the partition key and optionally the sort key.
def get_data(prod_id:int, table):
    try:
        response = table.get_item(
            # Key={'father_bhari': name_father_bhari, 'mother_bhari': name_mother_bhari}
            Key ={'product_id': str(prod_id)}
        )
    except ClientError as e:
        print(e)
        # .response['No item found.'])
    else:
        return response["Item"]
    

#Multi-Attributes Support in 'get_item' : Query method, The user_gender can be used as a sort key if required.
# def get_match_data(father_bhari:str, mother_bhari:str, gender: str, table):
#     try:
#         response = table.query(
#             KeyConditionExpression="bhari_father"= :father_bhari & 'bhari_mother'= :mother_bhari & 'user_gender'= :gender,
#             ExpressionAttributeValues={
#                 ":father_bhari": str(father_bhari),
#                 ":mother_bhari": str(mother_bhari),
#                 ":gender": str(gender)
#             },
#         )
#     except ClientError as e:
#         print(e)
#     else:
#         return response.get("Item",[])

def get_match_data(father_bhari:str, mother_bhari:str, gender: str, table):
    try:
        response = table.scan(
            FilterExpression=Attr("bhari_father").eq(father_bhari) & Attr('bhari_mother').eq(mother_bhari) & Attr('user_gender').eq(gender)
        )

        
    except ClientError as e:
        print(e)
    else:
        return response.get("Items",[])
        # return response["Items"]
    



get_table = into_table()
find_data = get_match_data("Salyan", "Banjan", "Male", get_table)
if find_data:
    pprint(find_data,sort_dicts=False)
