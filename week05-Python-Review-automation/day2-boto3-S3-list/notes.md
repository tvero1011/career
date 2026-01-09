# Boto3 S3 Bucket Script Notes

## Imports
- boto3: Python AWS SDK
- ClientError, NoCredentialsError: handle API errors

## Function: list_buckets()
- Creates S3 client
- Calls list_buckets API
- Loops through buckets (if any)
- Prints bucket names
- Handles missing credentials
- Handles AWS API errors

## Key points
- `response` is a dict
- Use `.get("Buckets", [])` to avoid crash if empty
- Empty bucket list is normal; success ≠ data exists
