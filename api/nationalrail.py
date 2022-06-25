from random import triangular
import boto3
import gzip
import xml.etree.ElementTree as ET

session = boto3.Session(
    aws_access_key_id="AKIAIPNSD2N5FJC5CMSQ",
    aws_secret_access_key="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",
    region_name="eu-west-1"
)

s3_client = session.client('s3')


objects = s3_client.list_objects_v2(
    Bucket='darwin.xmltimetable',
    Prefix='PPTimetable/',
)
  

latest = max(objects['Contents'], key=lambda x: x['LastModified'])

with open('api/data.xml.gz', 'wb') as data:
    s3_client.download_fileobj('darwin.xmltimetable', latest['Key'], data)

train_data = gzip.open('api/data.xml.gz','r') 

tree = ET.parse(train_data)
root = tree.getroot()

print(root.tag)
print(root.attrib)


# darwin.xmltimetable
# PPTimetable/