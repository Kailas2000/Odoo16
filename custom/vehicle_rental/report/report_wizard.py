# -*- coding: utf-8 -*-
from odoo import fields, models


class ReportWizard(models.TransientModel):
   _name = 'report.wizard'
   _description = 'Wizard form for report'

   from_date = fields.Date(string="From Date",
                           help="Report data will be visible from From Date")
   to_date = fields.Date(string="ToDate",
                         help="Data will be visible upto this date, if mention")
   name_id = fields.Many2one(comodel_name='rental.vehicle',
                          string="Vehicle Name",
                          help="To access the vehicles")
   customer_id = fields.Many2one("res.partner", string="Customer")

   def button_action_pdf(self):
      """While clicking the button from the form
       it return to the report.xml action."""
      return self.env.ref('vehicle_rental.action_report_vehicle_rental'
                          ).report_action(self, data=self.read()[0])
