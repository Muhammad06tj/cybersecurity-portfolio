with open("security.log.txt", "r") as f:
    for line in f:
        parts = line.split("|")
        parts = [p.strip() for p in parts]
        if parts[1] == 'FAILED_LOGIN':
            print("[ALERT] Неудачная попытка входа: FAILED_LOGIN", parts[2], parts[3])
        hour = parts[0].split(' ')
        hour = hour[1]
        hour = hour.split(':')
        hour = hour[0]
        if parts[1] == 'FILE_CREATED':
            print(f"[ALERT] Создан подозрительный файл") 
        if int(hour) < 6:
            print(f"[ALERT] активность в {int(hour)} часа ночи:", parts[1], parts[3])
            
