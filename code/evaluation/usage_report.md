# Model usage report

No final full-dataset model run has been performed for this checkout yet.

Before submission, run the final local Ollama command below. It overwrites
this file with the provider, model, call count, input/output token totals,
average tokens per request, and local-runtime cost estimate for that exact run:

```text
python code/main.py --llm-provider ollama --write-output output.csv --write-usage-report code/evaluation/usage_report.md
```
