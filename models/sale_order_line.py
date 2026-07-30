# -*- coding: utf-8 -*-
from odoo import api, models

class SaleOrderLine(models.Model):
    _name = 'sale.order.line'
    _inherit = ['sale.order.line', 'sah.packaging.mixin']

    @api.depends('product_uom_qty', 'product_uom_id', 'price_unit', 'product_id')
    def _compute_sah_packaging_values(self):
        super()._compute_sah_packaging_values()
