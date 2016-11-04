import nativo
from nativo import metrics, entities, resolutions

nativo.api_key = '<api_key>'
nativo.api_secret = '<api_secret>'

payload = {
    "start_date": "2016-11-01T03:00:00Z",
    "end_date": "2016-11-03T23:00:00Z",
    "breakdown": [entities.CAMPAIGN],
    "metrics": [metrics.CLICKS],
    "filters" : { entities.CAMPAIGN : [115361] },
    "resolution": resolutions.DAILY,
    "sort_by": metrics.IMPRESSIONS,
    "sort_order": "desc",
    "page_size": 500,
    "page": 1,
    "timezone": "America/New_York"
}

response = nativo.DirectReport.retrieve(**payload)
print(response)
