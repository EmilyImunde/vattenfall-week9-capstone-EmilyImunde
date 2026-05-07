
from datetime import datetime


def observability_record(
    notebook_name,
    source_table,
    target_table,
    rows_read,
    rows_written,
    validation_status,
    comments,
):
    return {
        "notebook_name": notebook_name,
        "source_table": source_table,
        "target_table": target_table,
        "rows_read": rows_read,
        "rows_written": rows_written,
        "validation_status": validation_status,
        "execution_timestamp": datetime.utcnow().isoformat(),
        "comments": comments,
    }