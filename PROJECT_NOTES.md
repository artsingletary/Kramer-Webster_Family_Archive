# Kramer-Webster Family Archive — Project Notes

## 1. Project Overview

The Kramer-Webster Family Archive is a genealogy website documenting the Kramer and Webster families through individual biographies, family relationships, photographs, historical documents, and family stories.

The website is generated using Python, Jinja2 templates, and JSON data files. It produces a static HTML website in the `docs/` directory, intended for publication through GitHub Pages.

## 2. Project Directory Structure

```text
Kramer-Webster_Family_Archive/
├── build_site.py
├── sort_people.py
├── sort_sources.py
├── PROJECT_NOTES.md
├── data/
│   ├── people.json
│   ├── sources.json
│   ├── photos.json
│   └── stories.json
├── templates/
├── static/
├── photos/
├── documents/
└── docs/
```

- `build_site.py` — Main website generator.
- `sort_people.py` — Utility script for sorting people records.
- `sort_sources.py` — Utility script for sorting source records.
- `data/` — Genealogical information stored in JSON.
- `templates/` — Jinja2 HTML templates.
- `static/` — CSS, JavaScript, and other static assets.
- `photos/` — Original family photographs.
- `documents/` — Historical document images.
- `docs/` — Generated website ready for GitHub Pages.

The repository files are the authoritative implementation. Review current files before modifying the website.

## 3. Website Generation

Run the following command from the repository root:

```bash
python build_site.py
```

The script reads the four JSON data files and renders the Jinja2 templates.

Generated pages include:

- Home page (`index.html`)
- Kramer family listing (`kramer-family.html`)
- Webster family listing (`webster-family.html`)
- All-family listing (`all-family.html`)
- Interactive family tree (`family-tree.html`)
- Photograph gallery (`photos.html`)
- Historical documents (`documents.html`)
- Family stories (`stories.html`)
- Privacy notice (`privacy.html`)
- Individual person pages (`people/<person_id>.html`)
- Individual published story pages (`stories/<story_id>.html`)

The build script copies the `static/`, `photos/`, and `documents/` directories into `docs/`.

The corresponding generated asset directories are deleted and recreated during each build. The generated `docs/stories/` directory is also recreated.

Always edit the source files rather than the generated output.

## 4. People Data — data/people.json

Contains an array of person records.

Confirmed fields in the initial record:

- `id` — Unique person identifier.
- `first_name` — Given name.
- `middle_name` — Middle name.
- `last_name` — Surname.
- `married_name` — Married surname.
- `nickname` — Nickname.
- `family_lines` — Array containing `kramer`, `webster`, or both.
- `profile_photo` — Profile photograph filename.
- `birth_year` — Birth year.
- `birth_date` — Full birth date in YYYY-MM-DD format.
- `death_year` — Death year.
- `death_date` — Full death date in YYYY-MM-DD format.
- `biography` — Array of biographical paragraphs.

Additional fields supported by the website generator include:

- `father` — Person ID of the father.
- `mother` — Person ID of the mother.
- `spouses` — Array of spouse person IDs.
- `suffix` — Name suffix.
- `death_before` — Year before which death occurred.

Parent and spouse references must point to existing person IDs.

The website derives children and siblings from parent references.

Do not add relationships without supporting genealogical evidence.

## 5. Sources — data/sources.json

Contains an array of historical source records.

Recommended source structure, based on the existing website generator and the established Singletary-Herrin archive conventions:

- `id` — Unique source identifier.
- `type` — Record type, such as census, birth, death, marriage, obituary, or military.
- `title` — Descriptive source title.
- `people` — Array of associated person IDs.
- `date` — Record date, where known.
- `location` — Location associated with the record.
- `description` — Detailed description of the source.
- `supports` — Array of facts or claims supported by the source.
- `documents` — Array of attached historical document filenames.

The website associates sources with people using the `people` array.

Sources containing document filenames in `documents` appear in the historical documents collection.

The source record may exist without a document image.

Preserve conflicting information and identify unresolved discrepancies rather than silently resolving them.

## 6. Photographs — data/photos.json

Contains photograph metadata.

The website associates photographs with individuals using the `people` array.

Photographs with `type` set to `grave` are separated from regular photographs on individual person pages and sorted after other photographs in the gallery.

Use `caption` for the visible photograph description.

Gravestone captions should include the cemetery name when known.

Photograph metadata fields beyond those referenced by the current build script should be confirmed against existing templates or future records before being standardized.

## 7. Family Stories — data/stories.json

Contains family history stories.

The website publishes only stories whose `status` is `published` (case-insensitive).

Published stories appear on the stories landing page and receive individual HTML pages based on their IDs.

Stories can reference associated people through a `people` array.

Draft or unpublished stories are excluded from the generated stories pages.

## 8. File Naming Conventions

- Use lowercase filenames with underscores.
- Prefix historical document filenames with the four-digit year when the document year is known.
- Example: `1910_webster_family_federal_census.jpg`
- Use descriptive filenames identifying the person, family, or record.
- Preserve original spellings and names in historical source descriptions.
- Include newspaper publication names in obituary descriptions when known.
- Include cemetery names in gravestone captions when known.
- Do not invent missing dates or publication details.

## 9. Genealogy Research Standards

- Never invent names, dates, locations, or family relationships.
- Distinguish verified facts from unconfirmed research leads.
- Base genealogical conclusions on historical evidence.
- Preserve original document spellings and conflicting information.
- Document the source of important biographical claims.
- Do not create parent-child relationships without supporting evidence.
- Record uncertainty explicitly when the evidence is incomplete.

## 10. Current Project Status — October 30, 2026

The archive currently contains one person record:

**Susie Catherine Webster (1902–1993)**

- Nickname: Sue.
- Married surname: Kramer.
- Person ID: `susie-catherine-webster-1902`.
- Family lines: Kramer and Webster.
- Her current biography identifies William Gabriel Snead Webster and Addie Leola Daniel as her parents, and Adam Kramer as her husband.
- These relatives have not yet been added as separate person records.

Current JSON status:

- `people.json` — One person record.
- `sources.json` — Empty array.
- `photos.json` — Empty array.
- `stories.json` — Empty array.

## 11. Next Planned Work

1. Review and document the 1910 United States Census associated with Sue Webster.
2. Create a source entry in `data/sources.json` using the established schema.
3. Add the corresponding census image to `documents/`.
4. Regenerate the website and verify that the source appears on Sue's profile and the historical documents page.
5. Continue expanding the Kramer and Webster family profiles using documented historical evidence.

## 12. Development and Continuity Rules

- Consult this file when beginning a new development session.
- Review the current repository files before proposing modifications.
- Preserve existing JSON field names and website functionality.
- Provide complete, valid JSON records when adding or updating data.
- Explain where new files and code changes belong.
- Keep source data and generated website output separate.
- Update these project notes when the architecture, conventions, or project status changes.

The local repository and its Git history are the authoritative sources for the website implementation. ChatGPT conversation history is not a substitute for version-controlled project documentation.
