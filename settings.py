CSV_DELIMETER = '~'
DB_NAME = 'expenditure.db'

# Limit the number of simultaneous requests (async)
MAX_REQUESTS = 2

# Publisher has list of packages. Each package has list of resources (files).
PACKAGE_FILES = 'http://data.gov.uk/api/3/action/dataset_show?id=%s'

PUBLISHERS_LIST = 'http://data.gov.uk/api/3/action/organization_list'
PUBLISHER_DETAILS = 'http://data.gov.uk/api/3/action/organization_show?id=%s'
REPORTS_PATH = 'reports'