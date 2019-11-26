# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Candidroot Solutions Pvt. Ltd.
# See LICENSE file for full copyright and licensing details.

{
    'name': "Aftership Integration with Odoo",
    'version': '12.0.1.0',
    'summary': """
        Aftership Integration with Odoo
    """,
    'description': """

Aftership Integration with Odoo
===============================
Aftership Integration with Odoo

Description
-----------
    - This module will allow user to create shipment record in aftership while validating Receipts.

    """,

    'author': "Candidroot Solutions Pvt. Ltd.",
    'website': "https://candidroot.com/",
    'category': 'Payment',
    'depends': ['base_setup', 'purchase_stock'],
    "external_dependencies": {"python": ['aftership'], "bin": []},
    'data': [
            'security/ir.model.access.csv',
            'data/aftership_data.xml',
            'views/country_view.xml',
            'views/res_config_settings_views.xml',
            'views/aftership_config_view.xml',
            'views/stock_picking_view.xml',
            'views/purchase_order_view.xml',
    ],
    'images':  [],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}
