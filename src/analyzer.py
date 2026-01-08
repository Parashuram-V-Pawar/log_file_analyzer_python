import re


def ip_analyze_log_file(file_path):
    ip_pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    ip_count = dict()
    unique_ips = set()

    status_pattern = re.compile(r'\d{1,3}$')
    status = dict()

    try:
        with open(file_path, 'r') as file:
            for line in file:
                ip_address = re.search(ip_pattern, line).group()
                if ip_address not in unique_ips:
                    unique_ips.add(ip_address)
                    ip_count[ip_address] = 1
                else:
                    ip_count[ip_address] += 1

                http_status = re.search(status_pattern, line).group()
                status[http_status] = status.get(http_status, 0) + 1
    
    except:
        raise FileNotFoundError("Log file not found")
    
    
    with open("src/log_summary.txt","w") as summary:
        summary.write("IP address summary: \n")
        summary.write("Ip address         Count\n")
        for ip_address, count in ip_count.items():
            summary.write(f"{ip_address:<18}: {count}\n")
        summary.write("\n\nHTTP Error code summary: \n")
        summary.write("status code    count\n")
        for status_code, count in status.items():
            summary.write(f"{status_code:<13} : {count}\n")


if __name__ == "__main__":
    ip_analyze_log_file('src/server_log.txt')