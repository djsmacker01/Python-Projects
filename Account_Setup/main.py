import json

x = input("1. Remove account  2. Add Interest: ")
if x == "1":
    with open("Data/accounts.json", "r+") as infile:
        accounts = json.load(infile)
    idToRemove = int(input("Enter the ID of the account to remove: "))
    for Account in accounts:
        if Account["id"] == idToRemove:
            accounts.remove(Account)
    with open("Data/accounts_updated.json", "w") as outfile:
        accs_as_json = json.dumps(accounts, indent=4)
        outfile.write(accs_as_json)
elif x == "2":
                with open("Data/accounts.json", "r+") as infile:
                    ACCOUNTS = json.load(infile)
                interest_rate = float(input("Enter an interest rate e.g. 2.5: "))
                for acc in ACCOUNTS:
                    acc["balance"] *= (1 + (interest_rate/100))
                with open("Data/accounts_with_interest.json", "w") as outfile:
                    accounts_converted_to_json_format_ = json.dumps(ACCOUNTS, indent=4)
                    outfile.write(accounts_converted_to_json_format_)