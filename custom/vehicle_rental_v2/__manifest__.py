{
    'name': "Vehicle Rental 2.0",
    'version': '16.0.1.0.0',
    'author': "Kailas",
    'category': 'Category',
    'summary' : 'Manage your fleet and track car costs',
    'description': """
    Vehicle Rental 2.0
    """,
    'depends' : [
        'base',
        'fleet'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/scheduler.xml',
        'view/custom_fleet.xml',
        'view/vehicle_rental.xml',
        'view/rental_charge.xml',
        'view/rental_request.xml',
        'view/vehicle_rental_v2_menu.xml',
    ]
}