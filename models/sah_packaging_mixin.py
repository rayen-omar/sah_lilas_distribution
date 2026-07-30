# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SahPackagingMixin(models.AbstractModel):
    _name = 'sah.packaging.mixin'
    _description = 'Mixin pour les quantites en cartons et en unites'

    sah_qty_unit = fields.Float(
        string="Qté Unités",
        compute='_compute_sah_packaging_values',
        store=False,
        digits='Product Unit of Measure'
    )
    sah_price_unit = fields.Float(
        string="PU Unité",
        compute='_compute_sah_packaging_values',
        store=False,
        readonly=False,
        digits='Product Price'
    )

    # Propriétés de mapping par défaut (à surcharger dans les modèles enfants si nécessaire)
    _sah_qty_field = 'product_uom_qty'
    _sah_uom_field = 'product_uom_id'
    _sah_price_field = 'price_unit'

    # Note: Le décorateur @api.depends est défini dans les modèles enfants
    def _compute_sah_packaging_values(self):
        for record in self:
            record.sah_qty_unit = 0.0
            record.sah_price_unit = 0.0

            if 'display_type' in record._fields and record.display_type in ('line_section', 'line_note'):
                continue

            product = record.product_id
            if not product:
                continue

            qty = getattr(record, record._sah_qty_field, 0.0)
            uom = getattr(record, record._sah_uom_field, False)
            price = getattr(record, record._sah_price_field, 0.0)

            if not uom or not product.uom_id:
                continue

            # Conversion de la quantité
            record.sah_qty_unit = uom._compute_quantity(qty, product.uom_id, round=False)

            # Conversion du prix unitaire
            if hasattr(uom, '_compute_price'):
                record.sah_price_unit = uom._compute_price(price, product.uom_id)
            else:
                qty_ratio = uom._compute_quantity(1.0, product.uom_id, round=False)
                if qty_ratio:
                    record.sah_price_unit = price / qty_ratio
