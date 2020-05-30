# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectTask(models.Model):
    _inherit = 'project.task'
    
    capture_attachment_ids = fields.Many2many(
        'ir.attachment',
        string='Capture Photos',
        copy=False,
    )

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
