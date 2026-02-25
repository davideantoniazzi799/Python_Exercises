#Scrivi un programma che:
# 1 - Conta ERROR, WARNING, INFO da server_log.txt
# 2 - Calcola la percentuale di ciascun tipo sul totale
# 3 - Salva in server_report.txt

log_counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}

with open("server_log.txt") as file_input, open("server_report.txt", "w") as file_output:
    tot_logs = 0
    for line in file_input:
        line = line.strip()
        for key in log_counts:
            if line.startswith(key):
                log_counts[key] += 1
                tot_logs += 1

    for key, count in log_counts.items():
        file_output.write(f"{key}: {count} ({count/tot_logs*100:.2f}%)\n")