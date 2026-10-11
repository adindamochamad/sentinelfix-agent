# Building in public — #neatHack

Bobot **15%**. Post selama **10–12 Okt**, bukan hanya Senin malam.

## Siap tempel (belum dipublish — plugin X tidak bisa membuat post)

Post 1:

```
#neatHack SentinelFix: demo /health was HTTP 503 (legacy_health_code returned 500).
The agent read the service and demo_service/.env, set the health token, and the next check was HTTP 200.
Prompt does not contain the token value. Repo: https://github.com/adindamochamad/sentinelfix-agent
```

Post 2:

```
#neatHack day 2 update: that 503→200 run did not take a wrong code patch first. It diagnosed config from the source.
Next gap for judges is the neatlogs trace URL plus an Entire checkpoint, not another feature.
```

## Template post 1 (hari 1)

```
Building for #neatHack: SentinelFix — an agent that doesn't stop at "looks fixed."
Goal: reproduce failure → patch → verify until health checks pass.
Today: wired @neatlogs traces on every tool call.
Repo: https://github.com/adindamochamad/sentinelfix-agent
```

## Template post 2 (failure)

```
#neatHack day 2: first patch made tests worse — trace shows wrong assumption on env var.
Using @Entire checkpoint to roll back agent context before retry.
Screenshot: [neatlogs trace link]
```

## Template post 3 (economics / launch)

```
#neatHack: unit economics for autonomous stabilization minutes — modeled in @cfo_ai.
Demo almost ready: verify loop + recovery on injected fault.
```

## Aturan

- Engagement asli; no bots / bought likes (DQ)
- Balas pertanyaan di thread — kualitas > follower count
- Simpan URL setiap post di [EVIDENCE.md](./EVIDENCE.md)
