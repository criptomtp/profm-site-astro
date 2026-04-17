---
name: Always push after changes
description: User expects git push after every change — don't wait for explicit request
type: feedback
---

Always push changes to remote after committing. Don't wait for the user to ask — they expect changes to deploy immediately via Vercel.

**Why:** The site is deployed on Vercel which auto-deploys from main. Unpushed changes = no deploy = wasted time.
**How to apply:** After any code change, commit and push in one flow. User confirmed: "No zwyczajno zawżdy pusz" (always push).
