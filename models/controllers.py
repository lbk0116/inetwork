# -*- coding: utf-8 -*-
from openerp import http

# class Inetwork(http.Controller):
#     @http.route('/inetwork/inetwork/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inetwork/inetwork/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inetwork.listing', {
#             'root': '/inetwork/inetwork',
#             'objects': http.request.env['inetwork.inetwork'].search([]),
#         })

#     @http.route('/inetwork/inetwork/objects/<model("inetwork.inetwork"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inetwork.object', {
#             'object': obj
#         })