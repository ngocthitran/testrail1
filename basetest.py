import pytest


@pytest.mark.usefixtures("driver_init", "logger_init", "credentials_init")
class BaseTest:
    pass
