{
    'name': 'Real Estate Askar',
    'version': '18.0.1.0.0',
    'category': 'Website/eCommerce',
    'summary': 'Adds a "Go To Checkout" button to the cart notification popup.',
    'author': 'Odoo Flash Pro',
    'depends': [
        'base',
    ],
    'data':[
        'security\ir.model.access.csv',
        'views\estate_property_menu.xml',
        'views\estate_property_views.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}