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

    _sah_qty_field = 'qty'
    _sah_uom_field = 'sah_actual_uom_id'

    sah_actual_uom_id = fields.Many2one('uom.uom', compute='_compute_sah_actual_uom_id')

    @api.depends('sah_uom_id', 'product_id.uom_id')
    def _compute_sah_actual_uom_id(self):
        for record in self:
            record.sah_actual_uom_id = record.sah_uom_id or record.product_id.uom_id

    @api.depends('qty', 'sah_actual_uom_id', 'price_unit', 'product_id')
    def _compute_sah_packaging_values(self):
        super()._compute_sah_packaging_values()
