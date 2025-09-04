import subprocess

def generate_report(report_title, content_file):
    """Generates a PDF report with a user-supplied title."""
    

    command = [
        "pandoc",
        content_file,
        "-o",
        "report.pdf",
        "--metadata",
        f"title={report_title}",
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        print("Report generated successfully.")
    else:
        print("Error:", result.stderr)

user_title = input("Enter report title: ")
generate_report(user_title, "report_data.md")
