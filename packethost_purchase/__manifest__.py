# -*- coding: utf-8 -*-
{
    'name': 'Packet Host: Purchase Customization',
    'summary': 'Packet Host : RFQ Product Lines on Email Template',
    'description':"""
    Task ID: 1966636
    New email template to send RFQs should include product lines with the following information:
    - "Notes" (x_studio_notes): Studio field on RFQ
    - "Delivery Location" (picking_type_id.warehouse_id): Stock location where the products would be received
    - "Vendor" (partner_id)
    - RFQ Lines:
      - "Product name 1" x "Quantity of product 1"
      - "Product name 2" x "Quantity of product 2"
      - "Product name 3" x "Quantity of product 3"
    """,
    'license': 'OEEL-1',
    'author': 'Odoo Inc',
    'version': '0.1',
    'depends': ['purchase', 'mail'],
    'data': [
        'data/mail_template_data.xml',
    ],
}
