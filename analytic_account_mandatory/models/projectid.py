from odoo import models, fields, api
from odoo.exceptions import UserError


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.multi
    def action_confirm(self):
        if not self.project_id:
            raise UserError('Analytic Account Not Found!!!')
        confirm = super(SaleOrder, self).action_confirm()
        return confirm





