# -*- coding: utf-8 -*-
{
    'name': "Pokedex",

    'summary': """
        Curso de desarrollo Odoo (Pokedex)""",

    'description': """
        Long description of module's purpose
    """,

    'author': "José Roberto Mejía Pacheco",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/partner_pokedex_pokedex_views.xml',
        'views/res_partner_views.xml',
        'wizard/evolve_pokemon.xml',
        'views/partner_pokedex_menu_views.xml'
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}