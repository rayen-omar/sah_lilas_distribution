from odoo import models, api

class AccountMove(models.Model):
    _name = 'account.move'
    _inherit = ['account.move', 'sah.totals.mixin']

    _sah_lines_field = 'invoice_line_ids'
    _sah_qty_field = 'quantity'

    @api.depends('invoice_line_ids.discount', 'invoice_line_ids.price_unit', 'invoice_line_ids.quantity', 'amount_untaxed')
    def _compute_sah_totals(self):
        super()._compute_sah_totals()
