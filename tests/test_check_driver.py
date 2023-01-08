import pytest


class TestClass:
    @pytest.fixture
    def example_fixture(self):
        return 1

    def test_with_fixture(self, driver, logger, example_fixture):
        assert example_fixture == 1
