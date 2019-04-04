# -*- coding: utf-8 -*-
from openerp import api, fields, models, _
    
class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    type = fields.Selection([
        ('service', _('Service'))], string='Product Type', default='service', required=True,
        help='A service is a non-material product you provide.\n'
             'A digital content is a non-material product you sell online. The files attached to the products are the one that are sold on '
             'the e-commerce such as e-books, music, pictures,... The "Digital Product" module has to be installed.')    