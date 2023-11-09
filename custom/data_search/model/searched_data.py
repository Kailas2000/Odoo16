# -*- coding: utf-8 -*-
from odoo import fields, models


class SearchedData(models.Model):
    _name = "searched.data"
    _description = "Searched Data"

    data = fields.Char(
        string="Searched Data",
        help="")
    model = fields.Char(
        string="Model",
        help="")
    type_id = fields.Many2one(comodel_name="data.search")