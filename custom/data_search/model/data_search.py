# -*- coding: utf-8 -*-
from odoo import models, fields


class DataSearch(models.Model):
    _name = "data.search"
    _description = "Data Search"

    data = fields.Char(string="Data", required=True)
    model_id = fields.Many2one('ir.model', required=True,
                               ondelete='cascade')
    fields_id = fields.Many2one('ir.model.fields', string='Fields',
                                domain="[('model_id', '=',  model_id)]")
    type_ids = fields.One2many(
        comodel_name="searched.data",
        inverse_name="type_id")

    def action_search(self):
        model = self.model_id.model
        menu_ids = self.env[model].sudo().search([])
        for i in menu_ids:
            print(i)
            search = self.env[model].sudo().search_read([('id', '=', i.id)])
            print(search)
