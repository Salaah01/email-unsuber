# Collect Unsubscribe Links (In Development)
## Description
This program will parse through your emails and collect a list of unsubscribe links and output them into a CSV, XLSX (Excel) or JSON.

Unlike some tools which you may come across on the internet we do not store any of your details, and this is why this tool needs to be downloaded and run manually.

The program will require you to enter your email address and password and then will parse through each email in your inbox looking for unsubscribe links. It will collect each link and output them into a file.

The program will not however click on each link for you attempting to unsubscribe on your behalf. This is done purely to prevent clicking on unsafe links. The file therefore will contain the sender email as well to help you search for the email should you wish to check the email before clicking on any link.

## Installation
|Platform|Method|
-- | --
| Windows | Download and run email-unsuber.exe |
| Mac | Not supported yet |
| Linux (Debian) | Download and run email-unsuber.deb |

### Running from Source
If you wish to run the program directory without running a binary, please follow the instructions below. The only requirement is Python3.

1. Fork and clone the directory.
2. `cd src`
3. Create a virtual environment (e.g: `python3 -m venv venv`)
4. Activate virtual environment.
  Windows: `venv\Scripts\activate`
  Linux: `. venv/bin/activate`
5. `pip install -r requirements.txt`
6. `python collect_unsubs.py`

The program will require some arguments to be set when running the program. 
```bash
  -h, --help            show this help message and exit
  -e EMAIL, --email EMAIL
                        Email address
  -c EMAIL_ENV, --email-env EMAIL_ENV
                        Name of environment variable containing the email address
  -d EMAIL_FILE, --email-file EMAIL_FILE
                        Path to file containing email address.
  -p PASSWORD_ENV, --password-env PASSWORD_ENV
                        Name of environment variable containing password.
  -f PASSWORD_FILE, --password-file PASSWORD_FILE
                        Path to file containing password.
  -t {csv,xlsx,json}, --filetype {csv,xlsx,json}
                        Output file type.
  -o OUTPUT_DIRECTORY, --output-directory OUTPUT_DIRECTORY
                        Directory of where the file should be stored.
```

## Supported Mail Servers
* Gmail
* Outlook/Hotmail
* Yahoo

Don't see your mailing server on the list? Create an issue with the mailing server you would like support for and I'll do my best to include it.


## Troubleshooting
### My password does not work
Because this program needs something called programmatic access, your mailing server may not allow your "normal" password to work. You would need to create a developer/application password for your mailing client.
 
This can be a bit frustrating, I know. But I am adamant to make this tool one where you have full control of your data and account. There is a way around it, but it would mean that I would need to host the tool online somewhere, and I would need to request your mailing server to provide me with information relating to your inbox. Yes, that would mean that I could potentially read your emails. Yikes! Let's be honest, you don't want that do you?
 
The option to create the application password should be in your security options, if you need help, please raise an issue and I'll do my best to help you.
