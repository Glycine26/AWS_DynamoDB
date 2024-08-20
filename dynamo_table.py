import boto3
import os
import requests
import tqdm
from pprint import pprint
from boto3.dynamodb.conditions import Attr


dynamo_client = boto3.resource('dynamodb', region_name='ap-south-1')

# connecting with table
student_table = dynamo_client.Table('product_table')

#Determining the table status
# get_status = student_table.table_status
# print(get_status)

#Create records to table:
product1 = student_table.put_item(Item = {"product_name": "TV", "Brand": "Samsung", "Price": 35000, "product_id": "prod01"})
# pprint(product1)
product2 = student_table.put_item(Item = {"product_id": "prod02", "prod_name": "Refrigerator", "prod_price":40000, "prod_brand": "LG"})

#get back the data
info_get = student_table.get_item(Key= {"product_id":"prod02"})
# pprint(info_get)

product3 = student_table.put_item(Item = {"product_id":"prod03", "prod_name":"Bulb", "prod_price":500, "prod_brand":"philipp's"})

# edit the info by addinng new column
info_change = student_table.update_item(Key= {"product_id":"prod01"}, UpdateExpression = 'set GST=:S', ExpressionAttributeValues = {":S":12})

#edit the exist info
info_edit = student_table.update_item(Key= {"product_id":"prod01"}, UpdateExpression=  'set price=:S', ExpressionAttributeValues= {":S":10000})

#delete the data
info_del = student_table.delete_item(Key={"product_id":"prod100"})

# Querying the records
querry1 = student_table.scan(Select = "ALL_ATTRIBUTES", FilterExpression = Attr("price").eq(10000) & Attr('GST').eq(13))
pprint(querry1)