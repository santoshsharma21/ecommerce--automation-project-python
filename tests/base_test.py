# import libraries
import pytest


@pytest.mark.usefixtures("browser_setup")
class BaseTest:
    pass
