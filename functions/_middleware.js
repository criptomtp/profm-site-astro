// Content negotiation: when an agent sends Accept: text/markdown,
// serve the pre-generated .md twin of the HTML page (via dual-md integration).
//
// - Browsers (Accept: text/html, */*) → unchanged HTML response
// - Agents (Accept: text/markdown)     → redirect to /path/index.md
// - Vary: Accept ensures correct caching on CF edge

const SKIP_PREFIXES = [
  '/api/',
  '/.well-known/',
  '/_headers',
  '/_redirects',
  '/robots.txt',
  '/sitemap',
  '/files/',
  '/admin/',
  '/thanks/',
  '/schedule/',
  '/new/',
];

export async function onRequest({ request, next }) {
  const url = new URL(request.url);
  const accept = request.headers.get('Accept') || '';

  const wantsMarkdown =
    /\btext\/markdown\b/i.test(accept) &&
    !/\btext\/html\b/i.test(accept); // browsers always send html too → not an agent

  const isPageRequest =
    request.method === 'GET' &&
    !url.pathname.endsWith('.md') &&
    !url.pathname.endsWith('.xml') &&
    !url.pathname.endsWith('.txt') &&
    !url.pathname.endsWith('.json') &&
    !url.pathname.match(/\.(js|css|png|jpg|jpeg|webp|svg|ico|woff2?)$/i) &&
    !SKIP_PREFIXES.some(p => url.pathname.startsWith(p));

  if (wantsMarkdown && isPageRequest) {
    const mdPath = url.pathname.endsWith('/')
      ? `${url.pathname}index.md`
      : `${url.pathname}/index.md`;

    const mdUrl = new URL(mdPath, url.origin);
    const mdResp = await fetch(mdUrl, { headers: { 'Accept': 'text/markdown' } });

    if (mdResp.ok) {
      const body = await mdResp.text();
      const headers = new Headers(mdResp.headers);
      headers.set('Content-Type', 'text/markdown; charset=utf-8');
      headers.set('Vary', 'Accept');
      headers.set('X-Served-As', 'markdown');
      const tokens = body.length; // rough token estimate (chars, not BPE)
      headers.set('X-Markdown-Tokens', String(Math.ceil(tokens / 4)));
      return new Response(body, { status: 200, headers });
    }
  }

  const response = await next();

  // Advertise markdown availability on HTML responses
  const ct = response.headers.get('Content-Type') || '';
  if (isPageRequest && ct.includes('text/html')) {
    const newHeaders = new Headers(response.headers);
    const existingVary = newHeaders.get('Vary');
    newHeaders.set('Vary', existingVary ? `${existingVary}, Accept` : 'Accept');
    const mdPath = url.pathname.endsWith('/')
      ? `${url.pathname}index.md`
      : `${url.pathname}/index.md`;
    const existingLink = newHeaders.get('Link');
    const mdLink = `<${mdPath}>; rel="alternate"; type="text/markdown"`;
    newHeaders.set('Link', existingLink ? `${existingLink}, ${mdLink}` : mdLink);
    return new Response(response.body, {
      status: response.status,
      statusText: response.statusText,
      headers: newHeaders,
    });
  }

  return response;
}
