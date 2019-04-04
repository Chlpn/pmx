# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def action_register_payment(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Register Payment',
            'view_mode': 'form',
            'view_type': 'form',
            'res_model': 'register.payment',
            'target': 'new',
            'context': 'None'
        }
class RegisterPayment(models.Model):
    _name = 'register.payment'

    @api.multi
    def _get_default_ref(self):
        invoice_obj = self.env['account.invoice'].browse(self.env.context.get('active_ids'))
        ref = ""
        for inv in invoice_obj:
            ref = ref + inv.number + " "
        return ref

    @api.multi
    def _get_default_amt(self):
        invoice_obj = self.env['account.invoice'].browse(self.env.context.get('active_ids'))
        amt = 0
        for inv in invoice_obj:
            amt = amt + inv.residual
        return amt

    journal_id = fields.Many2one('account.journal', string="Journal", domain=[('cash_journal', '=', True)])
    payment_method = fields.Selection([('cash', 'Cash'),
                                       ('cheque', 'Cheque'),
                                       ('transfer', 'Transfer')],
                                      required=True, default='cash')
    ref = fields.Char('Description', default=_get_default_ref)
    amount = fields.Float('Payment Amount', default=_get_default_amt, required=True)
    payment_date = fields.Date(string='Payment Date', default=fields.Date.context_today, required=True)
    move_id = fields.Many2one('account.move', string='Journal Entry',
                              readonly=True, index=True, ondelete='restrict', copy=False,
                              help="Link to the automatically generated Journal Items.")


    @api.multi
    def register_payment(self):
        invoice_objs = self.env['account.invoice'].browse(self.env.context.get('active_ids'))
        parters = []
        for inv in invoice_objs:
            if inv.partner_id not in parters:
                parters.append(inv.partner_id)
            if len(parters) >1:
                raise UserError(_('If you are selecting multiple invoices for payment, all those must belongs to same partner.'))
            if inv.state != 'open':
                raise UserError(_('You can only register payment for invoices in open state.'))
        invoice_obj = self.env['account.invoice'].browse(self.env.context.get('active_id'))
        if self.amount <= 0:
            raise UserError(_('Amount must be greater than zero !!!'))
        if invoice_obj.type == 'in_invoice':
            if self.payment_method == 'cash':
                view_id = self.env.ref('advanced_accounting.payment_voucher_form').id
                context = {
                    'default_journal_id': self.journal_id.id,
                    'default_transaction_date': self.payment_date,
                    'default_description': self.ref,
                    'default_partner_id': invoice_obj.partner_id.id,
                    'default_account_id': invoice_obj.account_id.id,
                    'default_amount': self.amount,
                    'default_move_id': invoice_obj.move_id.id,
                }
                return {
                    'name': 'Cash Payment Voucher',
                    'view_type': 'form',
                    'view_mode': 'tree',
                    'views': [(view_id, 'form')],
                    'res_model': 'payment.voucher',
                    'view_id': view_id,
                    'type': 'ir.actions.act_window',
                    'context': context,
                }
            elif self.payment_method == 'cheque':
                view_id = self.env.ref('cheque_management.issue_cheque_form').id
                context = {
                    'default_date_issue': self.payment_date,
                    'default_partner_id': invoice_obj.partner_id.id,
                    'default_dest_account_id': invoice_obj.account_id.id,
                    'default_amount': self.amount,
                    'default_move_id': invoice_obj.move_id.id,
                }
                return {
                    'name': 'Print Cheque',
                    'view_type': 'form',
                    'view_mode': 'tree',
                    'views': [(view_id, 'form')],
                    'res_model': 'issue.cheque',
                    'view_id': view_id,
                    'type': 'ir.actions.act_window',
                    'context': context,
                }
            else :
                view_id = self.env.ref('advanced_accounting.fund_transfer_form').id
                context = {
                    'default_journal_id': self.journal_id.id,
                    'default_type': 'out',
                    'default_transaction_date': self.payment_date,
                    'default_description': self.ref,
                    'default_partner_id': invoice_obj.partner_id.id,
                    'default_account_id': invoice_obj.account_id.id,
                    'default_amount': self.amount,
                    'default_move_id': invoice_obj.move_id.id,
                }
                return {
                    'name': 'Outward Fund Transfer Form',
                    'view_type': 'form',
                    'view_mode': 'tree',
                    'views': [(view_id, 'form')],
                    'res_model': 'fund.transfer',
                    'view_id': view_id,
                    'type': 'ir.actions.act_window',
                    'context': context,
                }


        if invoice_obj.type == 'out_invoice':
            if self.payment_method == 'cash':
                view_id = self.env.ref('advanced_accounting.receipt_voucher_form').id
                context = {
                    'default_journal_id': self.journal_id.id,
                    'default_transaction_date': self.payment_date,
                    'default_description': self.ref,
                    'default_partner_id': invoice_obj.partner_id.id,
                    'default_account_id': invoice_obj.account_id.id,
                    'default_amount': self.amount,
                    'default_move_id': invoice_obj.move_id.id,
                }
                return {
                    'name': 'Cash Receipt Voucher',
                    'view_type': 'form',
                    'view_mode': 'tree',
                    'views': [(view_id, 'form')],
                    'res_model': 'receipt.voucher',
                    'view_id': view_id,
                    'type': 'ir.actions.act_window',
                    'context': context,
                }
            elif self.payment_method == 'cheque':
                view_id = self.env.ref('cheque_management.wizard_receive_view_pdf').id
                context = {
                    'default_received_date': self.payment_date,
                    'default_partner_id': invoice_obj.partner_id.id,
                    'default_partner_account_id': invoice_obj.account_id.id,
                    'default_amount': self.amount,
                    'default_move_id': invoice_obj.move_id.id,
                }
                return {
                    'name': 'Receive A Cheque',
                    'view_type': 'form',
                    'view_mode': 'tree',
                    'views': [(view_id, 'form')],
                    'res_model': 'receive.cheque2',
                    'view_id': view_id,
                    'type': 'ir.actions.act_window',
                    'context': context,
                    'target': 'new'
                }
            else :
                view_id = self.env.ref('advanced_accounting.fund_transfer_form').id
                context = {
                    'default_journal_id': self.journal_id.id,
                    'default_type': 'in',
                    'default_transaction_date': self.payment_date,
                    'default_description': self.ref,
                    'default_partner_id': invoice_obj.partner_id.id,
                    'default_account_id': invoice_obj.account_id.id,
                    'default_amount': self.amount,
                    'default_move_id': invoice_obj.move_id.id,
                }
                return {
                    'name': 'Inward Fund Transfer',
                    'view_type': 'form',
                    'view_mode': 'tree',
                    'views': [(view_id, 'form')],
                    'res_model': 'fund.transfer',
                    'view_id': view_id,
                    'type': 'ir.actions.act_window',
                    'context': context,
                }

    ##@api.multi
    ##def register_payment(self, payment_line, writeoff_acc_id=False, writeoff_journal_id=False):
        ##""" Reconcile payable/receivable lines from the invoice with payment_line """
        ##line_to_reconcile = self.env['account.move.line']
        ##for inv in self:
            ##line_to_reconcile += inv.move_id.line_ids.filtered(
                ##lambda r: not r.reconciled and r.account_id.internal_type in ('payable', 'receivable'))
        ##return (line_to_reconcile + payment_line).reconcile(writeoff_acc_id, writeoff_journal_id)