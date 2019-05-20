# -*- coding: utf-8 -*-
{
    'name': 'Packet Host: Stock Customization',
    'summary': 'Packet Host : Warehouse Filter on Transfers',
    'description':"""
    Task ID: 1962968
    1) Warehouse filter on transfers.
    1.1) By Creating a Warehouse filter on transfers, the transfer will only show operation types that apply to that warehouse, simplifying the process and reducing the amount of errors that can be made by the users.
    """,
    'license': 'OEEL-1',
    'author': 'Odoo Inc',
    'version': '0.1',
    'depends': ['stock'],
    'data': [
        'views/stock_picking_views.xml',
    ],
}
