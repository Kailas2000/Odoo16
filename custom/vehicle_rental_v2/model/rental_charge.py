# -*- coding: utf-8 -*-
from odoo import models, fields


class RentalCharge(models.Model):
    _name = "rental.charge"
    _description = "Vehicle Rental Charge"
    _rec_name = "time"

    time = fields.Selection(
        string='Time',
        selection=[('hour', 'Hour'), ('day', 'Day'),
                   ('weak', 'Weak'), ('month', 'Month')])
    amount = fields.Integer(string="Amount")

    charge_id = fields.Many2one("vehicle.rental", string="Rent Charge")
