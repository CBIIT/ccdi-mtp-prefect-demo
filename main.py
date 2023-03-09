from prefect import task, flow
from prefect.deployments import Deployment
from prefect import flow, get_run_logger

def console(obj):
    logger = get_run_logger()
    logger.info(obj)


@task
def printer(obj):
    console(f"Received a {type(obj)} with value {obj}")

# note that we define the flow with type hints
@flow
def validation_flow_2(x: int, y: str):
    printer(x)
    printer(y)


deployment = Deployment.build_from_flow(
    flow=validation_flow_2,
    name="prefect-example-deployment",
)

deployment.apply()


validation_flow_2(1,2)