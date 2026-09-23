# Security Policy

## Supported surface

This public repository contains a read-only mirror of published jiami.dog articles and the synchronization code that maintains it. It is not an authentication service, credential store, WordPress backup, or private-data archive.

The synchronization workflow:

- reads only from the fixed HTTPS endpoint `https://jiami.dog/wp-json/wp/v2/posts`;
- sends no WordPress password, API key, token, or Cookie;
- has GitHub `contents: write` permission and no broader permission;
- can modify only the generated README section, mirrored articles, article navigation, the machine-readable article index, and deterministic sync state;
- rejects unexpected hosts, duplicate IDs, oversized responses, unsafe paths, and accidental empty-feed mass deletion;
- requires two consecutive complete snapshots to omit an existing article before deleting its mirror.

## Reporting a vulnerability

Do not publish credentials, personal data, exploitable URLs, or reproduction secrets in a public Issue. Use GitHub private vulnerability reporting for this repository when available. If that channel is unavailable, contact JiamiDog through the official contact channel listed on [jiami.dog](https://jiami.dog/).

## Out of scope

Requests for WordPress access, unpublished drafts, user information, traffic logs, affiliate-account data, or internal operating material are outside the scope of this repository and must never be added here.
