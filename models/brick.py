
from odoo import models, fields, api


class Brick(models.Model):

    _name = 'chain.brick'
    _description = "Brick representation"

    ident = fields.Integer()
    header_hash = fields.Char()
    previous_hash = fields.Char()
    nonce = fields.Integer()
    bits = fields.Char()
    timestamp = fields.Integer()

