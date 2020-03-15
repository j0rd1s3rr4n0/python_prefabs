import platform, os, smtplib

setBit = ''

# If not using gmail, change smtp server and port accordingly
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
# Be sure to enable less secure apps if using gmail!
smtpObj.login('SENDER EMAIL', 'SENDER PASS')

# Gets system info, such as name, model, etc
uname = platform.uname()
# Gets system architecture, such as x64
arch = platform.architecture()
is64Bit = platform.machine().endswith('64')

# Converting the uname variable to a string
unameStr = str(uname)
# Trimming the front
noFront = unameStr.replace("uname_result(", "")
# Trimming the end
noEnd = noFront.replace(")", "")
# Turning it into an array
unameSplit = noEnd.split(",")

# Printing to console
print()
print(unameSplit[0])
print(unameSplit[1].strip())
print(unameSplit[2].strip())
print(unameSplit[3].strip())
print(unameSplit[4].strip())
print(unameSplit[5].strip() + '\'')

# Checking system architecture
if is64Bit == True:
    setBit = 'architecture=\'x64\''
    print(setBit)
else:
    setBit = 'architecture=\'x86\''
    print(setBit)

# Sending email
smtpObj.sendmail('SENDER EMAIL', 'RECEIVER EMAIL', 'Subject: System Info\n' + unameSplit[0] + '\n' + unameSplit[1].strip() + '\n' + unameSplit[2].strip() + '\n' + unameSplit[3].strip() + '\n' + unameSplit[4].strip() + '\n' + unameSplit[5].strip() + '\'\n' + setBit)