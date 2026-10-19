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

- [Contact form draft and verification checklist](CONTACT-DRAFT.md) (not created or published).
- Choose contact method and create the actual form if selected.
- Review policy text, retention of inquiries, and effective date.
- Verify download destinations and the features available in each public version.
- Check desktop and mobile appearance and interactions.
- Remove draft notices only when the remaining items are complete.
- Obtain owner approval before changing visibility or enabling Pages.

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
