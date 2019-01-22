
from odoo import api, fields, models


class Transaction(models.Model):

    _name = 'chain.transaction'
    _description = "Transaction representation"

    sender_id = fields.Many2one('res.partner')
    receiver_id = fields.Many2one('res.partner')
    content = fields.Text()
    timestamp = fields.Integer()
