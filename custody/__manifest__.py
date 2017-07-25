{
    'name': "Custody",

    'description': """
      
    """,

    'author': "Mahmoud Elsaka",
    'website': "http://www.elsaka.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','mail'],

    # always loaded
    'data': [
        'security/custody_security.xml',
        'security/ir.model.access.csv',
        'templates.xml',
        'custody_report.xml',
        #'session_workflow.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],

}
# -*- coding: utf-8 -*-
