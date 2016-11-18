# -*- coding: utf-8 -*-
{
    'name': "inetwork",

    'summary': """
        An automatic manage app""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Nantian",
    'website': 'https://www.nantian.com.cn',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Inetwork',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/view.xml',
        'views/menu.xml',
        # 'security/ir.model.access.csv',
        # 'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}