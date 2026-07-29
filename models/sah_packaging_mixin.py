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
        digits='Product Price'
    )

    def _sah_get_qty_uom_price(self):
        """
        Méthode abstraite à surcharger par les modèles héritant de ce mixin.
        Doit retourner un tuple: (qty, uom, price_unit, product)
        """
        self.ensure_one()
        return (0.0, self.env['uom.uom'], 0.0, self.env['product.product'])

    @api.depends_context('lang')
    def _compute_sah_packaging_values(self):
        for record in self:
            # Valeurs par défaut
            record.sah_qty_unit = 0.0
            record.sah_price_unit = 0.0

            # Gestion des lignes section/note (display_type)
            if 'display_type' in record._fields and record.display_type:
                continue

            # Récupération des données via la méthode abstraite
            try:
                qty, uom, price_unit, product = record._sah_get_qty_uom_price()
            except Exception:
                continue

            if not product or not product.uom_id or not uom:
                continue

            # sah_qty_unit: quantité convertie de l'unité de la ligne vers l'unité de base du produit
            qty_unit = uom._compute_quantity(qty, product.uom_id, round=False)
            record.sah_qty_unit = qty_unit

            # sah_price_unit: prix unitaire de la ligne converti vers le prix à l'unité de base du produit
            # Si uom > product.uom_id (ex: Carton de 10 > Unité) -> le prix unitaire doit être divisé
            # Odoo _compute_price fait ça: uom._compute_price(price_unit, product.uom_id)
            if hasattr(uom, '_compute_price'):
                record.sah_price_unit = uom._compute_price(price_unit, product.uom_id)
            else:
                # Fallback manuel si _compute_price n'existe plus (bien qu'il existe normalement)
                qty_ratio = uom._compute_quantity(1.0, product.uom_id, round=False)
                if qty_ratio:
                    record.sah_price_unit = price_unit / qty_ratio
