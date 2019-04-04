# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    cash_journal = fields.Boolean('Cash Journal ?')
