from aws_cdk import Stack
from constructs import Construct
#from aws_cdk import RemovalPolicy as cdk
from aws_cdk import aws_s3 as s3

class TestPipeline2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket_name = "my-test-bucket"
        self.bucket = s3.Bucket(self, "test-bucket", bucket_name=bucket_name)


        # The code that defines your stack goes here
