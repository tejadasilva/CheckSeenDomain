def get_domain(url_2_check, domains_seen):
    domain_list = []
    for url in url_2_check:
        splitted = url.split(".")
        pos=len(splitted)-2
        domain=splitted[pos].lower()
        
        if domain == 'gov' or domain == 'com' or domain == 'co':
            pos -= 1
            domain=splitted[pos].lower()
            seen = False
            for x in domains_seen:
                if domain == x:
                    seen = True
                    break
            print('{}, {}, {}'.format(url, domain, seen))    
        else:
            seen = False
            for x in domains_seen:
                if domain == x:
                    seen = True
                    break
            print('{}, {}, {}'.format(url, domain, seen))


if __name__ == "__main__":

    with open('global_Always_Allow.txt') as file1:
        url_2_check=file1.read().splitlines()

    with open('WebInsight.txt') as file2:
        domains_seen=file2.read().splitlines()


    print("url, domain, seen")
    get_domain(url_2_check, domains_seen)


            