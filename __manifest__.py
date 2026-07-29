# -*- coding: utf-8 -*-
{
    'name': 'SAH Packaging Qty',
    'version': '19.0.1.0.0',
    'summary': 'Affichage des quantités en cartons et en unités',
    'description': """
        Ce module affiche simultanément la quantité en cartons et en unités sur toutes les
        lignes de documents, quelle que soit l'unité de saisie. Module purement visuel.
    """,
    'category': 'Hidden',
    'author': 'BenAmor',
    'website': '',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'product',
        'uom',
        'purchase',
        'sale_management',
        'stock',
        'account',
        'point_of_sale',
    ],
    'data': [
        'views/purchase_order_views.xml',
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
        'views/account_move_views.xml',
        'views/pos_order_views.xml',
        'report/purchase_report_templates.xml',
        'report/stock_report_templates.xml',
        'report/account_report_templates.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'sah_packaging_qty/static/src/app/models/*.js',
            'sah_packaging_qty/static/src/app/components/**/*',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}
