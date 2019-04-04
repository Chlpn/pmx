# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Po and do fix',
    'version': '2.0',
    'category': 'sale',
    'complexity': 'easy',
    'website': '',
    'description': """Po and do fix""",
    'depends': ['purchase'],
    'data': ['views/sale_order.xml',
    'views/account_invoice.xml',
    'views/stock_picking.xml'
    ],
    'author':'iSquare Informatics',
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
