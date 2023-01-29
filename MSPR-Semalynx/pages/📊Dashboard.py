import streamlit as st
from streamlit_elements import elements, mui
import os, requests, socket, subprocess, pandas, time, paramiko

st.title("Dashboard")

#scan = "python3 script/scan.py"

#def run_script():
#    process = subprocess.Popen(scan.split(), stdout=subprocess.PIPE)
#    while True:
#        output = process.stdout.readline()
#        if output == b'' and process.poll() is not None:
#            break
#        if output:
#            st.write(output.strip())
#
#if st.button("Run script"):
#    run_script()

# ========== Main ==============
# =========== PING ===============
col1,col2,col3,col4 = st.columns(4)

with col1:
    st.subheader("Hostname:")
    hostname = socket.gethostname()
    st.write(hostname)
with col2:
    st.subheader("IP Local:")
    ip_address = socket.gethostbyname(hostname)
    st.write(ip_address)

# Public ip 
def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    if response.status_code == 200:
        return response.json()['ip']
    else:
        st.warning("Échec" + response.status_code)

# Print public ip

# iping = {
#     "ippublic": get_public_ip(),
#     "iplocal": socket.gethostbyname(hostname),
#     "hostname": socket.gethostname(),
#     "dns": socket.getfqdn(hostname)
# }


# st.json(iping)
with col3:
    st.subheader("IP Publique:")
    ip = get_public_ip()
    st.write(ip)

# Hostname domain name dns
with col4:
    st.subheader("DNS:")
    hostname = socket.gethostname()
    fqdn = socket.getfqdn(hostname)
    st.write(fqdn)

# =========== PING ===============

# ===== Verification réseau ======
col1,col2 = st.columns(2)
with col1:
    st.subheader("Statut internet :")
    result = subprocess.run(["ping", "-c", "1", "8.8.8.8"], capture_output=True, text=True)
    if "1 packets transmitted, 1 received" in result.stdout:
        st.success("Connexion Internet établie")
    else:
        st.error("Connexion Internet non établie")

# ===== Verification réseau ======

# ======== Separation ============

st.markdown("---")

# ======== Separation ============

exec_clear = False

if st.button("CLEAR Interface"):
    exec_clear = True

# ========= Semabox Reboot ==============
IP = st.text_input("IP :")

def run_reboot(ip):
    os.system("ssh -t root@"+ ip +" shutdown -r now")

def run_ping(ip):
    result = subprocess.run(["ping", "-c", "1", ip], capture_output=True, text=True)
    if "1 packets transmitted, 1 received" in result.stdout:
        st.success("Semabox statut OK")
    else:
        st.error("Connexion avec la Semabox non établie")

col1,col2 = st.columns(2)
with col1:
    if st.button("Reboot"):
        run_reboot(IP)
        st.success("La Semabox va redémarer")

# ========= Semabox ==============
with col2:
    if st.button("Ping"):
        run_ping(IP)

# ========= Main ===============

# =========== CLEAR ==============
def clear():
    st.text("")
# ========== Button ==============
if exec_clear == True:
    clear()
    exec_clear = False
# ========== Button ==============