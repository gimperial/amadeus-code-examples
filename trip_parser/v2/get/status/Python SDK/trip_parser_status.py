# Install the Python library from https://pypi.org/project/amadeus
from amadeus import Client, ResponseError

amadeus = Client(
    client_id='YOUR_AMADEUS_API_KEY',
    client_secret='YOUR_AMADEUS_API_SECRET'
)

# Retrieves the status of the process. Replace JOB_ID with the id returned by Trip Parser Jobs
try:
    response = amadeus.travel.trip_parser_jobs.status('JOB_ID').get()
    print(response.data['status'])
except ResponseError as error:
    raise error