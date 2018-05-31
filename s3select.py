import boto3
import botocore

# As our text file doesn't have headers we can refer to the columns as _1, _2 etc ...
s3 = boto3.client('s3')
def lambda_handler(event,context):    
    r = s3.select_object_content(
        Bucket='taupirho',
        Key='iholding/issueholding.txt',
        ExpressionType='SQL',
        Expression="select * from s3object s where s._2 = 1",
        InputSerialization = {'CSV': {"FileHeaderInfo": "None"}},
        OutputSerialization = {'CSV': {}},
    )
    
    for event in r['Payload']:
        if 'Records' in event:
            records = event['Records']['Payload'].decode('utf-8')
            print(records)
        elif 'Stats' in event:
            statsDetails = event['Stats']['Details']
            print("Stats details bytesScanned: ")
            print(statsDetails['BytesScanned'])
            print("Stats details bytesProcessed: ")
