# Log file analyzer. Create 3 fake `.txt` log files with lines like `"[ERROR] connection failed"`, `"[INFO] server started"`, `"[WARNING] high memory"`. Script: counts each level across all files, finds the most repeated error message, writes a summary report to a new file. Use `pathlib`, comprehensions, file I/O.

from pathlib import Path

logsFolder = Path("logs")
logsFolder.mkdir(exist_ok=True)

logfiles = list(logsFolder.glob("*"))

strLog = (f"Files found in {logsFolder.name}:")
for file in logsFolder.glob("*.txt"):
    strLog = strLog + (f"\n\t{file.name}")

all_lines = [line for file in logfiles for line in file.read_text().splitlines()]
strLog = strLog + ("\n\nAll types of issues in log files:\n")
for line in range(len(all_lines)):
    prevLine = all_lines[line]
    strLog = strLog + (f"\t{prevLine}\n")

counts = {}
for issueType in all_lines:
    level = issueType.split("]")[0] + "]"
    if level in counts:
        counts[level] += 1
    else:
        counts[level] = 1

strLog = strLog + ("\nCounts of Each type of issue:\n")
for issue, countIssue in counts.items():
    previssue = (f"{issue}: {countIssue}")
    strLog = strLog + (f"\t{previssue}\n")

errorLines = [line for line in all_lines if line.startswith("[ERROR]")]

countsError = {}
for errorType in errorLines:
    if errorType in countsError:
        countsError[errorType] += 1
    else:
        countsError[errorType] = 1

strLog = strLog + ("\nCounts of Error types:\n")
for Error, countIssue in countsError.items():
    previssue = (f"{Error}: {countIssue}")
    strLog = strLog + (f"\t{previssue}\n")

mostErrorRepeated = max(countsError, key = lambda msg : countsError[msg])
strLog = strLog + (f"\nMost Repeating Error Message: {mostErrorRepeated}\n")

summaryLog = Path("logs/summaryReport.txt")
summaryLog.write_text(strLog)