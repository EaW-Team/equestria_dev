BAD_CHARS_TO_REPLACE = {
    "\u00ad": "-",  # soft hyphen
    "\u00b4": "'",  # acute accent
    "\u00f7": "/",  # division sign
    "\u01c0": "|",  # latin letter dental click
    "\u01c3": "!",  # latin letter retroflex click
    "\u02b9": "'",  # modifier letter prime
    "\u02ba": '"',  # modifier letter double prime
    "\u02bc": "'",  # modifier letter apostrophe
    "\u02c4": "^",  # modifier letter up arrowhead
    "\u02c6": "^",  # modifier letter circumflex accent
    "\u02c8": "'",  # modifier letter vertical line
    "\u02cb": "'",  # modifier letter grave accent
    "\u02cd": "_",  # modifier letter low macron
    "\u02dc": "~",  # small tilde
    "\u0300": "'",  # combining grave accent
    "\u0301": "'",  # combining acute accent
    "\u0302": "^",  # combining circumflex accent
    "\u0303": "~",  # combining tilde
    "\u030b": '"',  # combining double acute accent
    "\u030e": '"',  # combining double vertical line above
    "\u0331": "_",  # combining macron below
    "\u0332": "_",  # combining low line
    "\u0338": "/",  # combining long solidus overlay
    "\u0589": ":",  # armenian full stop
    "\u05c0": "|",  # hebrew punctuation paseq
    "\u05c3": ":",  # hebrew punctuation sof pasuq
    "\u066a": "%",  # arabic percent sign
    "\u066d": "*",  # arabic five pointed star
    "\u200b": "",  # zero width space
    "\u2015": "--",  # horizontal bar
    "\u2016": "||",  # double vertical line
    "\u2017": "_",  # double low line
    "\u2018": "'",  # left single quotation mark
    "\u2019": "'",  # right single quotation mark
    "\u201a": ",",  # single low-9 quotation mark
    "\u201b": "'",  # single high-reversed-9 quotation mark
    "\u201c": '"',  # left double quotation mark
    "\u201d": '"',  # right double quotation mark
    "\u201e": '"',  # double low-9 quotation mark
    "\u201f": '"',  # double high-reversed-9 quotation mark
    "\u2032": "'",  # prime
    "\u2033": '"',  # double prime
    "\u2034": "'''",  # triple prime
    "\u2035": "'",  # reversed prime
    "\u2036": '"',  # reversed double prime
    "\u2037": "'''",  # reversed triple prime
    "\u2038": "^",  # caret
    "\u2039": "<",  # single left-pointing angle quotation mark
    "\u203a": ">",  # single right-pointing angle quotation mark
    "\u203d": "?",  # interrobang
    "\u2044": "/",  # fraction slash
    "\u204e": "*",  # low asterisk
    "\u2052": "%",  # commercial minus sign
    "\u2053": "~",  # swung dash
    "\u2060": "",  # word joiner
    "\u20e5": "\\",  # combining reverse solidus overlay
    "\u2212": "-",  # minus sign
    "\u2215": "/",  # division slash
    "\u2216": "\\",  # set minus
    "\u2217": "*",  # asterisk operator
    "\u2223": "|",  # divides
    "\u2236": ":",  # ratio
    "\u223c": "~",  # tilde operator
    "\u2264": "<=",  # less-than or equal to
    "\u2265": ">=",  # greater-than or equal to
    "\u2266": "<=",  # less-than over equal to
    "\u2267": ">=",  # greater-than over equal to
    "\u2303": "^",  # up arrowhead
    "\u2329": "<",  # left-pointing angle bracket
    "\u232a": ">",  # right-pointing angle bracket
    "\u266f": "#",  # music sharp sign
    "\u2731": "*",  # heavy asterisk
    "\u2758": "|",  # light vertical bar
    "\u2762": "!",  # heavy exclamation mark ornament
    "\u27e6": "[",  # mathematical left white square bracket
    "\u27e8": "<",  # mathematical left angle bracket
    "\u27e9": ">",  # mathematical right angle bracket
    "\u2983": "{",  # left white curly bracket
    "\u2984": "}",  # right white curly bracket
    "\u3003": '"',  # ditto mark
    "\u3008": "<",  # left angle bracket
    "\u3009": ">",  # right angle bracket
    "\u301b": "]",  # right white square bracket
    "\u301c": "~",  # wave dash
    "\u301d": '"',  # reversed double prime quotation mark
    "\u301e": '"',  # double prime quotation mark
    "\ufeff": "",  # zero width no-break space
}

def replace_bad_chars(text: str) -> str:
    for k, v in BAD_CHARS_TO_REPLACE.items():
        text = text.replace(k, v)
    return text

from pathlib import Path

for path in Path('localisation').rglob('*.yml'):
    with open(path, "r", encoding="utf-8-sig") as f:
        txt = f.read()
    with open(path, "w", encoding="utf-8-sig") as f:
        f.write(replace_bad_chars(txt))