from odoo import fields, models
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name="estate.property"
    _description= "all peroperties of an estate"

    name=fields.Char('Property Name', required=True)
    description= fields.Text('Description')
    postcode= fields.Char('Postcode')
    date_availability= fields.Date('Date Availability', copy=False,default=fields.date.today()+ relativedelta(months=3))
    expected_price= fields.Float('Expected Price', required=True)
    selling_price= fields.Float('Selling Price', readonly=True,copy=False)
    bedrooms= fields.Integer('Bedrooms', default=2)
    living_area= fields.Integer('Living Area')
    facades= fields.Integer('Facades')
    garage= fields.Boolean('Garage')
    garden= fields.Boolean('Garden')
    garden_area= fields.Integer('Garden Area')
    garden_orientation = fields.Selection(
        selection=[
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West')
        ],
        string='Garden Orientation'
    )
    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('offer received', 'Offer Received'),
            ('offer accepted', 'Offer Accepted'),
            ('sold ', 'Sold'),
            ('cancelled ', 'Cancelled')
        ],
        string='State',
        default='new',
        copy=False,
        required=True
    )
    active= fields.Boolean(default=True)
    estate_property_type_id= fields.Many2one('esate.property.type', string='Property Type')
    buyer_id= fields.Many2one('res.partner', string='Buyer')
    salesman_id= fields.Many2one('res.users', string='Salesperson', index=True, tracking=True, default=lambda self: self.env.user)
    tag_ids=fields.Many2many('estate.property.tags', string='Tags')
    offer_ids=fields.One2many('estate.property.offers', "property_id", string='Offers')

