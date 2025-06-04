# VaultWeaver 🧠🔍

**VaultWeaver** is a surgical recon + CVE-aware sniper tool designed for bug bounty hunters and red teamers.

## 💡 Features

- 🔎 Subdomain + HTTPX Probing
- 🧬 CVE-Aware Matching (based on endpoint behavior & tech stack)
- 🕵️‍♂️ Stealth Mode with randomized headers and delays
- 🌐 Webhook Integration (Discord, Slack, etc.)

## 📦 Usage

```bash
python3 vaultweaver.py --target tesla.com --vault-aware --stealth --webhook https://your.url
