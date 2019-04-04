# -*- coding: utf-8 -*-
from openerp import api, fields, models, _

class account_invoice(models.Model):
    _inherit = "account.invoice"  
    

    po_number=fields.Char('Po number')
    do_number_invoiced = fields.Many2many('stock.picking', 'account_invoice_do_num_pick', string='Do Number Invoiceds',readonly=True)
    
    
    
    @api.multi
    def action_invoice_open(self):
        # lots of duplicate calls to action_invoice_open, so we remove those already open
        sale_order_obj=self.env['sale.order']
        sale_id=sale_order_obj.search([('name','=',self.origin)])
        if len(sale_id):
            print'--------------------------------------',sale_id[0].do_number
#            sale_id[0].write({'do_number_invoiced': sale_id[0].do_number})

#            sale_id[0].write({'do_number_invoiced': [(4,self.id)]})
#            sale_id[0].write({'do_number_invoiced': [(6,0, [self.id])]})
            
            print'hhhhhwritehhhhhhhhhhhh',sale_id[0].do_number
            for  m in   sale_id[0].do_number:
                self.write({'po_number':sale_id[0].po_number,'do_number_invoiced':[(4,m.id)]})
                sale_id[0].write({'do_number':[(3,m.id)],'do_number_invoiced':[(4,m.id)]})

        to_open_invoices = self.filtered(lambda inv: inv.state != 'open')
        if to_open_invoices.filtered(lambda inv: inv.state not in ['proforma2', 'draft']):
            raise UserError(_("Invoice must be in draft or Pro-forma state in order to validate it."))
        to_open_invoices.action_date_assign()
        to_open_invoices.action_move_create()
        return to_open_invoices.invoice_validate()