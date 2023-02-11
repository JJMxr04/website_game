# -*- coding: utf-8 -*-
{
    'name': "website_game",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_frontend': [
            'website_game/static/src/game/UE4Game/HTML5/MyProject4.css',
            'website_game/static/src/game/UE4Game/HTML5/MyProject4.data',
            'website_game/static/src/game/UE4Game/HTML5/MyProject4.data.js',
            'website_game/static/src/game/UE4Game/HTML5/MyProject4.UE4.js',
            'website_game/static/src/game/UE4Game/HTML5/UE4Game.js',
            'website_game/static/src/game/UE4Game/HTML5/Utility.js',
            'website_game/static/src/game/UE4Game/HTML5/UE4Game.wasm',
            'website_game/static/src/game/UE4Game/HTML5/.htaccess'
       
        ]
    },
}
