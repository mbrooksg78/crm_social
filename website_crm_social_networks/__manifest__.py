{
    "name": "Website CRM Social Networks",
    "summary": """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    "author": "Michael Brooks Guerra, Odoo Community Association (OCA)",
    "website": "",
    "category": "Website/Website",
    "version": "13.0.0.0.1",
    "license": "AGPL-3",
    # any module necessary for this one to work correctly
    "depends": ["website", "crm_social_networks"],
    # always loaded
    "data": ["data/website_data.xml", "views/partner_templates.xml"],
}
