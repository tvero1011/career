from aws_resource_checker import create_session


def test_boto3_session_creation():
    session = create_session()
    assert session is not None
