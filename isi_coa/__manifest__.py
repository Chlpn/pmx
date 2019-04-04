# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2014 Tech Receptives (<http://techreceptives.com>)

{
    'name': 'iSquare Informatics - COA',
    'author': 'iSquare Informatics',
    'website': 'http://www.isi.ae',
    'category': 'Localization',
    'description': """
General Purpose chart of Account.
=======================================================

    """,
    'depends': ['base', 'account'],
    'data': [
             'data/l10n_ae_chart_data.xml',
             'data/account_chart_template_data.yml',
    ],
}
