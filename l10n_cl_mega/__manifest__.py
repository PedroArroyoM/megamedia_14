# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Copyright (c) 2019 - Blanco Martín & Asociados. https://www.bmya.cl
{
    'name': 'Chile - Accounting MegaMedia',
    'version': "3.0",
    'description': """
Chilean accounting chart and tax localization.
Plan contable chileno e impuestos de acuerdo a disposiciones vigentes
    """,
    'author': 'Tierra Nube',
    'category': 'Accounting/Localizations/Account Charts',
    'depends': [
        'contacts',
        'base_address_city',
        'base_vat',
        'l10n_latam_base',
        'l10n_latam_invoice_document',
        'uom',
        'l10n_cl',
        ],
    'data': [
        'data/l10n_cl_chart_data.xml',
        'data/account.account.template.csv',
        #'data/account.fiscal.position.template.csv',
        #'data/account.fiscal.position.account.template.csv',
        'data/account_tax_report_data.xml',
        'data/account_tax_group_data.xml',
        'data/account_tax_tags_data.xml',
        'data/account_tax_data.xml',
        #'data/l10n_latam_identification_type_data.xml',
        #'data/l10n_latam.document.type.csv',
        'data/menuitem_data.xml',
        #'data/product_data.xml',
        #'data/uom_data.xml',
        'data/res.currency.csv',
        # 'data/res_currency_data.xml',
        #'data/res.bank.csv',
        #'data/res.country.csv',
        #'data/res_partner.xml',
        'data/account_fiscal_template.xml',
        'data/account_chart_template_data.xml',
    ],
    'demo': [
        'demo/partner_demo.xml',
    ]
}
