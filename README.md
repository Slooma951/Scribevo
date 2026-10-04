# Scribevo

**Writing help that understands how you spell.**

A Chrome extension by **Salem Elatrash**, developed from the **WordFlow** final-year research project at TU Dublin. Scribevo supports writers with dyslexia by suggesting sentence corrections they can review and accept.

[Try Scribevo on the Chrome Web Store](https://chromewebstore.google.com/detail/pfpakhloamdgoiokaljdfhpgkbanccci) · [Read the full case study](https://slooma951.github.io/portfolio/case-studies/scribevo.html)

![Prepared Scribevo correction example](assets/preview.png)

*Prepared product example, not a universal correction guarantee.*

![Scribevo workflow: write, request support, review and accept or dismiss](assets/scribevo-flow.svg)

## The problem

A person can know what they want to say without knowing the expected spelling. Sound-based spelling, missing letters and swapped letters can make ordinary dictionary suggestions frustrating. Students then have to manage spelling alongside expressing their ideas.

## What it does

- Suggests sentence corrections in supported browser text fields.
- Handles phonetic spellings, missing or swapped letters, apostrophes and some grammar errors.
- Shows the proposed change before the writer accepts it.
- Offers a dictionary searchable by an approximate spelling.
- Provides controls to pause help globally or on a particular site.

> Illustrative example: `i realy wnt to fon my freind` → `I really want to phone my friend.`
>
> This is a prepared example, not a universal accuracy claim.

## My contribution

I developed the original WordFlow research prototype, prepared a 6,571-pair training dataset, worked with a T5-based model using PyTorch and Hugging Face Transformers, and connected it to a JavaScript extension and a Python FastAPI service. Four participant sessions informed the prototype work.

The later Scribevo product uses a rule layer with AI-assisted correction. Its implementation has evolved beyond the original T5 prototype. AI coding assistance was used during later engineering and verification work.

## Evidence and current status

| Evidence | Scope and limits |
| --- | --- |
| Published extension | Live listing checked 3 October 2026: **Scribevo v2.0.0**, updated 28 September 2026. |
| Fresh release checks | 3 October 2026: **244 backend + 54 extension tests passed** in a release checkout. This does not establish support for every browser editor. |
| Rules-only evaluation | **70/70 already-correct sentences preserved**; **3% harmful edits** on a separate 200-example held-out set. The provider-assisted stage was not evaluated in this run. |
| Research history | 6,571 training pairs and four participant sessions belong to the academic prototype. Original training and participant work were not rerun in the fresh check. |

## Why it matters

The intended benefit is helping students express an idea with less spelling friction while retaining control over the wording. Improved grades or learning outcomes have not been demonstrated by the current evaluation. More participant work is needed.

## High-level engineering

Browser interface → sentence check → reviewable suggestion → accept or dismiss.

**Technologies:** JavaScript, Chrome Manifest V3, Python, FastAPI; PyTorch and Hugging Face Transformers in the research prototype.

The emphasis is on reviewable edits, measurement of harmful changes and clear differences between research results and current product behaviour.

## Privacy and limitations

The published listing says the AI stage processes the sentence through **Groq in the United States**. No account is required. Cloud processing is a meaningful trade-off; read the [product privacy policy](https://slooma951.github.io/projectweb/scribevo/privacy.html).

Context-dependent tense remains difficult. Editor behaviour varies, and automated tests do not replace real-site checks. No universal correction guarantee is made.

## About this repository

This is a **public project showcase**, not the product source repository. It contains an explanation, prepared product screenshot and original conceptual diagram. Private code, datasets, trained artefacts, credentials, endpoint configuration and implementation history are excluded.

Public descriptions demonstrate the work but cannot prevent independent implementation of a similar idea. No licence to the private implementation is granted by this showcase.
