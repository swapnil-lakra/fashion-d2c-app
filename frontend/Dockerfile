FROM oven/bun:latest AS builder

WORKDIR /app

COPY package.json bun.lock ./
RUN bun install --freeze-lockfile

COPY . .

RUN echo "import type { NextConfig } from \"next\";\n\nconst nextConfig: NextConfig = {\n  output : \"standalone\"\n};\n\nexport default nextConfig;" > next.config.ts

RUN bun run build

FROM oven/bun:latest AS runner

WORKDIR /app

COPY --from=builder /app/.next/standalone ./
COPY --from=builder /app/.next/static ./next/static
COPY --from=builder /app/public ./public

EXPOSE 3000

ENV NODE_ENV=production
ENV PORT=3000
ENV HOSTNAME="0.0.0.0"

CMD ["bun","run","server.js"]

