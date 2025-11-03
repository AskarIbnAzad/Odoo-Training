from odoo import models, fields

class EstatePropertyOffers(models.Model):
    _name = 'estate.property.offers'
    _description= 'Estate Property Offers'

    price=fields.Float(string='Price')
    status = fields.Selection(
        selection=[
            ('refused', 'Refused'),
            ('accepted', 'Accepted')
        ],
        string='Status',
        copy=False
    )
    partner_id=fields.Many2one('res.partner', string='Partner',required=True)
    property_id=fields.Many2one('estate.property', string='Property',required=True)