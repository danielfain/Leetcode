def numUniqueEmails(emails):
  validEmails = []

  for email in emails:
    temp = email.split('@')
    localName = ''.join([letter for letter in temp[0].split('+')[0] if not letter == '.'])
    domainName = temp[1]
    fullEmail = localName + '@' + domainName

    if not fullEmail in validEmails:
      validEmails.append(fullEmail)

  return len(validEmails)


print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))