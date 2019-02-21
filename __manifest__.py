# -*- coding: utf-8 -*-
{
    'name': "Hospital",

    'summary': """
        Modulo de Gestión de Hospital para Odoo 11
        """,

    'description': """
        Modulo de Gestíon de hospitales , medicos , personas , enfermedades , historiales , visitas...
    """,

    'author': "Gonzalo García Navarro",
    'website': "http://www.copernic.cat",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Employees',
    'version': '0.7',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hospital_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}