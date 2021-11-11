from aws_cdk import Stack, Stage
from constructs import Construct
from aws_service_construct.infrastructure import TestS3BucketConstruct

class DeploymentStage(Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        deploy_stack = Stack(self, "deployStack")

        my_test_bucket = TestS3BucketConstruct(deploy_stack, "my-test-bucket")

