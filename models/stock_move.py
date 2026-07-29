# -*- coding: utf-8 -*-
from odoo import api, models

class StockMove(models.Model):
    _name = 'stock.move'
    _inherit = ['stock.move', 'sah.packaging.mixin']

    def _sah_get_qty_uom_price(self):
        self.ensure_one()
        # Dans un mouvement de stock, qty peut être quantity (fait) ou product_uom_qty (demande)
        # On priorise quantity si elle est supérieure à 0 ou si on est en train de la saisir, sinon product_uom_qty
        qty = self.quantity if ('quantity' in self._fields and self.quantity) else self.product_uom_qty
        # Odoo 19: uom est product_uom_id ou product_uom
        uom = self.product_uom_id if 'product_uom_id' in self._fields else self.product_uom
        price_unit = 0.0 # Pas de prix sur les mouvements de stock simples par défaut
        product = self.product_id
        return (qty, uom, price_unit, product)

    @api.depends('product_uom_qty', 'quantity', 'product_uom', 'product_id')
    def _compute_sah_packaging_values(self):
        super()._compute_sah_packaging_values()
