{
    'name': "Vehicle Rental",
    'version': '16.0.5.2.0',
    'author': "Kailas",
    'category': 'Category',
    'summary' : 'Manage your fleet and track car costs',
    'description': """
    Vehicle Rental
    """,
    'depends' : [
        'base',
        'fleet',
        'mail',
        'account'
    ],
    'data': [
        'security/security_group.xml',
        'security/company_rule.xml',
        'security/rule.xml',
        'security/ir.model.access.csv',

        'report/report_wizard_view.xml',
        'report/ir_report_templates.xml',
        'report/report.xml',

        'data/sequence.xml',
        'data/ir_cron_data_warning.xml',

        'views/rental_vehicle_view.xml',
        'views/custom_fleet_view.xml',
        'views/rent_request.xml',
        'views/rent_charge.xml',
        'views/vehicle_rental_menu.xml',
    ]
}