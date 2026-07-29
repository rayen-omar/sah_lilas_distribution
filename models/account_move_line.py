# -*- coding: utf-8 -*-
from odoo import api, models

class AccountMoveLine(models.Model):
    _name = 'account.move.line'
    _inherit = ['account.move.line', 'sah.packaging.mixin']

    def _sah_get_qty_uom_price(self):
        self.ensure_one()
        qty = self.quantity if 'quantity' in self._fields else 0.0
        # Odoo 19: uom est product_uom_id
        uom = self.product_uom_id if 'product_uom_id' in self._fields else self.product_uom
        price_unit = self.price_unit
        product = self.product_id
        return (qty, uom, price_unit, product)

    @api.depends('quantity', 'product_uom_id', 'price_unit', 'product_id')
    def _compute_sah_packaging_values(self):
        super()._compute_sah_packaging_values()
