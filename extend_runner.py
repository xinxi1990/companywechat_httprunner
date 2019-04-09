#!/usr/bin/env python
# -*- coding: utf-8 -*-


from httprunner.api import HttpRunner
runner = HttpRunner(failfast=False)
runner.run('v1/testcases/test_department/test_list_department.yaml')
print(runner.summary)
runner.gen_html_report(
    html_report_name="demo",
    html_report_template="/path/to/custom_report_template"
)
