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
            # Jumper
            "website_game/static/src/game/UE4Game/myproject1html/Build/myproject1html.data",
            "website_game/static/src/game/UE4Game/myproject1html/Build/myproject1html.framework.js",
            "website_game/static/src/game/UE4Game/myproject1html/Build/myproject1html.loader.js",
            "website_game/static/src/game/UE4Game/myproject1html/Build/myproject1html.wasm",
            "website_game/static/src/game/UE4Game/myproject1html/TemplateData/favicon.ico",
            "website_game/static/src/game/UE4Game/myproject1html/TemplateData/fullscreen-button.png",
            "website_game/static/src/game/UE4Game/myproject1html/TemplateData/progress-bar-empty-dark.png",
            "website_game/static/src/game/UE4Game/myproject1html/TemplateData/progress-bar-empty-light.png",
            "website_game/static/src/game/UE4Game/myproject1html/TemplateData/progress-bar-full-dark.png",
            "website_game/static/src/game/UE4Game/myproject1html/TemplateData/progress-bar-full-light.png",
            "website_game/static/src/game/UE4Game/myproject1html/TemplateData/style.css",
            "website_game/static/src/game/UE4Game/myproject1html/TemplateData/unity-logo-dark.png",
            "website_game/static/src/game/UE4Game/myproject1html/TemplateData/unity-logo-light.png",
            "website_game/static/src/game/UE4Game/myproject1html/TemplateData/webgl-logo.png",
            # FlappyBird
            "website_game/static/src/game/UE4Game/FlappyBirdGames/TemplateData/favicon.ico",
            "website_game/static/src/game/UE4Game/FlappyBirdGames/TemplateData/fullscreen-button.png",
            "website_game/static/src/game/UE4Game/FlappyBirdGames/TemplateData/progress-bar-empty-dark.png",
            "website_game/static/src/game/UE4Game/FlappyBirdGames/TemplateData/progress-bar-empty-light.png",
            "website_game/static/src/game/UE4Game/FlappyBirdGames/TemplateData/progress-bar-full-dark.png",
            "website_game/static/src/game/UE4Game/FlappyBirdGames/TemplateData/progress-bar-full-light.png",
            "website_game/static/src/game/UE4Game/FlappyBirdGames/TemplateData/style.css",
            "website_game/static/src/game/UE4Game/FlappyBirdGames/TemplateData/unity-logo-dark.png",
            "website_game/static/src/game/UE4Game/FlappyBirdGames/TemplateData/unity-logo-light.png",
            "website_game/static/src/game/UE4Game/FlappyBirdGames/TemplateData/webgl-logo.png",
            "website_game/static/src/game/UE4Game/FlappyBirdGames/Build/FlappyBirdGames.data",
            "website_game/static/src/game/UE4Game/FlappyBirdGames/Build/FlappyBirdGames.framework.js",
            "website_game/static/src/game/UE4Game/FlappyBirdGames/Build/FlappyBirdGames.loader.js",
            "website_game/static/src/game/UE4Game/FlappyBirdGames/Build/FlappyBirdGames.wasm",

            

       
        ]
    },
}
