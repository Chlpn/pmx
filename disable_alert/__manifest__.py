# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Disable stock alert on quotation',
    'version': '2.0',
    'category': 'sale',
    'complexity': 'easy',
    'website': '',
    'description': """While create a quotation for customer in sales module. system has an alert if stock not available,This module disable this alert when we select the product and the quantity (both alerts to be disabled)""",
    'depends': ['sale_stock'],
    'data': [
    ],
    'author':'iSquare Informatics',
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
