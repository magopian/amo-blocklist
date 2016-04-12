"""amo-blocklist - A kinto plugin to generate and serve XML blocklist files for
Firefox et al."""

__version__ = '0.1.0'
__author__ = 'Mathieu Agopian <magopian@mozilla.com>'
__all__ = []


def includeme(config):
    print("Starting the amo-blocklist plugin.")

    # Activate end-points.
    config.scan('amo_blocklist.views')


def load_from_config(config):
    settings = config.get_settings()

    cert_bucket = settings.get('blocklist.cert_bucket', 'blocklists')
    gfx_bucket = settings.get('blocklist.gfx_bucket', 'blocklists')
    addons_bucket = settings.get('blocklist.addons_bucket', 'blocklists')
    plugins_bucket = settings.get('blocklist.plugins_bucket', 'blocklists')

    cert_collection = settings.get('blocklist.cert_collection', 'certificates')
    gfx_collection = settings.get('blocklist.gfx_collection', 'gfx')
    addons_collection = settings.get('blocklist.addons_collection', 'add-ons')
    plugins_collection = settings.get(
        'blocklist.plugins_collection', 'plugins')

    return {
        'certificates': [cert_bucket, cert_collection],
        'gfx': [gfx_bucket, gfx_collection],
        'addons_bucket': [addons_bucket, addons_collection],
        'plugins': [plugins_bucket, plugins_collection],
    }
