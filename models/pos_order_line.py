# -*- coding: utf-8 -*-
from odoo import api, fields, models

class PosOrderLine(models.Model):
    _name = 'pos.order.line'
    _inherit = ['pos.order.line', 'sah.packaging.mixin']

    sah_uom_id = fields.Many2one(
        'uom.uom',
        string="Unité (POS)",
        help="Unité choisie dans le Point de Vente"
    )

    def _sah_get_qty_uom_price(self):
        self.ensure_one()
        # In POS, product_uom_id doesn't exist natively. We use our custom sah_uom_id if set,
        # otherwise we fallback to the product's base uom
        uom = self.sah_uom_id if self.sah_uom_id else self.product_id.uom_id
        return self.qty, uom, self.price_unit, self.product_id
