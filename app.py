#!/usr/bin/env python3
import os

import aws_cdk as cdk
from pipeline import Pipeline
from deployment import DeploymentStage

# from test_pipeline_2.test_pipeline_2_stack import TestPipeline2Stack

APP_ENV = cdk.Environment(account="225342792054", region="us-east-1")

PIPELINE_ENV = cdk.Environment(account="225342792054", region="us-east-2")

app = cdk.App()

# TestPipeline2Stack(app, "TestPipeline2Stack", env=APP_ENV)

DeploymentStage(app, "TestPipelineStack2", env=APP_ENV)

Pipeline(app, "GitHubPipeline2", env=PIPELINE_ENV)

app.synth()
