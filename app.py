#!/usr/bin/env python3
import os

import aws_cdk as cdk

from test_pipeline_2.test_pipeline_2_stack import TestPipeline2Stack

APP_ENV = cdk.Environment(account="225342792054", region="us-east-1")

app = cdk.App()
TestPipeline2Stack(app, "TestPipeline2Stack", env=APP_ENV)

app.synth()
