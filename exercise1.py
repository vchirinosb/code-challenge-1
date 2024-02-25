"""
Refactor the next function using yield to return the array of objects found by
the `s3.list_objects_v2` function that matches the given prefix.
"""
import boto3


def get_s3_objects(bucket, prefix=''):
    """
    :param bucket: str, bucket name.
    :param prefix: str, prefix to search.

    :return: List, found objects.
    """
    s3 = boto3.client('s3')
    kwargs = {'Bucket': bucket}
    next_token = None

    if prefix:
        kwargs['Prefix'] = prefix

    while True:
        if next_token:
            kwargs['ContinuationToken'] = next_token
        resp = s3.list_objects_v2(**kwargs)
        contents = resp.get('Contents', [])
        for obj in contents:
            key = obj['Key']
            if key.startswith(prefix):
                yield obj

        next_token = resp.get('NextContinuationToken', None)

        if not next_token:
            break


if __name__ == '__main__':
    """
    Test method get_s3_objects.

    e.g. of expected output to print:
    'documents/document_1.docx'
    'documents/folder_1/document_2.docx'
    'documents/folder_2/document_3.docx'

    Explanation:
    The method get_s3_objects yields each object (when it's found) allowing
    memory efficiency.
    """
    bucket = 'bucket'
    prefix = 'documents/'

    for obj in get_s3_objects(bucket, prefix):
        print(obj['Key'])
