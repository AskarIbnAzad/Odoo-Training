from odoo import fields, models

class EstatePropertyTags(models.Model):
    _name= 'estate.property.tags'
    _description= 'EstatevProperty Tags'

    name= fields.Char('Name', required=True)