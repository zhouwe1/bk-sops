# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2020 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
from django.test import TestCase
from gcloud.utils.strings import (string_to_boolean, check_and_rename_params, camel_case_to_underscore_naming,
                                  standardize_pipeline_node_name, standardize_name)


class StringTestCase(TestCase):
    def test_string_to_boolean(self):
        self.assertTrue(string_to_boolean("True"))
        self.assertTrue(string_to_boolean("1"))
        self.assertFalse(string_to_boolean("False"))
        self.assertFalse(string_to_boolean("0"))

    def test_check_and_rename_params(self):
        params = [
            [{"project_id": "1"}, "project_id"],
            [{"project_uid": "1"}, "project_uid"],
        ]
        for param in params:
            _result = check_and_rename_params(*param[0])
            self.assertTrue(_result["success"])

    def test_camel_case_to_underscore_naming(self):
        self.assertEqual('user_id', camel_case_to_underscore_naming('UserId'))
        self.assertEqual('user_name', camel_case_to_underscore_naming('UserName'))

    def test_standardize_pipeline_node_name(self):
        self.assertTrue(standardize_pipeline_node_name({"name": "node_1"}))

    def test_standardize_name(self):
        self.assertEqual(standardize_name("node_1", 15), "node_1")
        self.assertEqual(standardize_name("node_(1)", 15), "node_1")
