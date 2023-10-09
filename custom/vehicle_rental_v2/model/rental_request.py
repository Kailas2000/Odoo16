# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class RentalRequest(models.Model):
    """Class represents the vehicle rental module"""
    _name = "rental.request"
    _description = "Vehicle Rental Request"
    _rec_name = "sequence_no"

    customer_id = fields.Many2one(comodel_name="res.partner")
    request_date = fields.Date(string="Request Date", required=True,
                               default=fields.Datetime.now())
    vehicle_id = fields.Many2one(comodel_name="vehicle.rental",
                                 string="Vehicle",
                                 domain="[('state', '=', 'available')]")
    from_date = fields.Date(string="From Date", required=True)
    to_date = fields.Date(string="To Date", required=True)
    period = fields.Integer(string="Period")
    state = fields.Selection(
        string='State',
        selection=[('draft', 'Draft'), ('confirm', 'Confirm'),
                   ('returned', 'Returned')],
        tracking=True,
        default='draft'
    )
    rent = fields.Integer(string="Rent", related='vehicle_id.rent')
    sequence_no = fields.Char(string='Sequence No', required=True,
                              readonly=True, default=lambda self: _('New'))
    period_type_id = fields.Many2one(comodel_name="rental.charge",
                                     string="Rent Time",
                                     domain="[('charge_id', '=', vehicle_id)]")
    warning = fields.Boolean()
    late = fields.Boolean()

    @api.model
    def create(self, vals):
        if vals.get('sequence_no', _('New')) == _('New'):
            vals['sequence_no'] = self.env['ir.sequence'].next_by_code(
                'rental.request') or _('New')
        res = super(RentalRequest, self).create(vals)
        return res

    @api.constrains('from_date', 'to_date')
    def _date_validation(self):
        if self.from_date >= self.to_date:
            raise ValidationError(
                "Check the date, To Date must be after from Date")

    @api.onchange('to_date', 'from_date')
    def _period_days(self):
        if self.to_date:
            self.period = (self.to_date - self.from_date).days

    def action_confirm(self):
        self.state = 'confirm'
        self.vehicle_id.state = 'not available'

    def action_return(self):
        self.state = 'returned'
        self.vehicle_id.state = 'available'

    def action_date(self):
        confirm_state = self.search(['state', '=', 'confirm'])

        # yesterday = fields.Date.today() - timedelta(days=1)
        # tomorrow = fields.Date.today() + timedelta(days=1)
        # date_after_tomorrow = fields.Date.today() + timedelta(days=2)
