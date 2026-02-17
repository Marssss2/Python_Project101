files = [
    "data.csv", "report.xlsx", "users.json", "backup.sql", "image.png",
    "notes.txt", "config.yaml", "archive.zip", "presentation.pptx",
    "script.py", "styles.css", "index.html", "database.db",
    "records.csv", "logfile.log", "summary.docx", "metrics.json",
    "photo.jpg", "inventory.csv", "app.js", "diagram.svg",
    "export.xml", "results.xlsx", "transactions.csv", "clients.csv",
    "analysis.ipynb", "server.log", "system.log", "backup_2024.zip",
    "backup_2025.zip", "draft.docx", "thesis.pdf", "research.pdf",
    "slides.pptx", "model.pkl", "weights.h5", "dataset.parquet",
    "raw_data.csv", "clean_data.csv", "processed_data.csv",
    "app_config.ini", "docker-compose.yml", "requirements.txt",
    "README.md", "LICENSE", "main.cpp", "program.java", "mobile.apk",
    "design.fig", "prototype.xd", "video.mp4", "audio.mp3", "voice.wav",
    "spreadsheet.ods", "document.odt", "presentation.odp",
    "compressed.rar", "firmware.hex", "microcontroller.ino",
    "circuit.sch", "layout.pcb", "simulation.sim",
    "finance_report_2023.xlsx", "finance_report_2024.xlsx", "finance_report_2025.xlsx",
    "students.db", "employees.db", "attendance.csv",
    "project1.py", "project2.py", "project3.py",
    "api_response.json", "error_dump.log", "temp.tmp",
    "cloud_backup.tar", "deployment.sh", "automation.ps1",
    "network_config.cfg", "security.key", "certificate.crt",
    "bigdata.avro", "stream_data.kafka", "warehouse.sql",
    "etl_pipeline.py", "ml_model.joblib", "training_data.csv",
    "validation_data.csv", "test_data.csv", "output_results.json",
    "notes_january.txt", "meeting_minutes.txt", "tasks.csv", "budget.xlsx",
    "diagram_flow.png", "logo.svg", "script_backup.py", "final_report.docx",
    "lecture_notes.pdf", "todo_list.txt", "experiment_data.csv",
    "photo_event1.jpg", "photo_event2.jpg", "presentation_final.pptx",
    "database_backup.sql", "webpage.html", "styles_backup.css",
    "audio_clip.wav", "video_clip.mp4"
]


for file in files:
    if not file.endswith('.csv'):
        print('Not all file is csv')
        break
else:
    print('All File is csv')