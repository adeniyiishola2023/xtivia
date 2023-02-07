import boto3
import os

def copy_all_objects():
    src_bucket_name = os.environ['SRC_BUCKET_NAME']
    dst_bucket_name = os.environ['DST_BUCKET_NAME']
    min_size = int(os.environ['MIN_OBJECT_SIZE'])

    s3 = boto3.client('s3')

    # Get a list of all object keys and sizes in the source bucket
    result = s3.list_objects(Bucket=src_bucket_name)
    object_keys = [content['Key'] for content in result.get('Contents', []) if content['Size'] >= min_size]

    # Copy each object from the source bucket to the destination bucket
    for key in object_keys:
        copy_source = {'Bucket': src_bucket_name, 'Key': key}
        s3.copy_object(Bucket=dst_bucket_name, CopySource=copy_source, Key=key)

# Call the function
copy_all_objects()

