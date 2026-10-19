"""Offline checks for the unpublished static website."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import sys

args = [arg for arg in sys.argv[1:] if arg != '--release']
release = '--release' in sys.argv[1:]
root = Path(args[0] if args else Path(__file__).resolve().parent.parent).resolve()

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, 'Duplicate anchor'
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])

files = list(root.rglob('*.html'))
assert len(files) == 4, f'Expected four pages, found {len(files)}'
parsed = {}
for path in files:
    content = path.read_text(encoding='utf-8')
    assert '<html lang="en">' in content
    assert content.index('id="english"') < content.index('id="japanese"')
    assert '<script' not in content.lower()
    assert '<form' not in content.lower(), 'Contact form remains pending'
    if release:
        assert 'Unpublished preview' not in content, 'Release blocked: unpublished draft notice remains'
        assert 'contact method is being selected' not in content.lower(), 'Release blocked: contact is pending'
        assert 'selected after review' not in content.lower(), 'Release blocked: contact is pending'
    page = Page()
    page.feed(content)
    parsed[path] = page
for path, page in parsed.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme:
            assert url.scheme == 'https', 'Unexpected external URL scheme'
            continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        assert target.is_relative_to(root) and target.is_file(), (path, link)
        if url.fragment:
            assert unquote(url.fragment) in parsed[target].ids, (path, link)
print('PASS: 4 bilingual pages; local links, anchors and assets; no scripts or live forms.')
