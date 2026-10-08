incident_id = "INC-2026-001"
date = "2026-10-05"
analyst = "Muhammad"
serverity = "High"
time_detected = "2026-10-05 09:13"
time_blocked = "2026-10-05 09:15"
attacker_ip = "185.220.101.45"
target_endpoint = "/login"
attempts = "500"
summary = "Brute-force атака на endpoint /login. 500 попыток за 2 минты с IP 185.220.101.45"
with open("report.md", "w", encoding="utf-8") as f:
    f.write(f"# Incident Report:{incident_id}\n\n## Summary\nДата:{date}\nАналитик:{analyst}\nСерьезность:{serverity}\n\n{summary}\n\n## Timeline\n{time_detected}: Обнаружена подозрительная активность\n{time_blocked}: IP заблокирован на файрволе\n\n## IOC\nIP атакующего:{attacker_ip}\nЦель:{target_endpoint}\nКоличество попыток:{attempts}\n\n## Remediation\n- IP заблокирован на файрволе\n- Включена защита от brute-force\n- Усилен мониторинг endpoint /login")
