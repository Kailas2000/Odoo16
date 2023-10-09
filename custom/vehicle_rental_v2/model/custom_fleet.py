# -*- coding: utf-8 -*-
from odoo import models, fields


class CustomFleet(models.Model):
    """Class represents the vehicle rental module"""
    _inherit = 'fleet.vehicle'

    registration_date = fields.Date(string="Registration Date",
                                    default=fields.Date.today)
