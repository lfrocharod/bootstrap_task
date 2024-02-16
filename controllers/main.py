from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal

class Widget(CustomerPortal):
    @http.route()
    def home(self, **kw):
        response = super().home(**kw)
        response.qcontext.update({
            'title' : 'My First Widget'
        })
        return response
