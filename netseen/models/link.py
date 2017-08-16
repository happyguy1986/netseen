# Copyright 2015-2017 Cisco Systems, Inc.
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from sqlalchemy import Column, Integer, Float

from netseen.models.table import Table


class Link(Table):
    '''
    router tables
    '''

    __tablename__ = 'Link'
    link_local_ipv4_int = Column(
        Integer, primary_key=True, nullable=False, unique=False)
    link_remote_ipv4 = Column(
        Integer, primary_key=True, nullable=False, unique=False)
    adj_segment_id = Column(Integer, nullable=True)
    metric_igp = Column(Integer, nullable=True)
    metric_te = Column(Integer, nullable=True)
    max_bandwidth = Column(Float, nullable=True)
    max_rsv_bandwidth = Column(Float, nullable=True)
