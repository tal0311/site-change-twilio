import requests
import time
from bs4 import BeautifulSoup
import twilo_service

class Site:
    def __init__(self, name, domain):
        self.name = name
        self.domain = domain
        self.content = self.get_site_content()
        self.active = True
        self.activated_at = time.time()
    
    def get_site_content(self):
        try:
            response = requests.get(self.domain)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {self.name}: {e}")
            return None
    
    def monitor_site(self, interval=10):
        while self.active:
            new_content = self.get_site_content()
            if new_content and self.clean_content(new_content) != self.clean_content(self.content):
                print(f"Site {self.name} has changed")
                self.active = False
                msg = f"Site {self.name} has changed. Check it out at {self.domain}"
                twilo_service.send_whatsapp_message(msg)
            else:
                print(f"Monitoring {self.name} for changes")
            time.sleep(interval)
            
    def stop_monitoring(self):
        self.active = False
            
    def print_info(self):
        print(f"**Site monitor for changes**\n🧶 Monitoring: {self.name}\n🔗 With URL: {self.domain}\n✅ Monitor status: {'Active' if self.active else 'Inactive'}")
    
    def clean_content(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        text = soup.get_text(separator=' ')
        return ' '.join(text.split())
    
    def _test_twilio(self):
        msg = f"Site {self.name} has changed. Check it out at {self.domain}"
        twilo_service.send_whatsapp_message(msg)

site = Site("14 Now", "https://www.now14.co.il/tag/%D7%9E%D7%91%D7%96%D7%A7%D7%99%D7%9D/")
# site.monitor_site(5)
time.sleep(3)
site._test_twilio()
