# -*- coding: utf-8 -*-
from odoo import http

# class Custody(http.Controller):
#     @http.route('/custody/custody/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custody/custody/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custody.listing', {
#             'root': '/custody/custody',
#             'objects': http.request.env['custody.custody'].search([]),
#         })

#     @http.route('/custody/custody/objects/<model("custody.custody"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custody.object', {
#             'object': obj
#         })