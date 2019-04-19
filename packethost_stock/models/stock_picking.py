# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    show_on_picking = fields.Boolean('Show on Picking')
    no_show_location_on_picking = fields.Boolean('Not Show Selectable Source Location on Picking',
                                                 help='When this box is checked, '
                                                      'source location for this operation type will not show as '
                                                      'a dropdown selectable option on transfer form, '
                                                      'but will be logged in the chatter.')
    no_show_location_dest_on_picking = fields.Boolean('Not Show Selectable Destination Location on Picking',
                                                      help='When this box is checked, '
                                                      'destination location for this operation type will not show as '
                                                      'a dropdown selectable option on transfer form, '
                                                      'but will be logged in the chatter.')


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    warehouse_id = fields.Many2one('stock.warehouse', ondelete='set null', string='Warehouse')
    no_show_location_on_picking = fields.Boolean(related='picking_type_id.no_show_location_on_picking', readonly=True)
    no_show_location_dest_on_picking = fields.Boolean(related='picking_type_id.no_show_location_dest_on_picking', readonly=True)

    location_id = fields.Many2one('stock.location', track_visibility='onchange')
    location_dest_id = fields.Many2one('stock.location', track_visibility='onchange')
