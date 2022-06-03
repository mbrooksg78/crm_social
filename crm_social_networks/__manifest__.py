{
    "name": "CRM Social Network",
    "summary": """
        Integrate CRM with Facebook, Instagram and LinkedIn""",
    "author": "Odoo Community Association (OCA), Michael Brooks",
    "license": "AGPL-3",
    "website": "",
    "category": "Sales/CRM",
    "version": "13.0.0.0.1",
    # any module necessary for this one to work correctly
    "depends": ["crm"],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/inherited_res_partner_views.xml",
    ],
    # only loaded in demonstration mode
    "demo": ["demo/demo.xml",],
    "application": True,
}
