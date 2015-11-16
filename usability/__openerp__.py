# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2015 Medma - http://www.medma.net
#    All Rights Reserved.
#    Medma Infomatix (info@medma.net)
#
#    Coded by: Turkesh Patel (turkesh.patel@medma.in)
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


{
    "name": "Apply All Groups",
    "version": "1.0",
    "author": "Medma Infomatix",
    "category": "User Access",
    "website": "http://www.medma.net",
    "description": """Apply all Groups to any user on Single click of button in users form view. This Module can be very useful for Developers who usually need to give all access to any user many times when developing something.""",
    "summary": "Apply All Groups to any user on single click",
    "license": "AGPL-3",
    "depends": ["base"],
    "data": [
        'views/usability_view.xml',
    ],
    "installable": True,
    "auto_install": False,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
