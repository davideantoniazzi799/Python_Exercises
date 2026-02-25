#Scrivi un programma che:
# 1 - Legge log.txt
# 2 - Conta quanti messaggi contengono: ERROR, WARNING, INFO
# Salva tutto in log_summary.txt nel formato
# ERROR: X
# WARNING: Y
# INFO: Z

log_counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}

with open("log.txt") as file_input, open("log_summary.txt", "w") as file_output:
    for line in file_input:
        line = line.strip()  # rimuove spazi iniziali/finali
        for key in log_counts:
            if line.startswith(key):
                log_counts[key] += 1

    for key, count in log_counts.items():
        file_output.write(f"{key}: {count}\n")