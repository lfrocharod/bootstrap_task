# __manifest__.py
{
    'name': 'Website Widget',
    'version': '1.0',
    'depends': ['portal', 'website'],
    'author': 'Luis Rocha',
    'description': 'Creating a new section inside the /my URL that contains a button that when clicked changes the text it contains.',
    'data': [
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'website_widget/static/src/js/website_widget.js',
            'website_widget/static/src/scss/website_widget.scss',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}
