from odoo import models, api

class SaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = ['sale.order', 'sah.totals.mixin']

    _sah_lines_field = 'order_line'
    _sah_qty_field = 'product_uom_qty'

    @api.depends('order_line.discount', 'order_line.price_unit', 'order_line.product_uom_qty', 'amount_untaxed')
    def _compute_sah_totals(self):
        super()._compute_sah_totals()
