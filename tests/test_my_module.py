import pytest
from src.my_package import my_module


class TestMyModule:
    def test_prints_hello_world(self):
        result = my_module.hello_world().unwrap()
        assert result == "Hello world!"
