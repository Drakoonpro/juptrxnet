# Prompt the user for input
wallet_address = input("Your TRX Wallet Address and username eg xxxxxxx.drakoon: ")

# Download the xmrig release
!wget https://github.com/xmrig/xmrig/releases/download/v6.14.1/xmrig-6.14.1-linux-x64.tar.gz

# Extract the downloaded file
!tar -zxvf xmrig-6.14.1-linux-x64.tar.gz

# Change directory to the extracted folder
%cd xmrig-6.14.1

# Clear the cell output (if needed)
from IPython.display import clear_output
clear_output()

# Run the xmrig command
!./xmrig -o rx.unmineable.com:80 -u TRX:{wallet_address}#yrmz-i60r.100001 -p x --coin monero -a rx/1,n=I_TA_VPS,o=VPS -k -t 8
