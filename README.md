# SubtleLibs - Python

An easy way to connect with SubtleData's API natively in Python.

Before you proceed, you should read the basics of SubtleData's objects at:

## Installation

Run this at a command prompt.  If you are using virtual environments, make sure you are in the right one:

    $ pip install subtledata

or

    $ easy_install subtledata

## Usage

Start by obtaining a SubtleData API key with SubtleLibs access.  Then, pick whether you want to use the Express or Standard Library.

### Express Library

The express library is fully objectified, similar to an ORM.

Next, create an instance of the Express client and pass it your API Key.

```python
from subtledata import SubtleData
SD = SubtleData(api_key='S0YrNTJY')
```

If possible, you should avoid hard coding your API key into your codebase and instead retrieve it from an external source.

Now, top level objects (such as a location) will allow you to deeply and quickly access all of the capabilities of the SubtheData API.

For instance:

```python
location = SD.Locations.get(959)
print location.tables
ticket = location.tables[4].open_ticket(user_id=1234)
ticket.pay(card_id=5678)
```

### Standard Library

The standard library is purely functional and maps 1:1 with SubtleJSON's endpoints.  It is similar to the direct access capable using a database package instead of an ORM.

To get started, create a swagger API client with the production SubtleData endpoint:

```python
from subtledata.config import SD_ENDPOINT
from subtledata.api import swagger
from subtledata.api.LocationsApi import LocationsApi
client = swagger.ApiClient(apiKey='S0YrNTJY', apiServer=SD_ENDPOINT)
location_api = LocationsApi(client)
location = location_api.getLocation(959, 'S0YrNTJY')
print location.name
```

You can explore the Standard API by going through the methods available in:

- api/GeneralApi.py
- api/LocationsApi.py
- api/UsersApi.py

All other examples here will use the Express library.

## Express Library Examples

### Get a Location

```python
loc = SD.Locations.get(959)
```

## Contributing

Contributions are greatly appreciated for all code within the express library.  The standard library (/api/) is auto-generated on our end.  If you see any errors in the standard library, please submit an issue and bring them to our attention.

To contribute:

1. Fork this repo and make changes in your own fork and in a new branch
2. Bump the version number in `setup.py`
3. Commit your changes and push to your fork
4. Create a new pull request and submit it back to us!

## Contact

- George Sibble &lt;george.sibble@subtledata.com&gt;

## License

(The MIT License)

Copyright (c) 2013 SubtleData, Inc. &lt;code@subtledata.com&gt;

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.