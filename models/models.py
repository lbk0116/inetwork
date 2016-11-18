# -*- coding: utf-8 -*-
##############################################################################
#
#    Change automatic
#    Copyright (C) 2016-2017 Nantian.
#
#
#
##############################################################################
from openerp import models , fields, api
import re
from IPy import IP
import json,sys
import urllib2,requests
import cookielib
from urllib import urlencode
import os
class network_equipment(models.Model):
    _name = 'inetwork.ne'

    name = fields.Char(string=u"设备名称")
    type = fields.Many2one('inetwork.ne_type',string="equipment_type")
    manage_ip = fields.Char(string=u"管理IP")
    account_name = fields.Char(string=u"账户名")
    account_password = fields.Char(string=u"账户密码")
    notes= fields.Text(string=u"说明")
    active = fields.Boolean(string=u"有效",default=True)

    _sql_constraints = [('manage_ip_unique','UNIQUE(manage_ip)',"管理IP必须唯一！"),]
class ne_type(models.Model):
    _name = 'inetwork.ne_type'

    name = fields.Char(string="类型名称")

