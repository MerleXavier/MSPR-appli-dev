import streamlit as st
from streamlit_elements import elements, mui
import os, requests, socket, subprocess, pandas

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

# ======== Separation ============

st.markdown("---")

# ======== Separation ============

exec_nmap = False
exec_speedtest = False
exec_clear = False

col1,col2,col3 = st.columns(3)
with col1:
    if st.button("Run Speedtest"):
        exec_speedtest = True
with col2:
    if st.button("Run NMAP"):
        exec_nmap = True
with col3:
    if st.button("CLEAR"):
        exec_clear = True

# ========= Main ===============


# =========== NMAP ==============

scan = "python3 script/scan.py"
scan_output = "scan_output.txt"

def run_scan():
    process = subprocess.Popen(scan.split(), stdout=subprocess.PIPE)

    while True:
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if output:
            print(output.strip())

    with open("scan_output.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if "open" in line:
                st.success(line)
            else:
                st.subheader(line)

# =========== NMAP ===============

# ======== SPEEDTEST =============

def run_speedtest():
    os.system("python3 script/speedtest.py")

    st.header("Speedtest :")

    with open("result.txt", "r") as f:
        ltests = f.readlines()
        col1,col2 = st.columns(2)
        with col1:
            st.subheader("↓ " + ltests[0])
        with col2:
            st.subheader("↑ " + ltests[1])

# ======== SPEEDTEST =============

# =========== CLEAR ==============
def clear():
    st.text("")
# ========== Button ==============
if exec_nmap == True:
    run_scan()
    exec_nmap = False

if exec_speedtest == True:
    run_speedtest()
    exec_speedtest = False

if exec_clear == True:
    clear()
    exec_clear = False
# ========== Button ==============