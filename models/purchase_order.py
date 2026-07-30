from odoo import models, api

class PurchaseOrder(models.Model):
    _name = 'purchase.order'
    _inherit = ['purchase.order', 'sah.totals.mixin']

    _sah_lines_field = 'order_line'
    _sah_qty_field = 'product_qty'

    @api.depends('order_line.discount', 'order_line.price_unit', 'order_line.product_qty', 'amount_untaxed')
    def _compute_sah_totals(self):
        super()._compute_sah_totals()
