from deployment import DeploymentStage
from aws_cdk import Stack
from constructs import Construct
from aws_cdk import pipelines

class Pipeline(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # Source
        github_repo = pipelines.CodePipelineSource.connection("MarcoCFA/test-pipeline-2", "master",
                                                              connection_arn="arn:aws:codestar-connections:us-east-1:225342792054:connection/0d952b85-4245-42bc-8619-a03128f24aa9")


        synth_step = pipelines.CodeBuildStep(
            "Synth",
            input=github_repo,
            install_commands=["./scripts/installs.sh"],
            commands=["npx cdk synth"],
            primary_output_directory="cdk.out"
        )

        pipeline = pipelines.CodePipeline(self, "GitHubPipeline2", pipeline_name="github-pipeline-2",
                                          cross_account_keys=False, synth=synth_step)

        stage = Deployment(self, "DeployStack")

        pipeline.add_stage(stage, pre=[pipelines.ConfirmPermissionsBroadening("Check", stage=stage)])
        #, pipelines.ManualApprovalStep("Approve Security Changes")])



