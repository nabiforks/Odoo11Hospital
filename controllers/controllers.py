# -*- coding: utf-8 -*-
from odoo import http

# class Exercici01(http.Controller):
#     @http.route('/exercici01/exercici01/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/exercici01/exercici01/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('exercici01.listing', {
#             'root': '/exercici01/exercici01',
#             'objects': http.request.env['exercici01.exercici01'].search([]),
#         })

#     @http.route('/exercici01/exercici01/objects/<model("exercici01.exercici01"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('exercici01.object', {
#             'object': obj
#         })