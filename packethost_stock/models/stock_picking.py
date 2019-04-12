# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    warehouse_id = fields.Many2one('stock.warehouse', ondelete='set null', string='Warehouse')