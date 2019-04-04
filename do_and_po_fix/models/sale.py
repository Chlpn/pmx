# -*- coding: utf-8 -*-
from openerp import api, fields, models, _

class sale_order(models.Model):
    _inherit = "sale.order"  
    

    po_number=fields.Char('Po number')
    do_number = fields.Many2many('stock.picking', 'stock_picking_do_num', string='Do Number',readonly=True)
    do_number_invoiced = fields.Many2many('stock.picking', 'account_invoice_do_num_stock_picking', string='Do Number Invoiced',readonly=True)

        
        

    