from flask_assets import Environment, Bundle


def compile_assets(app):
    """Configure authorization asset bundles."""
    assets = Environment(app)
    Environment.auto_build = False
    Environment.debug = False
    less_bundle = Bundle('src/less/main.less',
                         filters='less, cssmin',
                         output='dist/css/style.min.css',
                         extra={'rel': 'stylesheet/less'})
    js_bundle = Bundle('src/js/main.js',
                       filters='jsmin',
                       output='dist/js/main.min.js')
    assets.register('less_all', less_bundle)
    assets.register('js_all', js_bundle)
    if app.config['FLASK_ENV'] == 'development':
        less_bundle.build()
        js_bundle.build()
