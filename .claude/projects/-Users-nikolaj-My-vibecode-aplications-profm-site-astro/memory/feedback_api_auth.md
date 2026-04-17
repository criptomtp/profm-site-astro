---
name: Never add API auth without updating client code
description: Adding auth to API without updating CRM dashboard JS breaks the admin panel
type: feedback
---

Never add authentication (API keys, CORS restrictions) to API endpoints without simultaneously updating ALL client-side code that calls those endpoints.

**Why:** Added x-api-key requirement to /api/leads but CRM dashboard JS (public/admin/js/crm.js) didn't send the header → all leads disappeared from admin panel.

**How to apply:** Before restricting any API:
1. Find ALL files that call that API (grep for the endpoint path)
2. Update client code to send required headers
3. Verify env vars are set in Vercel BEFORE deploying
4. Test the admin panel after deploy
