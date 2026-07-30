# -*- coding: utf-8 -*-
from odoo import api, models

class AccountMoveLine(models.Model):
    _name = 'account.move.line'
    _inherit = ['account.move.line', 'sah.packaging.mixin']

    _sah_qty_field = 'quantity'

    @api.depends('quantity', 'product_uom_id', 'price_unit', 'product_id')
    def _compute_sah_packaging_values(self):
        super()._compute_sah_packaging_values()
