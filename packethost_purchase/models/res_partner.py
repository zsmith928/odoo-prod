# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class Partner(models.Model):
    _inherit = "res.partner"

    street_address = fields.Char(
        compute="_compute_street_address", string="Street Address"
    )

    @api.depends("street", "street2")
    def _compute_street_address(self):
        for partner in self:
            lines = [partner.street, partner.street2]
            lines = list(filter(lambda x: x, lines))
            partner.street_address = "\n".join(lines) if lines else False

