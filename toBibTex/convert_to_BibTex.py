import re

def convert_to_bibtex(entry):
    patterns = [
        re.compile(r'(?P<author>.+?), (?P<year>\d{4})\. (?P<title>.*?)\. (?P<journal>.*?), (?P<volume>\d+)\((?P<issue>\d+)\), pp\. (?P<pages>.*?)\. Available at: (?P<doi>https://doi\.org/.*?)\.'),
        re.compile(r'(?P<author>.+?), (?P<year>\d{4})\. (?P<title>.*?)\. (?P<journal>.*?), (?P<volume>\d+), pp\. (?P<pages>.*?)\. Available at: (?P<doi>https://doi\.org/.*?)\.'),
        re.compile(r'(?P<author>.+?), (?P<year>\d{4})\. (?P<title>.*?)\. (?P<journal>.*?), Volume (?P<volume>\d+), p\. (?P<pages>\d+)\. (?P<doi>https://doi\.org/.*?)\.'),
        re.compile(r'(?P<author>.+?) et al\., (?P<year>\d{4})\. (?P<title>.*?)\. (?P<journal>.*?), (?P<volume>\d+), (?P<doi>https://doi\.org/.*?)\.'),
        re.compile(r'(?P<author>.+?) \((?P<year>\d{4})\) ‘(?P<title>.*?)’, (?P<journal>.*?), (?P<volume>\d+)\((?P<issue>\d+)\), pp\. (?P<pages>.*?)\. Available at: (?P<doi>https://doi\.org/.*?)\.'),
        re.compile(r'(?P<author>.+?) \((?P<year>\d{4})\) ‘(?P<title>.*?)’, (?P<journal>.*?), (?P<volume>\d+), p\. (?P<pages>\d+)\. Available at: (?P<doi>https://doi\.org/.*?)\.'),
        re.compile(r'(?P<author>.+?) \((?P<year>\d{4})\) ‘(?P<title>.*?)’, (?P<journal>.*?), (?P<volume>\d+), pp\. (?P<pages>.*?)\. Available at: (?P<doi>https://doi\.org/.*?)\.'),
        re.compile(r'(?P<author>.+?), (?P<year>\d{4})\. (?P<title>.*?)\. (?P<journal>.*?) (?P<volume>\d+), (?P<pages>.*?)\. (?P<doi>https://doi\.org/.*?)\.'),
        re.compile(r'(?P<author>.+?), (?P<year>\d{4})\. (?P<title>.*?)\. (?P<journal>.*?) (?P<volume>\d+)\((?P<issue>\d+)\), (?P<pages>.*?)\. (?P<doi>https://doi\.org/.*?)\.'),
        re.compile(r'(?P<author>.+?), (?P<year>\d{4})\. (?P<title>.*?)\. (?P<journal>.*?) (?P<volume>\d+), (?P<doi>https://doi\.org/.*?)\.')
    ]

    for pattern in patterns:
        match = pattern.match(entry)
        if match:
            # Extract information using named groups
            author = match.group('author')
            year = match.group('year')
            title = match.group('title')
            journal = match.group('journal')
            volume = match.group('volume')
            pages = match.group('pages') if 'pages' in match.groupdict() else ''
            doi = match.group('doi')
            issue = match.group('issue') if 'issue' in match.groupdict() else ''

            # Create a unique key for each entry
            key = f"{author.split(',')[0].replace(' ', '_')}_{year}"

            # Convert to BibTeX format
            bibtex_entry = f"""@article{{{key},
  author = {{{author}}},
  title = {{{title}}},
  journal = {{{journal}}},
  year = {{{year}}},
  volume = {{{volume}}},"""

            if issue:
                bibtex_entry += f"""
  number = {{{issue}}},"""

            if pages:
                bibtex_entry += f"""
  pages = {{{pages}}},"""

            bibtex_entry += f"""
  doi = {{{doi}}}
}}"""
            return bibtex_entry

    print(f"Could not parse entry: {entry}")
    return None

# Read the references from a file
with open('/mnt/data/input.txt', 'r') as file:
    entries = file.readlines()

# Convert each entry and save to a new BibTeX file
with open('/mnt/data/references.bib', 'w') as bib_file:
    for entry in entries:
        entry = entry.strip()  # Remove leading/trailing whitespace
        if entry:  # Ensure entry is not empty
            bibtex_entry = convert_to_bibtex(entry)
            if bibtex_entry:
                bib_file.write(bibtex_entry + '\n\n')
