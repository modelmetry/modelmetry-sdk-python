# coding: utf-8

"""
    Modelmetry API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from modelmetry.openapi.models.metric_value import MetricValue

class TestMetricValue(unittest.TestCase):
    """MetricValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MetricValue:
        """Test MetricValue
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetricValue`
        """
        model = MetricValue()
        if include_optional:
            return MetricValue(
                key = '',
                value = 1.337
            )
        else:
            return MetricValue(
                key = '',
                value = 1.337,
        )
        """

    def testMetricValue(self):
        """Test MetricValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()