# coding: utf-8

"""
    Modelmetry API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from modelmetry.openapi.models.check_payload_request_body import CheckPayloadRequestBody

class TestCheckPayloadRequestBody(unittest.TestCase):
    """CheckPayloadRequestBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CheckPayloadRequestBody:
        """Test CheckPayloadRequestBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CheckPayloadRequestBody`
        """
        model = CheckPayloadRequestBody()
        if include_optional:
            return CheckPayloadRequestBody(
                var_schema = '',
                guardrail_id = '',
                payload = modelmetry.openapi.models.payload.Payload(
                    completion = {
                        'key' : null
                        }, ),
                tenant_id = ''
            )
        else:
            return CheckPayloadRequestBody(
                guardrail_id = '',
                payload = modelmetry.openapi.models.payload.Payload(
                    completion = {
                        'key' : null
                        }, ),
        )
        """

    def testCheckPayloadRequestBody(self):
        """Test CheckPayloadRequestBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
