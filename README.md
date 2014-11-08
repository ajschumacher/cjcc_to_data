# CJCC Resource Locator to data

Extracts data from [DC's Criminal Justice Coordinating Council](http://cjcc.dc.gov/) (CJCC) [Resource Locator](http://www.cjccresourcelocator.net/).

Data is taken from HTML to an internal structured format that mimics the format implied by CJCC's system.

The eventual target data format is the (currently draft) [Human Services Data Specification](https://docs.google.com/document/d/1RH89UY7FDndivWNmtQkql4tdRTwYnCZluyu8itp5nTw/edit) (HSDS), which will be stored as a [data package](http://dataprotocols.org/data-packages/) conforming to an HSDS [JSON table schema](http://dataprotocols.org/json-table-schema/).


### Process

1. Download HTML page for each resource.
2. Extract data from each HTML page.
