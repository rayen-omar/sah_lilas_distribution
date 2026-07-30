# -*- coding: utf-8 -*-
from odoo import api, models

class PurchaseOrderLine(models.Model):
    _name = 'purchase.order.line'
    _inherit = ['purchase.order.line', 'sah.packaging.mixin']

    _sah_qty_field = 'product_qty'

    @api.depends('product_qty', 'product_uom_id', 'price_unit', 'product_id')
    def _compute_sah_packaging_values(self):
        super()._compute_sah_packaging_values()
