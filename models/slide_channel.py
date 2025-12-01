# hrm_course_members_display/models/slide_channel.py
from odoo import models, fields

class SlideChannel(models.Model):
    _inherit = "slide.channel"

    fake_members_display = fields.Integer(
        string="Display Members",
        compute="_compute_fake_members_display",
        store=False,
    )

    def _compute_fake_members_display(self):
        base = 587024
        for channel in self:
            # members_count = real attendees per course
            real = channel.members_count or 0
            channel.fake_members_display = base + real
