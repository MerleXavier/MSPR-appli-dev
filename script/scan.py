import nmap

# Création d'un objet nmap.PortScanner()
nm = nmap.PortScanner()

# Lancement d'un scan sur un réseau
nm.scan('192.168.1.0/24', '1-1024')

# Boucle sur les hôtes du réseau
for host in nm.all_hosts():
    print('Hôte : %s (%s)' % (host, nm[host].hostname()))
    # Boucle sur les ports ouverts de l'hôte
    for proto in nm[host].all_protocols():
        lport = nm[host][proto].keys()
        for port in lport:
            if nm[host][proto][port]['state']== 'open':
                print ('port : %s\tétat : %s' % (port, nm[host][proto][port]['state']))