# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Enterprise Management Solution
#    risk_management Module
#    Copyright (C) 2014 OpenSur (comercial@opensur.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Customize Menus to Collapse or Expand with Animation',
    'category' : 'Menus',
    'description': """
        Module to Customize Menus to Collapse or Expand with Animation
 """,
    'version':'1.0',
    'author': '3cDevs',
    'website': 'http://www.3cdevs.com',
    'price': 10,
    'currency': 'EUR',
    'depends': [],
    'data': [
                'cm_collapse_menu.xml',

            ],
    'js': [
        'static/src/cm_collapse_menu.js'
    ],
    'css': [
    ],
    'installable': True,
    'application': True,
    'active': True,
}

