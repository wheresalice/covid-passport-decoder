# Covid Passport Decoder

This Python code decodes the content of QR codes that represent Covid Passports

Since people are very wary of sharing their own QR codes, this has received limited testing with NHS Digital-generated codes.  Please test it with your own QR codes and report any issues.


## Installation

This code was written in Python 3.  You will need Python 3 installed to use it.

1. `pip3 install -r requirements.txt` to install dependencies
2. `python main.py 'HC1:long string'` to decode the string

Note that you must use single quotes in step two because the string will probably have dollar symbols in it

## What am I seeing?

I don't know.

Clearly there's first and last name, and date of birth.  Some of the other fields are less clear

## Can I generate my own?

Yes and no.

You can generate your own, but it won't be signed by the right authority so it should fail.
