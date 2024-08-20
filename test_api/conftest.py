import yaml
import pytest

@pytest.fixture
def load_data(file='./config.yaml'):
    with open(file) as f:
        return yaml.safe_load(f)
    