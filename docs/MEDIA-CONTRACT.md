# Media Production Contract

Media production is part of the same Team OS, scheduler, storage, QA and recovery architecture.

## Supported project classes

- image
- thumbnail/social visual
- storyboard
- short video
- vertical video
- long-form video
- documentary
- voice-over production
- mixed media

## Canonical workflow

Goal Contract
→ Creative Brief
→ Research
→ Source/rights capture
→ Script
→ Independent fact-check for factual content
→ Storyboard
→ Shot list
→ Scene DAG
→ Parallel asset generation
→ Voice/audio generation
→ Non-destructive edit
→ Subtitles/captions
→ Preview render
→ Media QA
→ Final render
→ Human publish approval

## Scene model

Each scene owns:
- scene index
- script
- timing
- storyboard
- prompts/generation specs
- source references
- assets
- checkpoint
- QA status

Independent scenes may fan out in parallel.

GPU-heavy generation still obeys central resource admission.

## Provenance

Every externally sourced or generated asset stores:
- source_kind
- source reference
- generation metadata
- model/engine identity where applicable
- license/attribution metadata where applicable
- checksum
- derivation lineage where applicable

## Documentary integrity

Factual documentary content requires:
- source list;
- claim-to-source traceability for important claims;
- independent fact-check;
- unresolved uncertainty surfaced;
- final factual QA before render.

## Non-destructive editing

Source assets are immutable.
Edits create derived versions/manifests.
Final output can be traced back to source assets and scene decisions.

## Long-running jobs

Required:
- progress events;
- checkpointing where engine supports it;
- scene-level resumability;
- cancellation;
- retry budget;
- no full-project restart for one failed scene when avoidable.

## Render verification

Before READY:
- all required scenes present;
- no missing asset refs;
- audio stream present when required;
- duration plausible;
- subtitle file structurally valid when required;
- output file readable;
- checksum recorded.

## Publishing

Rendering and publishing are separate actions.

The platform may render automatically.
External publishing remains explicit human approval unless the user changes that policy.
