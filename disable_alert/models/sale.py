# -*- coding: utf-8 -*-
from openerp import api, fields, models, _

class sale_order_line(models.Model):
    _inherit = "sale.order.line"    
    
    @api.onchange('product_uom_qty', 'product_uom', 'route_id')
    def _onchange_product_id_check_availability(self):
        if not self.product_id or not self.product_uom_qty or not self.product_uom:
            self.product_packaging = False
            return {}
        if self.product_id.type == 'product':
            precision = self.env['decimal.precision'].precision_get('Product Unit of Measure')
            product_qty = self.product_uom._compute_quantity(self.product_uom_qty, self.product_id.uom_id)
          
        return {}