# Find Possible London Underground Stations

This application is a method to find which London Underground Stations are between x and y minutes journey duration from a particular London postcode.

### Use cases:
* Find what stations would be suitable to live near for a reasonable work commute
* Find an area suitable for a hotel destination for short commutes from places of interest

## Pre-requisites
### API KEY
You will need to generate an API KEY to run the application and place the API KEY in the primary key global variable in GetStationsDurations.py. Information on how to do this can be found here: https://api.tfl.gov.uk/.

The application is limited to 500 API requests per minute under TFL API's default limits.

### PyQt5
You will also need to install PyQt5, link here: https://pypi.org/project/PyQt5/

```bash
python -m pip install pyqt5
```
## Usage
Run the following command to start the application and interact with the PyQt5 GUI to specify location/postcode of interest.

```bash
FindPossibleStations.py
```
