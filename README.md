**UltraPY-Mailer - PY eMail Sender**
UltraPY-Mailer is a Python-based email sender tool designed to send bulk emails efficiently. It supports various SMTP server configurations, proxy settings, and email customization options. This tool allows you to send emails to multiple recipients using parallel processing for faster delivery.

**SMTP Server Settings**
SMTP_SERVER: The SMTP server address.
SMTP_PORT: The port number for the SMTP server.
SENDER_USERNAME: The username for SMTP authentication.
SENDER_PASSWORD: The password for SMTP authentication.
ENABLE_NON_OFFICE_SMTP_AUTH: Flag to enable non-Office SMTP authentication.
PROXY_SETTINGS: Proxy settings for sending emails through a proxy server.
ENABLE_OFFICE_SMTP: Flag to enable Office 365 SMTP settings.
OFFICE_SMTP_SERVER: The SMTP server address for Office 365.
OFFICE_SMTP_PORT: The port number for the Office 365 SMTP server.
OFFICE_SMTP_USERNAME: The username for Office 365 SMTP authentication.
OFFICE_SMTP_PASSWORD: The password for Office 365 SMTP authentication.
ENABLE_SMTP_AUTH: Flag to enable SMTP authentication.
USE_RECIPIENT_MX: Flag to use the recipient's MX server.
ENABLE_RECIPIENT_AS_SENDER: Flag to use the recipient's email as the sender's email.


**Connection and Threading Settings**
MAX_CONNECTIONS: Maximum number of simultaneous connections to the SMTP server.
NUM_THREADS: Number of threads for parallel sending.
HIGHEST_PRIORITY: Flag to set the highest priority for emails.

**Security Settings**
ENABLE_TLS: Flag to enable TLS encryption.
ENABLE_SSL: Flag to enable SSL encryption.

**Retry and Test Interval Settings**
MAX_RETRIES: Maximum number of retries for failed email sending.
RETRY_DELAY: Delay in seconds between retry attempts.
ENABLE_TEST_INTERVAL: Flag to enable sending test emails at regular intervals.
TEST_INTERVAL: Number of emails to send before sending a test email.

**Email Content Settings**
TEST_EMAIL_ADDRESS: Email address for sending test emails.
NUM_EMAILS_FOR_TEST: Number of emails to send before sending a test email.
TEST_EMAIL_SUBJECT: Custom subject for test emails.
TEST_EMAIL_MESSAGE: Custom message for test emails.

**Sender Name and Email Settings**
SENDER_EMAIL_FILE: File containing sender email addresses.
SENDER_NAME_FILE: File containing sender names.

**File Paths**
SENT_EMAILS_FILE: File to store successfully sent email addresses.
FAILED_EMAILS_FILE: File to store failed email addresses.
RECIPIENT_LIST_FILE: File containing recipient email addresses.

**HTML to Image Conversion Settings**
ENABLE_CID_IMAGE: Flag to enable HTML to image conversion.
HTML_IMAGE_TEMPLATE: HTML template file for image conversion.
IMAGE_CID: Content ID for the generated image.

**Attachment Settings**
ENABLE_ATTACHMENT: Flag to enable email attachments.
ATTACHMENT_FILE: File to attach to the email.

**HTML to PDF Conversion Settings**
ENABLE_HTML_TO_PDF: Flag to enable HTML to PDF conversion.
HTML_TO_PDF_FILE: HTML file to convert to PDF.
PDF_FILENAME_PREFIX: Prefix for the generated PDF filenames.

**License Key and Machine IP**
LICENSE_KEY: License key for the UltraPY-Mailer tool.
MACHINE_IP: IP address of the machine running the tool.

**Encoding, Charset, and Time Zone Settings**
ENCODING_TYPE: Encoding type for email content.
CHARSET: Charset for email content.
TIME_ZONE: Time zone for date and time-related operations.
