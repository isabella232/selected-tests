"""Application to serve API of selected-tests service."""
from evergreen import EvergreenApi
from fastapi import FastAPI

from selectedtests.app.controllers import (
    health_controller,
    project_task_mappings_controller,
    project_test_mappings_controller,
)
from selectedtests.datasource.mongo_wrapper import MongoWrapper


def create_app(mongo_wrapper: MongoWrapper, evg_api: EvergreenApi) -> FastAPI:
    """
    Create a selected-tests REST API.

    :param mongo_wrapper: MongoDB wrapper.
    :param evg_api: Evergreen Api.
    :return: The application.
    """
    app = FastAPI(
        version="1.0",
        title="Selected Tests Service",
        description="This service is used to predict which tests and tasks need to run based on"
        " code changes.",
        docs_url="/swagger",
        openapi_url="/swagger.json",
    )
    app.include_router(health_controller.router, prefix="/health", tags=["health"])
    app.include_router(
        project_task_mappings_controller.router,
        prefix="/projects/{project}/task-mappings",
        tags=["projects"],
    )
    app.include_router(
        project_test_mappings_controller.router,
        prefix="/projects/{project}/test-mappings",
        tags=["projects"],
    )
    app.state.db = mongo_wrapper
    app.state.evg_api = evg_api
    return app
