import markdown
import codecs

text="""
# Using markdown package for markdown processing

Markdown syntax allows you to use simple syntax for defining structured text. Usually this is used for quick and easy writing parts of HTML code.

## Preparation

To get it started working in python markdown package is necessary (with optional pygments, which is output code highlighter):

<kbd>pip install markdown</kbd>

<kbd>pip install pygments</kbd>

next, we need to create CSS for converted code output:

<kbd>pygmentize.exe -S default -f html -a .codehilite > styles.css</kbd>

If wanted, different style can be choosen (`-S default` parameter).
To see all styles available, use

<kbd>pygmentize -L style</kbd>

which will give you something similar to:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Pygments version 2.3.0, (c) 2006-2017 by Georg Brandl.

Styles:
~~~~~~~
* default:
    The default style (inspired by Emacs 22).
* emacs:
    The default style (inspired by Emacs 22).
* friendly:
    A modern style based on the VIM pyte theme.
* colorful:
    A colorful style, inspired by CodeRay.
* autumn:
    A colorful style, inspired by the terminal highlighting style.
* murphy:
    Murphy's style from CodeRay.
* manni:
    A colorful style, inspired by the terminal highlighting style.
* monokai:
    This style mimics the Monokai color scheme.
* perldoc:
    Style similar to the style used in the perldoc code blocks.
* pastie:
    Style similar to the pastie default style.
* borland:
    Style similar to the style used in the borland IDEs.
* trac:
    Port of the default trac highlighter design.
(...)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
et caetera.

## Usage

Simple code example:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# !/usr/bin/python3
import markdown
import codecs

text=\"""
# This is simple test for markdown output conversion

Let's see how it works.

## Tables

no. | name      | surname
--- | --------- | ---------------------
1   | Gabriel   | Milczarek
2   | Łukasz    | Bryzek
3   | Marcin    | Kawka

`extension=['tables'] is needed here`

Some simple list:

- this is simple list item
- created by markdown

\"""

html=markdown.markdown(text,extensions=['tables','fenced_code','codehilite'])
# note: if you don't want to use tables, code blocks and code highlighting, 
# you can omit extensions parameter

# print contents to utf-8 encoded html file:
output_file = codecs.open("output.html", "w",
                          encoding="utf-8",
                          errors="xmlcharrefreplace"
)
output_file.write(html)
output_file.close()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

and the output will look like:
<div class="card">
<div class="card-header">created output</div>
  <div class="card-body">

# This is simple test for markdown output conversion

Let's see how it works.

## Tables

no. | name      | surname
--- | --------- | ---------------------
1   | Gabriel   | Milczarek
2   | Łukasz    | Bryzek
3   | Marcin    | Kawka

`extension=['tables'] is needed here`

Some simple list:

- this is simple list item
- created by markdown
</div>
</div>
"""
html_header="""
<!DOCTYPE html>
<html>
<head>    
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
    <link rel="stylesheet" type="text/css" media="screen" href="styles.css" />    
</head>
<body>
    <div class="container">
    <!-- page contents start here -->
"""
html_footer="""
    <!-- page contents end here   -->
    </div>
</body>
</html>
"""

html=html_header+markdown.markdown(text,extensions=['tables','fenced_code','codehilite'])+html_footer
output_file = codecs.open("markoutput.html", "w",
                          encoding="utf-8",
                          errors="xmlcharrefreplace"
)
output_file.write(html)
output_file.close()
