import waveassist
waveassist.init()

# Fetch the quote data from the previous node
quote_data_list = waveassist.fetch_data("quote_data") or []

# Extract the first quote safely
if quote_data_list and isinstance(quote_data_list, list):
    quote_item = quote_data_list[0]
    quote_text = quote_item.get("q", "")
    author = quote_item.get("a", "Unknown")
else:
    quote_text = "Be yourself; everyone else is already taken."
    author = "Oscar Wilde"

# Create email content
subject = "🌟 Your Daily Inspiration"

email_content = f"""
<div style="font-family: Georgia, serif; padding: 16px; color: #333;">
  <blockquote style="font-size: 20px; font-style: italic; margin: 0 0 12px 0; border-left: 4px solid #ccc; padding-left: 12px;">
    “{quote_text}”
  </blockquote>
  <p style="text-align: right; font-size: 16px; margin: 0;">– {author}</p>
</div>
"""

waveassist.send_email(
    subject=subject,
    html_content=email_content.strip()
)

# Store confirmation
waveassist.store_data("email_sent", True)
