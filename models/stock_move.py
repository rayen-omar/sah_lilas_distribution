# -*- coding: utf-8 -*-
from odoo import api, fields, models

class StockMove(models.Model):
    _name = 'stock.move'
    _inherit = ['stock.move', 'sah.packaging.mixin']

    # Dans un mouvement de stock on priorise la quantité sélectionnée.
    # Pour simplifier avec le mixin, on peut utiliser product_uom_qty par défaut
    # car 'quantity' est souvent le fallback
    _sah_qty_field = 'sah_actual_qty'

    sah_actual_qty = fields.Float(compute='_compute_sah_actual_qty')

    @api.depends('product_uom_qty', 'quantity')
    def _compute_sah_actual_qty(self):
        for record in self:
            record.sah_actual_qty = record.quantity if ('quantity' in record._fields and record.quantity) else record.product_uom_qty

    @api.depends('sah_actual_qty', 'product_uom', 'product_id')
    def _compute_sah_packaging_values(self):
        super()._compute_sah_packaging_values()
