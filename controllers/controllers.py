# -*- coding: utf-8 -*-
from odoo import http

# class ShinyChain(http.Controller):
#     @http.route('/shiny_chain/shiny_chain/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/shiny_chain/shiny_chain/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('shiny_chain.listing', {
#             'root': '/shiny_chain/shiny_chain',
#             'objects': http.request.env['shiny_chain.shiny_chain'].search([]),
#         })

#     @http.route('/shiny_chain/shiny_chain/objects/<model("shiny_chain.shiny_chain"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('shiny_chain.object', {
#             'object': obj
#         })