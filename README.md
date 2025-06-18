<h1 align="center">QuoteSpark</h1>

<p align="center">
  <a href="https://waveassist.io/assistant/quotespark-template">
    <img src="https://img.shields.io/badge/Deploy_with-WaveAssist-007F3B" alt="Deploy with WaveAssist" />
  </a>
  <img src="https://img.shields.io/badge/QuoteSpark-Daily%20Inspiration%20Quote-blue" alt="QuoteSpark Badge" />
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License" />
  </a>
</p>

---

## Overview

Fetches a random quote from Quotable and emails it with the author line.

QuoteSpark runs on [WaveAssist](https://waveassist.io) and sends you a daily inspiration quote to start your workday.

---

## One-Click Deploy on WaveAssist (Recommended)

<p>
  <a href="https://waveassist.io/assistant/quotespark-template" target="_blank">
    <img src="https://waveassistapps.s3.us-east-1.amazonaws.com/public/Button.png" alt="Deploy on WaveAssist" width="230" />
  </a>
</p>

Deploy QuoteSpark instantly on [WaveAssist](https://waveassist.io)—a zero-infrastructure automation platform that handles orchestration, scheduling, secrets, and hosting for you.

> 🔐 You may be prompted to log in or create a free WaveAssist account before continuing.

#### How to Use:

1. Click the button above or go to [waveassist.io/assistant/quotespark-template](https://waveassist.io/assistant/quotespark-template)
2. Run the starting node:
   1. **quote_fetcher**: Fetches a random quote from the Quotable API.
3. Monitor logs to ensure the quote is fetched successfully.
4. Click **Deploy** to schedule this automation and run it daily.

✅ You’re now running QuoteSpark on autopilot.

---

## Manual Deployment

Clone this repo and use your preferred scheduler such as:

Scripts:
* `quote_fetcher.py`
* `daily_inspiration_email_sender.py`

> _No external Python package requirements listed in this template._

---

## Features

* **quote_fetcher (QuoteFetcher):**
  Fetches a random quote from the Quotable API to provide daily inspiration.
* **daily_inspiration_email_sender (DailyInspirationEmailSender):**
  Sends the fetched quote and author line as a plain-text email.
* **Processing Variables:**
  * `quote_data` — stores the data of the fetched quote

---

Built with ❤️ by the WaveAssist team. Want help or integrations? [Say hello](https://waveassist.io).
