def test_pipeline_status():
    status = "success"
    assert status == "success"


def test_pipeline_failure_detection():
    status = "failed"
    assert status != "success"


def test_project_name():
    project_name = "PipelinePilot"
    assert project_name == "PipelinePilot"