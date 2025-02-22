from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/configure', methods=['POST'])
def configure():
    ssid = request.form['ssid']
    psk = request.form['psk']
    
    # 写入wpa_supplicant配置
    with open('/etc/wpa_supplicant/wpa_supplicant.conf', 'a') as f:
        f.write(f'\nnetwork={{\n\tssid="{ssid}"\n\tpsk="{psk}"\n}}\n')
    
    # 重启网络服务
    subprocess.run(['sudo', 'systemctl', 'restart', 'dhcpcd'])
    return "配置成功！请重新连接新WiFi"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)