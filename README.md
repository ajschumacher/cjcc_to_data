# CJCC Resource Locator to data

Extracts data from [DC's Criminal Justice Coordinating Council](http://cjcc.dc.gov/) (CJCC) [Resource Locator](http://www.cjccresourcelocator.net/).

### Process

1. Download HTML page for each resource into a file in the `html` directoy.

    1. The `get_pages.py` script does this, when run from the project directory.

2. Extract data from each HTML page. Data is taken from HTML to an internal structured format that mimics the format implied by CJCC's system.

    1. The `get_data.py` script has a function `reader_all()` which returns a list of dicts with the data from the html files.

3. Convert to the [Human Services Data Specification](https://docs.google.com/document/d/1RH89UY7FDndivWNmtQkql4tdRTwYnCZluyu8itp5nTw/edit) (HSDS), which will be stored as a [data package](http://dataprotocols.org/data-packages/) conforming to an HSDS [JSON table schema](http://dataprotocols.org/json-table-schema/).
