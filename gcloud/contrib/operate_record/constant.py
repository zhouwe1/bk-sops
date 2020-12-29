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

from django.utils.translation import ugettext_lazy as _

TASK_OPERATE_TYPE = [
    # 任务操作
    ("none", "None"),
    ("create", _("创建")),
    ("task_clone", _("克隆(创建)")),
    ("delete", _("删除")),
    ("start", _("执行")),
    ("pause", _("暂停")),
    ("resume", _("继续")),
    ("revoke", _("撤消")),
    ("delete", _("删除")),
    ("update", _("修改")),
    # 任务节点操作
    ("retry", _("重试")),
    ("skip", _("跳过")),
    ("skip_exg", _("跳过失败网关")),
    ("pause_subproc", _("暂停节点")),
    ("resume_subproc", _("继续节点")),
    ("forced_fail", _("强制失败")),
    ("update", _("修改")),
    ("spec_nodes_timer_reset", _("调整时间")),
]


TEMPLATE_OPERATE_TYPE = [
    ("none", "None"),
    ("create", _("创建")),
    ("delete", _("删除")),
    ("update", _("修改")),
]

RECORD_TYPE = {
    "task": _("任务实例"),
    "task_node": _("任务节点"),
    "template": _("项目模版"),
    "common_template": _("公共模版"),
}

TASK_OPERATE_SOURCE = [
    ("app", _("app 页面")),
    ("api", _("api 接口")),
]

# 任务引用的流程模板来源
TEMPLATE_SOURCE = [
    ("project", _("项目流程")),
    ("common", _("公共流程")),
    ("onetime", _("一次性任务")),
]
