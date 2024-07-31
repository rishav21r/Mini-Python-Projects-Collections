import re

def convert_to_bibtex(entry):
    # Regular expression to parse the entry
    pattern = re.compile(r'(?P<author>.*?), (?P<year>\d{4})\. (?P<title>.*?)\. (?P<journal>.*?) (?P<volume>\d+), (?P<pages>\d+)\. (?P<doi>https://doi\.org/.*?)\.')

    match = pattern.match(entry)
    if not match:
        print(f"Could not parse entry: {entry}")
        return None

    # Extract information using named groups
    author = match.group('author')
    year = match.group('year')
    title = match.group('title')
    journal = match.group('journal')
    volume = match.group('volume')
    pages = match.group('pages')
    doi = match.group('doi')

    # Create a unique key for each entry
    key = f"{author.split(',')[0].replace(' ', '_')}_{year}"

    # Convert to BibTeX format
    bibtex_entry = f"""@article{{{key},
  author = {{{author}}},
  title = {{{title}}},
  journal = {{{journal}}},
  year = {{{year}}},
  volume = {{{volume}}},
  pages = {{{pages}}},
  doi = {{{doi}}}
}}"""
    return bibtex_entry

# Read the references from a file
with open('references.txt', 'r') as file:
    entries = file.readlines()

# Convert each entry and save to a new BibTeX file
with open('references.bib', 'w') as bib_file:
    for entry in entries:
        entry = entry.strip()  # Remove leading/trailing whitespace
        bibtex_entry = convert_to_bibtex(entry)
        if bibtex_entry:
            bib_file.write(bibtex_entry + '\n\n')
