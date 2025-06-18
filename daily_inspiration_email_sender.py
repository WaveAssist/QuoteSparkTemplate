import waveassist
waveassist.init("2fec42dd-492b-4294-8154-d33c3ccf", "darshika_test")

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
subject = "Daily Inspiration Quote"
email_content = f'"{quote_text}"\n\n- {author}'

# Send the email
waveassist.send_email(subject, html_content=email_content)
print(email_content)

# Store confirmation
waveassist.store_data("email_sent", True)
