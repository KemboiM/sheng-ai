# Data Governance

## Required provenance fields
Every retained corpus item should include:

- `source_name`
- `source_url_or_id`
- `source_type`
- `collector`
- `date_collected`
- `permission_basis`
- `license_or_terms`
- `commercial_use_allowed`
- `training_use_allowed`
- `speaker_consent` (for private/commissioned audio)
- `review_status`

## Social platform rule
Do not treat technical accessibility as permission. Prefer:

1. official APIs with compatible terms;
2. creator/rights-holder licensing;
3. commissioned recordings;
4. public-domain or permissively licensed corpora;
5. manual linguistic annotation of facts/meanings.

Do not commit raw private or sensitive source data to Git.

## Voice rule
Do not create a commercial voice clone of a person without explicit authorization for that use.

## Scripture rule
Do not assume a Bible translation is public domain because it is readable online. Record the translation, rights holder, permission basis, and publication restrictions before using it for model training or publication.
