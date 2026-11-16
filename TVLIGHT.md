# YouTube Glass

Fork of [webosbrew/youtube-webos](https://github.com/webosbrew/youtube-webos),
based on upstream 0.5.3. GPL-3.0-only and upstream credits remain unchanged.

The TVLight skin adds cool layered glass surfaces, rounded navigation and
thumbnails, and a scrollable settings panel. It uses no blur filter or animation
loop. Ad blocking, SponsorBlock, video quality controls and the other upstream
features remain intact. This still uses YouTube's TV web interface and contacts
YouTube/Google; SponsorBlock contacts its own service. It is not an offline or
tracking-free YouTube client.

Open options with the green remote button. Liquid Glass can be switched off
there independently of ad blocking. On remotes without colour buttons, webOS's
More Actions menu may expose them; the TVLight remote tools can also send GREEN.

Build: `pnpm install --frozen-lockfile`, `pnpm run build`, `pnpm run lint:tsc`,
`pnpm run test:compat`, `pnpm run package`.
`tools/glass-preview.html` provides a local CSS preview served from the repository
root, without connecting to YouTube. Verify the real YouTube page on the TV too.

The app keeps `youtube.leanback.v4` to retain upstream launch/casting behaviour.
The native store app must be removed before installation. Installing a newer
upstream package under that same ID would replace this fork's theme.
