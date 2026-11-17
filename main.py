#!/usr/bin/env python3
"""Write entry.txt: a 30-day, $100-start money plan for an AI agent."""

import os

LINES = [
    "Sell: rescue the weakest product page of small Shopify stores. $49 fixed, live in 24h, no call, no login shared.",
    "Day 1: Code lists ~300 stores with 50+ products and thin, copy-pasted descriptions, picks each worst page, rewrites it free: title, benefit bullets, FAQ, alt text.",
    "Email the owner that before/after free, with a Stripe link: pay $49, it goes live in 24h. Edge: 1,000 agents send promises; this one sends finished work.",
    "Days 2-10: Send ~300 emails/day from a $12 domain. Deliver paid pages by template+code same day. Each delivery offers two upsells: rest of catalogue at $29/page, and a $99/mo watch rewriting new pages as they appear.",
    "Days 11-30: After 20 sold, raise page one to $79. Buy a second domain ($40) only if replies run under 2%. If sales are under 1 per 300 emails by day 10, pivot same machine to Etsy sellers.",
    "Math: 6,000 emails at 1% = 60 pages, ~$2,900 plus upsells. Likely kept: $800-1,500. $100 covers domain/email only; never ads or inventory.",
]

PLAN = "\n".join(LINES)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(PLAN.encode("utf-8"))


if __name__ == "__main__":
    main()
