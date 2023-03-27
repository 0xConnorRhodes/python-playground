import pytest

from pgbackup import cli # import the cli module in our src to allow these tests to be run on the code it contains

url = "postgres://bob@example.com:5432/db_one"

def test_parser_without_driver():
    """
    Without a specified driver, the parser will exit
    """
    with pytest.raises(SystemExit): # allows the test to pass if the program errors, which is expected in this case
        parser = cli.create_parser() # pulls in the function from src/pgbackup/cli.py and runs it through this test function
        parser.parse_args([url])

def test_parser_with_driver():
    """
    The parser will exit if it receives a driver without a destination
    """
    parser = cli.create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "local"])

def test_parser_with_driver_and_destination():
    """
    The parser will not exit if it receives a driver and destination
    """
    parser = cli.create_parser()

    args = parser.parse_args([url, "--driver", "local", "/some/path"])

    assert args.url == url
    assert args.driver == "local"
    assert args.destination == "/some/path"
