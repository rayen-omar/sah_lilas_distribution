# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SahTotalsMixin(models.AbstractModel):
    _name = 'sah.totals.mixin'
    _description = 'Mixin pour le calcul du FODEC et Remise globale'

    currency_id = fields.Many2one('res.currency', string='Devise')
    sah_total_discount = fields.Monetary(string='Total Remise', compute='_compute_sah_totals', currency_field='currency_id')
    sah_total_fodec = fields.Monetary(string='FODEC (1%)', compute='_compute_sah_totals', currency_field='currency_id')

    # À surcharger dans les modèles enfants
    _sah_lines_field = 'order_line'
    _sah_qty_field = 'product_uom_qty'

    def _compute_sah_totals(self):
        for record in self:
            discount = 0.0
            lines = getattr(record, record._sah_lines_field, [])
            for line in lines:
                # Ignorer les sections et notes si possible
                if 'display_type' in line._fields and line.display_type in ('line_section', 'line_note'):
                    continue

                qty = getattr(line, record._sah_qty_field, 0.0)
                price = getattr(line, 'price_unit', 0.0)
                line_discount = getattr(line, 'discount', 0.0)
                
                discount += (price * qty) * (line_discount / 100.0)
            
            record.sah_total_discount = discount
            record.sah_total_fodec = record.amount_untaxed * 0.01
