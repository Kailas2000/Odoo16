# -*- coding: utf-8 -*-
from odoo import models, fields


class RentCharge(models.Model):
    """Class represents the rent charge module"""
    _name = "rent.charge"
    _description = "Rent Charges"
    _rec_name = "time"

    time = fields.Selection(
        string='Time',
        selection=[('hour', 'Hour'), ('day', 'Day'), ('weak', 'Weak'),
                   ('month', 'Month')]
    )
    amount = fields.Float('Amount')
    time_id = fields.Many2one("rental.vehicle", string="Rent Charge")

    # To avoid the duplication of the time in rent charges
    _sql_constraints = [
        ('name_uniq', 'unique (time,time_id)',
         "Only one value can be defined for each given usage!"),
    ]
