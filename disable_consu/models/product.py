# -*- coding: utf-8 -*-
from openerp import api, fields, models, _
    
class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    type = fields.Selection([
        ('product', _('Stockable Product')),
        ('service', _('Service'))], string='Product Type', default='product', required=True,
        help='A stockable product is a product for which you manage stock. The "Inventory" app has to be installed.\n'
             'A consumable product, on the other hand, is a product for which stock is not managed.\n'
             'A service is a non-material product you provide.\n'
             'A digital content is a non-material product you sell online. The files attached to the products are the one that are sold on '
             'the e-commerce such as e-books, music, pictures,... The "Digital Product" module has to be installed.')    