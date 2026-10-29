"""Minimal RTF to plain text (standard library only): paragraphs become lines."""
import re

_DEST = {'fonttbl', 'colortbl', 'stylesheet', 'info', 'pict', 'header', 'footer', 'headerl', 'headerr', 'footerl',
         'footerr', 'headerf', 'footerf', 'listtable', 'listoverridetable', 'rsidtbl', 'latentstyles', 'datastore',
         'themedata', 'colorschememapping', 'xmlnstbl', 'generator', 'object', 'fldinst', 'filetbl', 'revtbl',
         'pgdsctbl', 'operator', 'author', 'title', 'nonshppict', 'footnote', 'listtext', 'pntext', 'pntxta', 'pntxtb',
         'mmathPr', 'wgrffmtfilter', 'xe', 'tc', 'bkmkstart', 'bkmkend', 'shpinst', 'sp'}
_SPECIAL = {'par': '\n', 'line': '\n', 'sect': '\n', 'page': '\n', 'cell': '\t', 'row': '\n', 'tab': '\t',
            'emdash': '\u2014', 'endash': '\u2013', 'lquote': '\u2018', 'rquote': '\u2019', 'ldblquote': '\u201c',
            'rdblquote': '\u201d', 'bullet': '\u2022', '~': '\u00a0', '_': '-', '-': ''}
_TOK = re.compile(r'\([a-zA-Z]+)(-?\d+)? ?|\\'([0-9a-fA-F]{2})|\(.)|([{}])|(\r\n|\n|\r)|([^\{}\r\n]+)', re.S)


def to_text(raw: bytes) -> str:
    s = raw.decode('latin-1')
    stack, ignorable, uc, skip = [], False, 1, 0
    out = []
    hexbuf = bytearray()

    def flush():
        if hexbuf:
            out.append(hexbuf.decode('cp1252', 'replace'))
            hexbuf.clear()
    first_star = False
    for m in _TOK.finditer(s):
        word, arg, hx, ch, brace, nl, text = m.groups()
        if brace == '{':
            flush(); stack.append((ignorable, uc)); first_star = True; continue
        if brace == '}':
            flush()
            if stack:
                ignorable, uc = stack.pop()
            first_star = False; continue
        if nl:
            continue
        if skip and (text or hx or ch):
            if text:
                n = min(skip, len(text)); skip -= n; text = text[n:]
                if not text: continue
            else:
                skip -= 1; continue
        if ch == '*':
            ignorable = True; continue
        if word:
            flush()
            if word in _DEST:
                ignorable = True
            elif word == 'uc':
                uc = int(arg or 1)
            elif word == 'u':
                if not ignorable:
                    v = int(arg); out.append(chr(v + 65536 if v < 0 else v))
                skip = uc
            elif word in _SPECIAL and not ignorable:
                out.append(_SPECIAL[word])
            continue
        if hx:
            if not ignorable:
                hexbuf.append(int(hx, 16))
            continue
        if ch:
            flush()
            if not ignorable:
                out.append(_SPECIAL.get(ch, ch) if ch in '~_-' else ch)
            continue
        if text:
            flush()
            if not ignorable:
                out.append(text)
    flush()
    return ''.join(out)

if __name__ == '__main__':
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    print(to_text(open(sys.argv[1], 'rb').read()))
