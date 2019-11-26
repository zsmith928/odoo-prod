# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Candidroot Solutions Pvt. Ltd.
# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    aftership_tracking_id = fields.Many2one('aftership.tracking', 'Tracking ID', copy=False,readonly=True)
    aftership_state = fields.Selection(related="aftership_tracking_id.state", string="Aftership Status")
    tracking_no_vendor = fields.Char("Vendor Tracking Number", copy=False)