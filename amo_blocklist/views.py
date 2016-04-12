"""Example url to get a blocklist:
https://blocklist.addons.mozilla.org/
    blocklist/
    3/
    %7Bec8030f7-c20a-464f-9b0e-13a3a9e97384%7D/
    44.0a1/
    Firefox/
    20151027120555/
    Linux_x86_64-gcc3/
    en-US/
    default/
    Linux%203.13.0-66-generic%20%28GTK%203.10.8%29/
    default/
    default/
    7/
    64/
    1/
"""

from cliquet import Service


blocklist = Service(
    name="blocklist",
    path='/blocklist/{api_ver}/{application_guid}/{application_ver}/',
    description="Blocklist data")


@blocklist.get()
def get_blocklist(request):
    api_ver = request.matchdict['api_ver']
    app = request.matchdict['application_guid']
    app_ver = request.matchdict['application_ver']

    query = request.body

    print api_ver, app, app_ver, query

    return {
        'API version': api_ver,
        'Application': app,
        'Application version': app_ver,
        'Query': query,
    }
