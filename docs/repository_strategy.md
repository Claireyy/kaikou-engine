# Repository Strategy

## Public Repository

The public repository is `kaikou-engine`.

It contains the public-safe engineering shell:

- folder structure
- product and architecture documents
- public schemas
- non-sensitive prompt templates
- placeholder integration folders
- core engine module boundaries

It must not contain operational secrets, unpublished content, raw platform data, or private automation details.

## Private Assets

Private assets should be stored outside the public repository or in a separate private repository.

Private assets include:

- real prompts used for production generation
- WorkBuddy browser automation details
- platform account notes
- platform cookies or tokens
- raw captured signals
- unpublished scripts
- output history
- cloud deployment secrets

## Future Link With Kaikou

The future Kaikou product can call `kaikou-engine` as a public or internal engine layer.

Private content assets should be injected through configuration, environment variables, private packages, or cloud storage instead of being committed to the public repository.

## Rule

Public repository shows the system shape.

Private repository keeps the production advantage.

