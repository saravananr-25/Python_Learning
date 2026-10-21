# Resume vs JD Analyzer (n8n)

An n8n workflow that compares a resume against a job description and returns a fit analysis: a 1–10 fit score, matching and missing skills, a short summary, and the top 3 improvements to make to the resume.

## How it works

```
n8n Form Trigger → Extract from File → Basic LLM Chain → Google Sheets → Form
                                         ├─ OpenAI Chat Model (gpt-4o-mini)
                                         └─ Structured Output Parser
```

| Node | What it does |
|------|--------------|
| **n8n Form Trigger** | Web form that collects Name, Email (optional), Resume (PDF) and Job Description |
| **Extract from File** | Pulls the text out of the uploaded PDF resume |
| **Basic LLM Chain** | Prompts the model, acting as a technical recruiter, to compare the resume with the JD |
| **OpenAI Chat Model** | `gpt-4o-mini` at temperature 0.2 |
| **Structured Output Parser** | Makes the model return JSON with `name`, `matching_skills`, `missing_skills`, `fit_score`, `top_3_improvements` and `summary` |
| **Google Sheets** | Adds one row per analysis so you have a log of all runs |
| **Form** | Shows the result to the user: fit score, summary, missing skills and top 3 improvements |

## Prerequisites

- n8n (latest version) running locally at http://localhost:5678
- An OpenAI API key
- A Google account with a Google Sheet to log results to

## Setup

1. **Import the workflow.** In n8n, go to **Workflows → Import from File** and pick `workflows/resume-analyzer.json`.
2. **Attach the OpenAI credential.** Open **OpenAI Chat Model** and select or create an OpenAI API credential.
3. **Prepare the Google Sheet.** Create a sheet whose first row has these headers:

   | Timestamp | Name | Email | Fit Score | Matching Skills | Missing Skills | Summary |
   |-----------|------|-------|-----------|-----------------|----------------|---------|

4. **Configure Google Sheets.** Open the **Google Sheets** node, attach a Google Sheets OAuth2 credential, then pick your document and sheet from the dropdowns.
5. **Save** the workflow.

The JSON doesn't contain any credentials or API keys. You attach them in n8n after you import the workflow.

## Usage

- **Testing:** open the **n8n Form Trigger** node, click **Test step**, then open the **Test URL** (`http://localhost:5678/form-test/...`).
- **Production:** activate the workflow and use the **Production URL** (`http://localhost:5678/form/...`).

Fill in the form, upload a PDF resume and paste the job description. The analysis appears on the completion page and a row is added to your sheet.

## Notes

- The resume must be a **PDF with selectable text**. Scanned or image-only PDFs extract no text and give poor results.
- If you want a different model, change it in the **OpenAI Chat Model** node.

## Files

```
Resume_Analyzer/
├── CLAUDE.md                      # Project guidelines
├── README.md
└── workflows/
    └── resume-analyzer.json       # Importable n8n workflow
```
