# hrm_course_members_display/__manifest__.py
{
    "name": "HRM Course Members Display",
    "version": "18.0.1.0.0",
    "summary": "Show fake members count (587024 + attendees) on website course page",
    "author": "Habit Reset Method",
    "website": "https://habitresetmethod.com",
    "category": "Website/eLearning",
    "license": "LGPL-3",
    "depends": ["website_slides"],
    "data": [
        "views/website_slides_members_display.xml",
    ],
    "installable": True,
    "application": False,
}
