from constructs import Construct
import aws_cdk as cdk
from aws_cdk import aws_s3 as s3


class TestS3BucketConstruct(Construct):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket_name = "my-test-bucket-1981-2021"
        self.bucket = s3.Bucket(
            self,
            "test-bucket",
            bucket_name=bucket_name,
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )
