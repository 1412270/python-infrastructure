from aws_cdk import (
    # Duration,
    # aws_sqs as sqs,
    core as cdk,
    aws_lambda
)
from aws_cdk.aws_apigatewayv2_integrations import HttpLambdaIntegration
from aws_cdk import aws_apigatewayv2 as apigwv2
from constructs import Construct


class PythonInfrastructureStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "PythonInfrastructureQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        random_drink_function = aws_lambda.Function(
            self,
            id="RandomDrinkFunction",
            code=aws_lambda.Code.from_asset("python_infrastructure/compute/"),
            handler="random_drink.lambda_handler",
            runtime=aws_lambda.Runtime.PYTHON_3_8
        )

        random_drink_integration = HttpLambdaIntegration(
            "RandomDrinkIntegration", random_drink_function
        )

        http_api = apigwv2.HttpApi(self, "HttpApi")
        http_api.add_routes(
            path="/random_drink",
            methods=[apigwv2.HttpMethod.ANY],
            integration=random_drink_integration
        )
