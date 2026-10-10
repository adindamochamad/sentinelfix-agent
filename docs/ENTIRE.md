# Entire — checkpoints for SentinelFix

Use Entire while iterating patches with Cursor or this agent.

## Setup

1. Install CLI from https://entire.io
2. In this repo root: `entire init` (follow prompts)
3. After each patch attempt:

```bash
entire checkpoint -m "patch attempt N: <short reason>"
```

## Demo narrative (video)

- Show checkpoint after **failed** patch (tests/health still red)
- Restore context / compare `entire-graph` for files touched
- Final checkpoint when `/health` is 200

## Evidence

Paste PR or checkpoint links in [SUBMISSION_EVIDENCE.md](./SUBMISSION_EVIDENCE.md).
