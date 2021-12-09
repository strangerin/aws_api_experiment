from pprint import pprint
import unittest
import boto3  # AWS SDK for Python
from botocore.exceptions import ClientError
from moto import mock_dynamodb2


@mock_dynamodb2
class TestDatabaseFunctions(unittest.TestCase):
    def setUp(self):
        """
        Create database resource and mock table
        """
        from create_mock_event_table import create_event_table
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
        self.table = create_event_table(self.dynamodb)

    def tearDown(self):
        """
        Delete database resource and mock table
        """
        self.table.delete()
        self.dynamodb = None

    def test_table_exists(self):
        """
        Test if our mock table is ready
        """
        def test_table_exists(self):
            self.assertIn('events', self.table.name)


if __name__ == '__main__':
    unittest.main()