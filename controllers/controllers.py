# -*- coding: utf-8 -*-
from odoo import http

class WebsiteGame(http.Controller):
    @http.route('/game', auth='public',website=True)
    def index(self, **kw):
        return http.request.render('website_game.game', {})


# class WebsiteGame(http.Controller):
#     @http.route('/website_game/website_game', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_game/website_game/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_game.listing', {
#             'root': '/website_game/website_game',
#             'objects': http.request.env['website_game.website_game'].search([]),
#         })

#     @http.route('/website_game/website_game/objects/<model("website_game.website_game"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_game.object', {
#             'object': obj
#         })
