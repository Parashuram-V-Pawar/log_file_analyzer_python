from faker import Faker
import random

def create_log_data(n):
    f = Faker()
    with open('server_log.txt', mode='w') as file:
        for i in range(n):
            log_line = (
                f"{f.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S')} "
                f"{random.choice(['INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL'])} "
                f"{f.sentence(nb_words=6)}"
                f"{f.ipv4()} "
                f"{random.choice([200, 404, 500])}\n"
            )
            file.write(log_line)
