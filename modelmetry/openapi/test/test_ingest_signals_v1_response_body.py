# coding: utf-8

"""
    Modelmetry API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from modelmetry.openapi.models.ingest_signals_v1_response_body import IngestSignalsV1ResponseBody

class TestIngestSignalsV1ResponseBody(unittest.TestCase):
    """IngestSignalsV1ResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IngestSignalsV1ResponseBody:
        """Test IngestSignalsV1ResponseBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IngestSignalsV1ResponseBody`
        """
        model = IngestSignalsV1ResponseBody()
        if include_optional:
            return IngestSignalsV1ResponseBody(
                var_schema = ''
            )
        else:
            return IngestSignalsV1ResponseBody(
        )
        """

    def testIngestSignalsV1ResponseBody(self):
        """Test IngestSignalsV1ResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
