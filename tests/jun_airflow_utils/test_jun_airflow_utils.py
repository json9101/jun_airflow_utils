import sys
import jun_airflow_utils


def test_ping():
    sys.argv = ['foo', '10']
    jun_airflow_utils.ping()

