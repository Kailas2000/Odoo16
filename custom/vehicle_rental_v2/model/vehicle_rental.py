# -*- coding: utf-8 -*-
from odoo import models, fields, api


class VehicleRental(models.Model):
    """Class represents the vehicle rental module"""
    _name = "vehicle.rental"
    _description = "Vehicle Rental"

    vehicle_id = fields.Many2one(comodel_name="fleet.vehicle", string="Vehicle",
                                 domain="[('state_id', 'in', 'Registered')]")
    name = fields.Char(string="Name", compute="_compute_name",
                       store=True)
    brand = fields.Char(string="Brand", related='vehicle_id.brand_id.name',
                        store=True)
    model = fields.Char(string="Model Year", compute="_compute_model_year")
    rent = fields.Integer(string="Rent")
    currency_id = fields.Many2one('res.currency', string='Currency',
                                  default=lambda
                                      self: self.env.user.company_id.currency_id)
    state = fields.Selection(
        string='State',
        selection=[('available', 'Available'),
                   ('not available', 'Not Available'),
                   ('sold', 'Sold')],
        default='available'
    )
    request_count = fields.Integer(compute='compute_request_count')
    confirm_request_id = fields.One2many(comodel_name="rental.request",
                                         inverse_name="vehicle_id",
                                         domain="[('state', '=', 'confirm')]")
    rent_charge_id = fields.One2many(comodel_name="rental.charge",
                                     inverse_name="charge_id")

    @api.depends('vehicle_id')
    def _compute_model_year(self):
        """selecting the model year from the date"""
        for record in self:
            record.model = str(
                record.vehicle_id.registration_date.year) if record.vehicle_id.registration_date else ""

    @api.depends('vehicle_id')
    def _compute_name(self):
        """selecting the model year from the date"""
        for record in self:
            if record.vehicle_id:
                record.name = str(
                    record.vehicle_id.brand_id.name) + '/' + record.vehicle_id.model_id.name + '/' + record.model

    def action_view_requests(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Requests',
            'view_mode': 'tree,form',
            'res_model': 'rental.request',
            'domain': [('vehicle_id', '=', self.id)],
            'context': "{'create': False}"
        }

    def compute_request_count(self):
        for record in self:
            record.request_count = self.env['rental.request'].search_count(
                [('vehicle_id', '=', self.id)])

