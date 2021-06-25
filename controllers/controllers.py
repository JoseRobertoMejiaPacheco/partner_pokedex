# -*- coding: utf-8 -*-
from odoo import http

# class PartnerPokedex(http.Controller):
#     @http.route('/partner_pokedex/partner_pokedex/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_pokedex/partner_pokedex/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_pokedex.listing', {
#             'root': '/partner_pokedex/partner_pokedex',
#             'objects': http.request.env['partner_pokedex.partner_pokedex'].search([]),
#         })

#     @http.route('/partner_pokedex/partner_pokedex/objects/<model("partner_pokedex.partner_pokedex"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_pokedex.object', {
#             'object': obj
#         })