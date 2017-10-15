# 2017 Reinvent schedule data extractor
This is meant to turn the data available through https://www.portal.reinvent.awsevents.com/connect/interests.ww into a table of data for figuring out what you actually want to request reserved seats for.

The results are delimited by a "|" are easily imported into excel or similar.

## The Data
Because I built this quickly and because of the way the webpage is built, you need to load the page in a browser, click *every one* of the "Scheduling Options" links, which will add load the location data into the page, and then save it via the dev tools.
In chrome:
- "inspect" the page
- choose the "elements" tab
- right click on the <html> tag at the top
- copy -> "copy outerHTML"
- save the clipboard contents to a file (the default is a file called `AWS re_Invent 2017.htm` in the same directory as this script, but you can pass it as the 1st argument per below)


## Running
```
python buildtable.py <path_to_filename>
```
the output is sent to stdout, so this can of course be redirected to a file (` > /path/to/outputfile`)

## Packages to install

- python 3
- beautifulsoup4

## Testing

```
python tests/tests.py
```
