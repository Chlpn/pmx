# -*- coding: utf-8 -*-

from odoo import fields,models


class InvoiceFields(models.Model):
    _inherit = "account.invoice"

    grn = fields.Char(string='GRN Number')



