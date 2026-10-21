# Resume vs JD Analyzer (n8n)

## Goal
Build an n8n workflow, "Resume vs JD Analyzer". It takes a resume and a job description and returns a match analysis.

## Output
- Importable n8n workflow JSON files go in `/workflows` (e.g. `workflows/resume-vs-jd-analyzer.json`).
- Each file must import cleanly through n8n's **Import from File** without manual fixes.

## Environment
- Local n8n, latest version, at http://localhost:5678
- Webhook URLs follow `http://localhost:5678/webhook/<path>` (production) or `/webhook-test/<path>` (test mode).

## Guidelines
- Keep it simple and readable. This is a live demo, so the canvas should be easy to follow on screen.
- Use standard built-in n8n nodes only. No community nodes.
- Give each node a clear, descriptive name (e.g. "Receive Resume & JD", "Analyze Match").
- Keep the node count small and the flow linear left-to-right where possible.
- Don't hardcode credentials or API keys in the JSON. Reference n8n credentials by name and leave them for the user to attach after import.
- Use current node type versions for the latest n8n.
