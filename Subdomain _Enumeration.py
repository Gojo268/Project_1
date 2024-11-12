import requests

def request(url):
    try:
        result = requests.get("https://" + url)
        if(result):
            print("[+] Subdomain Discovered ----------> " + url)
    except:
        pass


def main():
    target_url = "facebook.com"
    #open subd list
    with open("subdomains-10000.txt", "r") as wordlist:
        for line in wordlist:
            word = line.strip()
            test_url = word + "." + target_url
            request(test_url)

main()