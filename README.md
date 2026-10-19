# triplesky website — private draft

Keep this repository PRIVATE and GitHub Pages DISABLED until owner approval.
Open index.html on the local PC to review. English appears first; Japanese below.

## Local checks

    python tools/build.py
    python tools/check.py .

Before publication, also run `python tools/check.py --release`.
It currently fails intentionally while draft notices remain. This check is manual;
it does not change GitHub settings or guarantee store approval.

## Remaining before publication

- [Contact form draft and verification checklist](CONTACT-DRAFT.md): Google Form created, unpublished; end-to-end acceptance pending.
- Retention policy approved and applied in both languages and the Google Form. Set effective date immediately before publication.
- Verify download destinations and the features available in each public version.
- Check desktop and mobile appearance and interactions.
- Remove draft notices only when the remaining items are complete.
- Obtain owner approval before changing visibility or enabling Pages.

## Prioritized remaining tasks

| Priority | Task | Current boundary |
|---|---|---|
| P0 | Review phone layout | PC appearance, language links and page content approved by owner; phone check pending |
| P0 | Review final distribution URLs and per-version feature claims | No unverified download link is published |
| P0 | Authorize contact-form publication and test receipt/deletion | Requires publication; not yet authorized |
| P0 | Test actual respondent access without login | Preview settings alone do not prove this |
| P0 | Integrate tested respondent URL and effective date | Form edit/preview URLs must never be placed on the public site |
| P0 | Approve site publication, verify HTTPS and final app links | Repository stays private; Pages disabled |

Completed: four English-first bilingual pages; local links and anchors validated;
unpublished Google Form created; required/optional fields and invalid/blank email
checked in preview; inquiry retention wording approved and saved. No actual form
submission has been performed.

2026-10-20: Owner approved the remaining PC page content. Removed inquiry
categories Suggestion and Other and improvement-request solicitation as requested.
Subsequent owner request: remove Type entirely, require Platform (Windows/Mac/iPhone/Android)
and App version; Message remains required and Reply email remains optional.

## Apple release order

1. Complete free local/device tests and prepare the website privately.
2. Owner enrolls in Apple Developer Program after both apps are ready.
3. Perform distribution signing, TestFlight install/update and data-retention checks.
4. Publish reviewed privacy/support pages and verify HTTPS URLs.
5. Integrate actual URLs in apps; verify final builds and metadata; owner submits.

Xcode is free. Program membership is needed for App Store distribution/TestFlight.
Enrollment activation and review can take time; same-day release is not promised.
Do not place credentials, personal notes, unreleased product information or binaries here.
No deployment workflow is included. A private repository alone does not make a Pages site private.
