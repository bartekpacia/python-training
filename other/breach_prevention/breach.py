rfishield = 0
dfishield = 0
sqlishield = 0

counter = 0
with open("breach.log") as f:
    while True:
        line = f.readline()

        if "blocking reason" in line.lower():
            reason = line.strip().split(': ')[1]
            print(
                f"line {counter}, blocking reason: {reason}")

            if reason == "rfishield":
                rfishield += 1
            elif reason == "dfishield":
                dfishield += 1
            elif reason == "sqlishield":
                sqlishield += 1

        if not line:
            break

        # print(line)
        counter += 1

print(f"rfishield: {rfishield}")
print(f"dfishield: {dfishield}")
print(f"sqlishield: {sqlishield}")
