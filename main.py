import sys
import psutil
import speedtest
import sounddevice as sd
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QProgressBar, QTextEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import subprocess
from pynvml import nvmlInit, nvmlDeviceGetCount, nvmlDeviceGetHandleByIndex, nvmlDeviceGetName, nvmlDeviceGetUtilizationRates, nvmlDeviceGetTemperature, NVML_TEMPERATURE_GPU
import platform
import datetime

class SystemChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.disk_label = QLabel('Disk Usage: Checking...')
        self.memory_label = QLabel('Memory Usage: Checking...')
        self.cpu_label = QLabel('CPU Usage: Checking...')
        self.smart_label = QLabel('SMART Status: Checking...')
        self.gpu_label = QLabel('GPU Status: Checking...')
        self.network_label = QLabel('Network Speed: Checking...')
        self.battery_label = QLabel('Battery Status: Checking...')
        self.uptime_label = QLabel('System Uptime: Checking...')
        self.cpu_temp_label = QLabel('CPU Temperature: Checking...')
        self.gpu_temp_label = QLabel('GPU Temperature: Checking...')
        self.system_info_label = QLabel('System Info: Checking...')
        self.audio_label = QLabel('Audio Devices: Checking...')
        self.software_label = QLabel('Installed Software: Checking...')
        self.software_list = QTextEdit()
        self.software_list.setReadOnly(True)

        self.disk_progress = QProgressBar()
        self.memory_progress = QProgressBar()
        self.cpu_progress = QProgressBar()
        self.gpu_progress = QProgressBar()

        self.setStyleSheet("QLabel { font-size: 16px; }")

        check_btn = QPushButton('Check System')
        check_btn.clicked.connect(self.check_system)
        check_btn.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px;")

        layout.addWidget(self.disk_label)
        layout.addWidget(self.disk_progress)
        layout.addWidget(self.memory_label)
        layout.addWidget(self.memory_progress)
        layout.addWidget(self.cpu_label)
        layout.addWidget(self.cpu_progress)
        layout.addWidget(self.smart_label)
        layout.addWidget(self.gpu_label)
        layout.addWidget(self.gpu_progress)
        layout.addWidget(self.network_label)
        layout.addWidget(self.battery_label)
        layout.addWidget(self.uptime_label)
        layout.addWidget(self.cpu_temp_label)
        layout.addWidget(self.gpu_temp_label)
        layout.addWidget(self.system_info_label)
        layout.addWidget(self.audio_label)
        layout.addWidget(self.software_label)
        layout.addWidget(self.software_list)
        layout.addWidget(check_btn)

        self.setLayout(layout)
        self.setWindowTitle('System Checker')
        self.setGeometry(300, 300, 600, 800)
        self.show()

    def check_system(self):
        self.check_disk()
        self.check_memory()
        self.check_cpu()
        self.check_smart()
        self.check_gpu()
        self.check_network()
        self.check_battery()
        self.check_uptime()
        self.check_cpu_temp()
        self.check_gpu_temp()
        self.check_system_info()
        self.check_audio_devices()
        self.check_installed_software()

    def check_disk(self):
        disk_usage = psutil.disk_usage('/')
        self.disk_label.setText(f'Disk Usage: {disk_usage.percent}%')
        self.disk_progress.setValue(disk_usage.percent)
        if disk_usage.percent > 90:
            self.disk_label.setStyleSheet('color: red;')
        else:
            self.disk_label.setStyleSheet('color: black;')

    def check_memory(self):
        memory_info = psutil.virtual_memory()
        self.memory_label.setText(f'Memory Usage: {memory_info.percent}%')
        self.memory_progress.setValue(memory_info.percent)
        if memory_info.percent > 90:
            self.memory_label.setStyleSheet('color: red;')
        else:
            self.memory_label.setStyleSheet('color: black;')

    def check_cpu(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        self.cpu_label.setText(f'CPU Usage: {cpu_usage}%')
        self.cpu_progress.setValue(cpu_usage)
        if cpu_usage > 90:
            self.cpu_label.setStyleSheet('color: red;')
        else:
            self.cpu_label.setStyleSheet('color: black;')

    def check_smart(self):
        try:
            smart_output = subprocess.check_output(['smartctl', '-H', '/dev/sda'])
            smart_status = "OK" if b"PASSED" in smart_output else "FAIL"
        except Exception as e:
            smart_status = f"Error: {str(e)}"
        
        self.smart_label.setText(f'SMART Status: {smart_status}')
        if smart_status != "OK":
            self.smart_label.setStyleSheet('color: red;')
        else:
            self.smart_label.setStyleSheet('color: black;')

    def check_gpu(self):
        try:
            nvmlInit()
            device_count = nvmlDeviceGetCount()
            for i in range(device_count):
                handle = nvmlDeviceGetHandleByIndex(i)
                name = nvmlDeviceGetName(handle)
                utilization = nvmlDeviceGetUtilizationRates(handle)
                self.gpu_label.setText(f'GPU: {name.decode()} Utilization: {utilization.gpu}%')
                self.gpu_progress.setValue(utilization.gpu)
                if utilization.gpu > 90:
                    self.gpu_label.setStyleSheet('color: red;')
                else:
                    self.gpu_label.setStyleSheet('color: black;')
        except Exception as e:
            self.gpu_label.setText(f'GPU Status: Error: {str(e)}')
            self.gpu_progress.setValue(0)
            self.gpu_label.setStyleSheet('color: red;')

    def check_network(self):
        try:
            st = speedtest.Speedtest()
            st.download()
            st.upload()
            download_speed = st.results.download / 1_000_000  # Convert to Mbps
            upload_speed = st.results.upload / 1_000_000  # Convert to Mbps
            self.network_label.setText(f'Network Speed: {download_speed:.2f} Mbps download, {upload_speed:.2f} Mbps upload')
            if download_speed < 5:
                self.network_label.setStyleSheet('color: red;')
            else:
                self.network_label.setStyleSheet('color: black;')
        except Exception as e:
            self.network_label.setText(f'Network Speed: Error: {str(e)}')
            self.network_label.setStyleSheet('color: red;')

    def check_battery(self):
        battery = psutil.sensors_battery()
        if battery:
            self.battery_label.setText(f'Battery: {battery.percent}% {"Plugged in" if battery.power_plugged else "Not plugged in"}')
            if battery.percent < 20 and not battery.power_plugged:
                self.battery_label.setStyleSheet('color: red;')
            else:
                self.battery_label.setStyleSheet('color: black;')
        else:
            self.battery_label.setText('Battery: Not available')
            self.battery_label.setStyleSheet('color: red;')

    def check_uptime(self):
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
        uptime = datetime.datetime.now() - boot_time
        self.uptime_label.setText(f'System Uptime: {uptime}')
        self.uptime_label.setStyleSheet('color: black;')

    def check_cpu_temp(self):
        try:
            temps = psutil.sensors_temperatures()
            cpu_temp = temps['coretemp'][0].current if 'coretemp' in temps else 'N/A'
            self.cpu_temp_label.setText(f'CPU Temperature: {cpu_temp}°C')
            if cpu_temp != 'N/A' and cpu_temp > 80:
                self.cpu_temp_label.setStyleSheet('color: red;')
            else:
                self.cpu_temp_label.setStyleSheet('color: black;')
        except Exception as e:
            self.cpu_temp_label.setText(f'CPU Temperature: Error: {str(e)}')
            self.cpu_temp_label.setStyleSheet('color: red;')

    def check_gpu_temp(self):
        try:
            nvmlInit()
            device_count = nvmlDeviceGetCount()
            for i in range(device_count):
                handle = nvmlDeviceGetHandleByIndex(i)
                temp = nvmlDeviceGetTemperature(handle, NVML_TEMPERATURE_GPU)
                self.gpu_temp_label.setText(f'GPU Temperature: {temp}°C')
                if temp > 80:
                    self.gpu_temp_label.setStyleSheet('color: red;')
                else:
                    self.gpu_temp_label.setStyleSheet('color: black;')
        except Exception as e:
            self.gpu_temp_label.setText(f'GPU Temperature: Error: {str(e)}')
            self.gpu_temp_label.setStyleSheet('color: red;')

    def check_system_info(self):
        system_info = platform.uname()
        self.system_info_label.setText(f'System Info: {system_info.system} {system_info.node} {system_info.release} {system_info.version} {system_info.machine}')
        self.system_info_label.setStyleSheet('color: black;')

    def check_audio_devices(self):
        try:
            devices = sd.query_devices()
            device_info = "\n".join([f"{i}: {d['name']}" for i, d in enumerate(devices)])
            self.audio_label.setText(f'Audio Devices:\n{device_info}')
            self.audio_label.setStyleSheet('color: black;')
        except Exception as e:
            self.audio_label.setText(f'Audio Devices: Error: {str(e)}')
            self.audio_label.setStyleSheet('color: red;')

    def check_installed_software(self):
        try:
            if sys.platform == "win32":
                installed_software = subprocess.check_output(['wmic', 'product', 'get', 'name'])
                software_list = installed_software.decode().split('\r\r\n')
                self.software_list.setText("\n".join(software_list))
                self.software_label.setText('Installed Software:')
                self.software_label.setStyleSheet('color: black;')
            else:
                self.software_label.setText('Installed Software: Not available for this OS')
                self.software_label.setStyleSheet('color: red;')
        except Exception as e:
            self.software_label.setText(f'Installed Software: Error: {str(e)}')
            self.software_label.setStyleSheet('color: red;')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SystemChecker()
    sys.exit(app.exec_())
