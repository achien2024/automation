# Membership Dues Reminder Script

This script helps you send email reminders to members who have not yet paid their membership dues. It interacts with an Excel workbook tracking payment status and uses SMTP to send emails.

---

## 📦 Important Libraries to Install

Before running the script, install the following Python libraries:

```bash
pip3 install openpyxl
```

## Instructions
* ensure that the excel workbook follows the exact format as the example workbook given, should be clear on what data to input, and indexing (column numbers) should be followed exactly
* in line 81, I used my own name. Feel free to replace it with anything else or to change the body itself
* for the workbook, ensure that the script and workbook are in the same file directory, else you will need to copy paste the exact file path of the workbook
