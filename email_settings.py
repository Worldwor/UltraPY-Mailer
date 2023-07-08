from threading import Semaphore

# SMTP server settings
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# Sender email settings
SENDER_EMAIL_FILE = 'sender_emails.txt'  # Path to the file containing sender email addresses
SENDER_NAME_FILE = 'sender_names.txt'
SENDER_USERNAME = 'info@example.com'
SENDER_PASSWORD = 'Password2311'

# Reply-to email settings
ENABLE_REPLY_TO = False
REPLY_TO_EMAIL = 'replto@example.com'

# Define the email address for sending test emails
TEST_EMAIL_ADDRESS = 'test@example.com'

# Flag to enable/disable sending test emails
ENABLE_TEST_EMAILS = False

# Number of emails to send before sending a test email
NUM_EMAILS_FOR_TEST = 1

# Proxy settings
ENABLE_PROXY = True
PROXY_PROTOCOL = 'socks5'  # or 'http 0r https/socks5 or socks4
PROXY_HOST = '169.239.205.61'
PROXY_PORT = 30494
PROXY_USERNAME = 'UserSocks5'
PROXY_PASSWORD = 'fWp0MHJnw3'

# Office 365 SMTP settings
ENABLE_OFFICE_SMTP = False
OFFICE_SMTP_SERVER = 'smtp.office365.com'
OFFICE_SMTP_PORT = 587
OFFICE_SMTP_USERNAME = 'info@example.com'
OFFICE_SMTP_PASSWORD = 'Password2311'

# SMTP authentication flags
ENABLE_SMTP_AUTH = False
ENABLE_NON_OFFICE_SMTP_AUTH = False  # Add this flag for non-Office SMTP authentication

# Use recipient's MX server
USE_RECIPIENT_MX = False

# Enable or disable using recipient's email as the sender's email
ENABLE_RECIPIENT_AS_SENDER = False

# Enable or disable fake names
ENABLE_FAKE_NAMES = True

# TLS and SSL settings
ENABLE_TLS = True
ENABLE_SSL = False

# Retry settings
MAX_RETRIES = 10000000000
RETRY_DELAY = 0

# Test interval settings
ENABLE_TEST_INTERVAL = True
TEST_INTERVAL = 1000

# File paths
SENT_EMAILS_FILE = 'successful_sent_emails.txt'
FAILED_EMAILS_FILE = 'failed_emails.txt'
RECIPIENT_LIST_FILE = 'recipient_list.txt'
ATTACHMENT_FILE = 'attachment.html'
HTMLTOIMAGE_FILE = 'htmltoimage.html'
HTML_TO_PDF_FILE = 'htmltopdf.html'

# Max connection limit
MAX_CONNECTIONS = 5
connection_semaphore = Semaphore(MAX_CONNECTIONS)

# Set the number of threads for parallel sending
NUM_THREADS = 50

# Highest priority flag
HIGHEST_PRIORITY = True

# Enable or disable attachment
ENABLE_ATTACHMENT = False
# Enable or disable html to pdf
ENABLE_HTML_TO_PDF = False

# Enable or disable HTML to image conversion
ENABLE_CID_IMAGE = False

ENABLE_CC = False
CC_RECIPIENTS = ['Example Recipients <recipients@example.com>']

# License Key
LICENSE_KEY = "098f956796d07f7ebe0a3f2e99ff5c1c7eef5ada"

# Machine IP
MACHINE_IP = '102.83.291.1.0'

# Encoding type
ENCODING_TYPE = 'utf-8'

# Charset setting
CHARSET = 'utf-8'

# Time Zone setting
TIME_ZONE = 'America/New_York'