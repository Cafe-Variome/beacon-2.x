"""Beacon Configuration."""

#
# Beacon general info
#
beacon_id = 'B2RI Demo Beacon'  # ID of the Beacon
beacon_name = 'B2RI Demo Beacon'  # Name of the Beacon service
api_version = 'v2.0.0'  # Version of the Beacon implementation
uri = 'https://www668.lamp.le.ac.uk'
beacon_granularity = "record"

#
#  Organization info
#
org_id = 'UoL'  # Id of the organization
org_name = 'Brookeslab, University of Leicester'  # Full name
org_description = (
    'Bioinformatics Research Group at the University of Leicester')
org_adress = ('The University of Leicester',
              'University Road',
              'Leicester',
              'LE1 7RH',
              'United Kingdom')
org_welcome_url = 'https://le.ac.uk/'
org_contact_url = 'mailto:ts339@le.ac.uk'
org_logo_url = 'https://beacon.cafevariome.org/img/uol_logo.png'
org_info = ''

#
# Project info
#
description = (r"This <a href='https://beacon-project.io/'>Beacon</a> "
               r"is based on the GA4GH Beacon "
               r"<a href='https://github.com/ga4gh-beacon/specification-v2/blob/master/beacon.yaml'>v2.0</a>")
version = 'v2.0'
welcome_url = 'https://beacon.ega-archive.org/'
alternative_url = 'https://beacon.ega-archive.org/api'
create_datetime = '2021-11-29T12:00:00.000000'
update_datetime = ''
# update_datetime will be created when initializing the beacon, using the ISO 8601 format

#
# Service
#
service_type = 'org.ga4gh:beacon:1.0.0'  # service type
service_url = 'https://beacon.ega-archive.org/api/services'
entry_point = False
is_open = True
# Documentation of the service
documentation_url = 'https://github.com/EGA-archive/beacon-2.x/'
# Environment (production, development or testing/staging deployments)
environment = 'test'

# GA4GH
ga4gh_service_type_group = 'org.ga4gh'
ga4gh_service_type_artifact = 'beacon'
ga4gh_service_type_version = '1.0'

# Beacon handovers
beacon_handovers = [
]

#
# Database connection
#
database_host = '127.0.0.1'
database_port = 27017
database_user = False
database_name = 'beacon'
database_auth_source = False
database_password = False
# database_schema = 'public' # comma-separated list of schemas
# database_app_name = 'beacon-appname' # Useful to track connections

#
# Web server configuration
# Note: a Unix Socket path is used when behind a server, not host:port
#
beacon_host = '0.0.0.0'
beacon_port = 5050
beacon_tls_enabled = False
beacon_tls_client = False
beacon_cert = '/etc/ega/server.cert'
beacon_key = '/etc/ega/server.key'
CA_cert = '/etc/ega/CA.cert'

#
# Permissions server configuration
#
permissions_url = 'http://beacon-permissions'

#
# IdP endpoints (OpenID Connect/Oauth2)
#
# or use Elixir AAI (see https://elixir-europe.org/services/compute/aai)
#
idp_client_id = 'beacon'
idp_client_secret = 'b26ca0f9-1137-4bee-b453-ee51eefbe7ba'  # same as in the test IdP
idp_scope = 'profile openid'

idp_authorize = 'http://idp/auth/realms/Beacon/protocol/openid-connect/auth'
idp_access_token = 'http://idp/auth/realms/Beacon/protocol/openid-connect/token'
idp_introspection = 'http://idp/auth/realms/Beacon/protocol/openid-connect/token/introspect'
idp_user_info = 'http://idp/auth/realms/Beacon/protocol/openid-connect/userinfo'
idp_logout = 'http://idp/auth/realms/Beacon/protocol/openid-connect/logout'

idp_redirect_uri = 'http://beacon:5050/login'

#
# UI
#
autocomplete_limit = 16
autocomplete_ellipsis = '...'

#
# Ontologies
#
ontologies_folder = "deploy/ontologies/"
